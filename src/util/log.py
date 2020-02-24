#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from src.dto.color import C


def setup():
    logging.addLevelName(logging.WARNING, "\033[1;31m[%s]\033[1;0m" % logging.getLevelName(logging.WARNING))
    logging.addLevelName(logging.ERROR, "\033[1;41m[%s]\033[1;0m" % logging.getLevelName(logging.ERROR))
    logging.addLevelName(logging.INFO, "\033[1;32m[%s]\033[1;0m" % logging.getLevelName(logging.INFO))
    logging.addLevelName(logging.DEBUG, "\033[1;34m[%s]\033[1;0m" % logging.getLevelName(logging.DEBUG))
    _ = f'{C.BOLD}-{C.END}'
    time = f'{C.HEADER}%(asctime)s{C.END}'
    lvl = f'{C.GREEN}%(levelname)s{C.END}'
    process = f'{C.BOLD}%(funcName)s{C.END}'
    msg = f'{C.BOLD}%(message)s{C.END}'
    log_format = f'{time} {lvl} {process} {_} {msg}'
    logging.basicConfig(format=log_format,
                        level=logging.INFO)
