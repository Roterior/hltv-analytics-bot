#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src.dto.bet_info import BetInfo
from src.util.tostring import tostring


@tostring
class Bet:
    name: str = None
    left: BetInfo = None
    right: BetInfo = None

    def __init__(self, name: str, left: BetInfo, right: BetInfo):
        self.name = name
        self.left = left
        self.right = right
