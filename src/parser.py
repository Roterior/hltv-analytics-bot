#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List
from bs4 import BeautifulSoup
from src.event import Event


class Parser:
    data: str = None

    def __init__(self, data: str):
        self.data = data

    def parse(self) -> List[Event]:
        data = BeautifulSoup(self.data, 'lxml')
        data = data.body.find('div', {'class': 'timerange timerange_now sys-timerange'})
        data = data.find_all('div', {'class': 'bet-item'})
        event_list = []
        for i in data:
            tour_name = str(i.find('div', {'class': 'bet-match__picture-text'}).text).strip()
            best_of = str(i.find('div', {'class': 'sys-bo'}).text).strip()
            start_time = str(i.find('span', {'class': 'sys-datetime'}).text).strip()
            bet_list = {}
            event_list.append(Event(start_time, best_of, tour_name, bet_list))
        return event_list
