#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from time import sleep
from src.service.connector import Connector
from src.service.parser import Parser


def process():
    logging.basicConfig(level=logging.INFO)
    # path = 'https://betscsgo.me'
    path = '../resource/data/html_bet_cs_go.txt'
    # data = Connector.get(path)

    # with open('../resource/data/output.txt', 'w', encoding='utf-8') as file:
    #     file.write(data)

    while True:
        data = Connector.get(path)

        parsed_data_now = Parser.betcsgo(data, 'now')
        logging.info('printing result with state NOW')
        for event in parsed_data_now:
            print(event)
            for i in event.bet_list:
                print('        ' + str(i))

        parsed_data_next = Parser.betcsgo(data, 'next')
        logging.info('printing result with state NEXT')
        for event in parsed_data_next:
            print(event)
            for i in event.bet_list:
                print('        ' + str(i))

        sleep(60)

    pass
