#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from src.dto import color as c


def setup():
    logging.addLevelName(logging.WARNING, "\033[1;31m[%s]\033[1;0m" % logging.getLevelName(logging.WARNING))
    logging.addLevelName(logging.ERROR, "\033[1;41m[%s]\033[1;0m" % logging.getLevelName(logging.ERROR))
    logging.addLevelName(logging.INFO, "\033[1;32m[%s]\033[1;0m" % logging.getLevelName(logging.INFO))
    logging.addLevelName(logging.DEBUG, "\033[1;34m[%s]\033[1;0m" % logging.getLevelName(logging.DEBUG))
    _ = f'{c.BOLD}-{c.END}'
    time = f'{c.HEADER}%(asctime)s{c.END}'
    lvl = f'{c.GREEN}%(levelname)s{c.END}'
    process = f'{c.BOLD}%(funcName)s{c.END}'
    msg = f'{c.BOLD}%(message)s{c.END}'
    log_format = f'{time} {lvl} {process} {_} {msg}'
    logging.basicConfig(format=log_format,
                        level=logging.INFO)
