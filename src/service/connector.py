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
    @staticmethod
    def get(path: str) -> str:
        # todo: remove in future versions
        if 'https://' in path:
            return Connector._get_html(path)
        return Connector._get_test_html(path)

    @staticmethod
    def _get_html(path: str) -> str:
        try:
            settings = ChromeOptions()
            settings.add_argument(f'user-data-dir={abspath("../cache")}')
            browser = Chrome('../resource/lib/chrome_driver.exe', options=settings)
            del settings
            browser.set_window_size(1920, 1080)
            browser.get(path)
            sleep(5)
            html = str(browser.page_source)
            browser.close()
            del browser
            return html
        except WebDriverException:
            trace(limit=1, file=stdout)

    @staticmethod
    def _get_test_html(path: str) -> str:
        try:
            with open(path, 'r', encoding='utf-8') as file:
                return str(file.read())
        except FileNotFoundError:
            trace(limit=1, file=stdout)
