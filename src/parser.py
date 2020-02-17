#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src.tag import Tag


class Parser:
    data: str

    def __init__(self, data: str):
        self.data = data

    def parse(self):
        temp = []
        line = ''
        for letter in self.data:
            if letter == '>':
                temp.append(line + letter)
                line = ''
            else:
                line = line + letter

        for i in temp:
            line = i.strip()
            if 'script' not in line:
                # print(i.strip())
                if 'timerange_now' in line:
                    print(line)

        return self.data
