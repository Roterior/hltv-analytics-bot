#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import traceback
from os.path import abspath
from time import sleep

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import WebDriverException


def connection():
    # link_bet_cs_go = 'https://betscsgo.me'
    # data = get_html(link_bet_cs_go)

    path = '../resource/data/html_bet_cs_go.txt'
    data = get_test_html(path)

    # file = open('../resource/data/output.txt', 'w', encoding="utf-8")
    # file.write(data)
    # file.close()

    """
    --- PROCESSING DATA ---
    """

    parsed_data = parse(data)
    print(parsed_data)

    # num = 0
    # for i, line1 in enumerate(data):
    #     if 'timerange timerange_now sys-timerange' in line1:
    #         num = i
    # row = data[num+2].strip()
    # temp = []
    # cur = ''
    # for letter in row:
    #     if letter == '>':
    #         temp.append(cur.strip() + letter)
    #         cur = ''
    #     else:
    #         cur = cur + letter

    # print(temp)
    # tournament_names = []
    # is_print = False
    # for num, i in enumerate(temp):
    #     if is_print:
    #         tournament_names.append(i.split('<')[0])
    #         is_print = False
    #     if 'bet-match__picture-text' in i:
    #         is_print = True
    #         continue

    # print(len(tournament_names))

    # soup = BeautifulSoup(data, 'html.parser')
    # parse_html = soup.contents
    # print(parse_html)

    print('Finishing...')


def parse(data):

    return data


def get_html(address) -> str:
    try:
        settings = webdriver.ChromeOptions()
        settings.add_argument(f'user-data-dir={abspath("../cache")}')
        browser = webdriver.Chrome('../resource/lib/chrome_driver.exe', options=settings)
        browser.set_window_size(1920, 1080)
        browser.get(address)
        sleep(10)
        html = str(browser.page_source)
        browser.close()
        return html
    except WebDriverException:
        traceback.print_exc(limit=1, file=sys.stdout)


def get_test_html(path) -> str:
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return str(file.read())
    except FileNotFoundError:
        traceback.print_exc(limit=1, file=sys.stdout)
