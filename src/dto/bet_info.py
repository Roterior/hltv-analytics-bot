#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src.util.tostring import tostring


@tostring
class BetInfo:
    info: str = None
    sum: str = None

    def __init__(self, info: str, sum: str):
        self.info = info
        self.sum = sum
