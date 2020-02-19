#!/usr/bin/env python
# -*- coding: utf-8 -*-


class BetInfo:
    ratio: float = None
    summary: int = None
    percent: int = None

    def __init__(self, ratio: float, summary: int, percent: int):
        self.ratio = ratio
        self.summary = summary
        self.percent = percent
