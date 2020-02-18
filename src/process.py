#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src.connector import Connector
from src.parser import Parser


def process():
    print('Starting process...')

    # path = 'https://betscsgo.me'
    path = '../resource/data/html_bet_cs_go.txt'
    connect = Connector(path)
    data = connect.connection()

    # file = open('../resource/data/output.txt', 'w', encoding="utf-8")
    # file.write(data)
    # file.close()

    parser = Parser(data)
    parsed_data = parser.parse()

    for i in parsed_data:
        print(i.str())

    print('Process done')
