#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sys import exit
from src.service.process import process
from src.util import log


def run():
    log.setup()
    process()
    exit()


if __name__ == '__main__':
    run()
