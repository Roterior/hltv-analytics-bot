#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep


def connection():
    print('Starting...')
    # link_bet_cs_go = 'https://betscsgo.me'
    # link_gg_bet = 'https://gg.bet/ru/betting'
    # driver = webdriver.Chrome('../resource/lib/chrome_driver.exe')
    # driver.get(link_bet_cs_go)
    # sleep(15)
    # html_code = driver.page_source
    # driver.close()

    test_data_file = open('../resource/data/html_bet_cs_go.txt', 'r', encoding='utf-8')
    data = test_data_file.readlines()
    test_data_file.close()
    # for i, line in enumerate(data):
    #     print(line.strip())
    #     if '<div class="sys-timerange-header timerange__header">Текущие события</div>' in line:
    #         print(i)

    print(data[2048].strip())
    print(data[2055].strip())

    # soup = BeautifulSoup(html_code, 'html.parser')
    # file = open('../output', 'w', encoding="utf-8")
    # file.write(str(html_code))
    # file.close()
    print("Finishing...")
