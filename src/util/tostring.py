#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src.dto import color as c

COMMA = f'{c.BLACK},{c.END} '
L_BRACKET = f'{c.YELLOW}' + "{" + f'{c.END}'
R_BRACKET = f'{c.YELLOW}' + "}" + f'{c.END}'


def tostring(obj: object) -> object:
    def param():
        return lambda o: f'{L_BRACKET}%s{R_BRACKET}' % \
                         (
                             f'{COMMA}'.join(f'{c.RED + k + c.END}: {o.__dict__[k]}'
                                             for k in obj.__init__.__code__.co_varnames[1:])
                         )

    obj.__str__ = param()
    obj.__repr__ = param()
    return obj
