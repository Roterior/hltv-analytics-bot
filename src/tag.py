#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Tag:
    name: str
    attr: str
    is_closable: bool

    def __init__(self, name: str):
        self.name = name
