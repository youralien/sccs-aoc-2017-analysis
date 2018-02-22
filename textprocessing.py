# -*- coding: utf-8 -*-
# @Author: youralien
# @Date:   2018-02-21 22:04:01
# @Last Modified by:   youralien
# @Last Modified time: 2018-02-22 01:13:27


def i_just_completed(df):
    return df[df['text'].str.contains('I just completed')]


def startswith_i_just_completed(df):
    return df[df['text'].str.startswith('I just completed')]


def i_just_completed_all(df):
    return df[df['text'].str.contains('I just completed all')]
