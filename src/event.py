#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Event:
    start_time: str = None
    best_of: str = None
    tour_name: str = None
    bet_list: dict = None

    def __init__(self, start_time: str, best_of: str, tour_name: str, bet_list: dict):
        self.start_time = start_time
        self.best_of = best_of
        self.tour_name = tour_name
        self.bet_list = bet_list

    def str(self) -> str:
        return f'{{' \
               f'start_time={self.start_time}, ' \
               f'best_of={self.best_of}, ' \
               f'tour_name={self.tour_name}, ' \
               f'bet_list={self.bet_list}' \
               f'}}'
