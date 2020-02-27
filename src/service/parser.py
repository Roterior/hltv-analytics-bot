#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from typing import List
from bs4 import BeautifulSoup
from src.dto.bet import Bet
from src.dto.bet_info import BetInfo
from src.dto.event import Event


def betcsgo(data: str, state: str) -> List[Event]:
    logging.info(f'parsing html by event with state: {state}')
    data_events = BeautifulSoup(data, 'lxml').body.find('div', {'class': 'tabs-container__content'})
    if state == 'all':
        pass
    else:
        event_list = _by_event(data_events, state)
        logging.info('parsing done')
        return event_list


def _by_event(data_events, state: str) -> List[Event]:
    event_list = []
    if state == 'now':
        data_event_list = data_events \
            .find('div', {'class': 'timerange timerange_now sys-timerange'}) \
            .find_all('div', {'class': 'bet-item'})
    elif state == 'next':
        data_event_list = data_events \
            .find('div', {'class': 'timerange timerange_next sys-timerange'}) \
            .find_all('div', {'class': 'bet-item'})
    else:
        logging.info('SOMETHING WENT WRONG!')
        raise ValueError
    logging.info(f'parsing found {len(data_event_list)} events')
    for line in data_event_list:
        main_block = line.find('div', {'class': 'bet-match'})
        start_time = str(main_block.find('span', {'class': 'sys-datetime'}).text).strip()
        best_of = str(main_block.find('div', {'class': 'sys-bo'}).text).strip()
        tour_name = str(main_block.find('div', {'class': 'bet-match__picture-text'}).text).strip()
        t1_name = str(main_block.find('div', {'class': 'bet-team__name sys-t1name'}).text).strip()
        t2_name = str(main_block.find('div', {'class': 'bet-team__name sys-t2name'}).text).strip()
        bet_list = []
        name = 'Winner'
        summary_l = str(main_block.find('div', {'class': 'sys-stat-abs-1'}).text).strip()
        left = BetInfo(t1_name, summary_l)
        summary_r = str(main_block.find('div', {'class': 'sys-stat-abs-2'}).text).strip()
        right = BetInfo(t2_name, summary_r)
        bet_main = Bet(name, left, right)
        bet_list.append(bet_main)
        extra_block = line.findAll('div', {'class': 'bet-events__item'})
        for tag in extra_block:
            name = str(tag.find('div', {'class': 'bet-event__text-inside-part'}).text).strip()
            info_l = str(tag.find('div', {'class': 'bet-team_left'}).text).strip()
            summary_l = str(tag.find('div', {'class': 'sys-stat-abs-1'}).text).strip()
            left = BetInfo(info_l, summary_l)
            info_r = str(tag.find('div', {'class': 'bet-team_right'}).text).strip()
            summary_r = str(tag.find('div', {'class': 'sys-stat-abs-2'}).text).strip()
            right = BetInfo(info_r, summary_r)
            bet = Bet(name, left, right)
            bet_list.append(bet)
        event_list.append(Event(start_time, best_of, tour_name, t1_name, t2_name, bet_list))
    return event_list
