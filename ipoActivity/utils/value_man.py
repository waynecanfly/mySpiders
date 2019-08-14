#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 对数据为空的值进行处理
def manage_val(anyVal):
    if anyVal is None:
        anyVal2 = '--'
    else:
        anyVal2 = anyVal
    return anyVal2