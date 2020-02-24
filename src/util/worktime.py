#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime


def worktime(f):
    def wrapper(*args, **kwargs):
        s = datetime.now()
        r = f(*args, **kwargs)
        print(f'func: "{f.__name__}" done in {(datetime.now() - s).total_seconds()} ms')
        return r
    return wrapper
