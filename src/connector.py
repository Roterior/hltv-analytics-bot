#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep
from sys import stdout
from os.path import abspath
from traceback import print_exc as trace
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.common.exceptions import WebDriverException


class Connector:
    path = ''
    sleep_time = 5

    def __init__(self, path: str):
        self.path = path

    def connection(self) -> str:
        # todo: remove in future versions
        if 'https://' in self.path:
            return self.get_html()
        else:
            return self.get_test_html()

    def get_html(self) -> str:
        try:
            settings = ChromeOptions()
            settings.add_argument(f'user-data-dir={abspath("../cache")}')
            browser = Chrome('../resource/lib/chrome_driver.exe', options=settings)
            browser.set_window_size(1920, 1080)
            browser.get(self.path)
            sleep(self.sleep_time)
            html = str(browser.page_source)
            browser.close()
            return html
        except WebDriverException:
            trace(limit=1, file=stdout)

    def get_test_html(self) -> str:
        try:
            with open(self.path, 'r', encoding='utf-8') as file:
                return str(file.read())
        except FileNotFoundError:
            trace(limit=1, file=stdout)
