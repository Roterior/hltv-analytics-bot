#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src.service.connector import Connector
from src.service.parser import Parser


def process():
    print('Starting process...')

    # path = 'https://betscsgo.me'
    path = '../resource/data/html_bet_cs_go.txt'
    data = Connector.get(path)

    # with open('../resource/data/output.txt', 'w', encoding='utf-8') as file:
    #     file.write(data)

    parsed_data = Parser.by_event(data)

    for i in parsed_data:
        print(i.str())

    print('Process done')
