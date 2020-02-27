#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from src.service import connector
from src.service import parser
from src.util.worktime import worktime


@worktime
def process():
    # path = 'https://betscsgo.me'
    path = '../resource/data/html_bet_cs_go.txt'

    data = connector.get(path)

    parsed_data_now = parser.betcsgo(data, 'now')
    logging.info('printing result with state NOW')
    for event in parsed_data_now:
        print(event)
        for i in event.bet_list:
            if i.name == 'Winner':
                print('        ' + str(i))

    parsed_data_next = parser.betcsgo(data, 'next')
    logging.info('printing result with state NEXT')
    for event in parsed_data_next:
        print(event)
        for i in event.bet_list:
            if i.name == 'Winner':
                print('        ' + str(i))

    pass
