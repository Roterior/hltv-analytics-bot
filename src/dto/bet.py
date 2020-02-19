#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src.dto.bet_info import BetInfo


class Bet:
    bet_name: str = None
    team_left: BetInfo = None
    team_right: BetInfo = None

    def __init__(self, bet_name: str, team_left: BetInfo, team_right: BetInfo):
        self.bet_name = bet_name
        self.team_left = team_left
        self.team_right = team_right
