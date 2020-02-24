#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src.dto.color import C

COMMA = f'{C.BLACK},{C.END} '
L_BRACKET = f'{C.YELLOW}' + "{" + f'{C.END}'
R_BRACKET = f'{C.YELLOW}' + "}" + f'{C.END}'


def tostring(obj: object) -> object:
    obj.__str__ = lambda o: f'{L_BRACKET}%s{R_BRACKET}' % (
        f'{COMMA}'.join(f'{C.RED + k + C.END}: {o.__dict__[k]}'
                        for k in obj.__init__.__code__.co_varnames[1:])
    )
    obj.__repr__ = lambda o: f'{L_BRACKET}%s{R_BRACKET}' % (
        f'{COMMA}'.join(f'{C.RED + k + C.END}: {o.__dict__[k]}'
                        for k in obj.__init__.__code__.co_varnames[1:])
    )
    return obj
