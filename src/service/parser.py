#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List
from bs4 import BeautifulSoup
from src.dto.bet import Bet
from src.dto.bet_info import BetInfo
from src.dto.event import Event


class Parser:
    @staticmethod
    def by_event(data: str) -> List[Event]:
        data = BeautifulSoup(data, 'lxml')\
            .body.find('div', {'class': 'timerange timerange_now sys-timerange'})\
            .find_all('div', {'class': 'bet-item'})
        event_list = []
        for line in data:
            tour_name = str(line.find('div', {'class': 'bet-match__picture-text'}).text).strip()
            best_of = str(line.find('div', {'class': 'sys-bo'}).text).strip()
            start_time = str(line.find('span', {'class': 'sys-datetime'}).text).strip()
            t1_name = str(line.find('div', {'class': 'bet-team__name sys-t1name'}).text).strip()
            t2_name = str(line.find('div', {'class': 'bet-team__name sys-t2name'}).text).strip()

            bet_list = []
            bet_name = 'winner'
            ratio = 1.0
            summary = 1
            percent = 10
            team_left = BetInfo(ratio, summary, percent)
            team_right = BetInfo(ratio, summary, percent)
            bet = Bet(bet_name, team_left, team_right)
            bet_list.append(bet)

            event_list.append(Event(start_time, best_of, tour_name, t1_name, t2_name, bet_list))
        return event_list
