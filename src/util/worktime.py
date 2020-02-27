#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime


def worktime(f):
    def wrapper(*args, **kwargs):
        s = datetime.now()
        r = f(*args, **kwargs)
        print(f'func: "{f.__name__}" done in {round((datetime.now() - s).total_seconds(), 3)} sec')
        return r
    return wrapper
