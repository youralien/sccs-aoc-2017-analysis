# -*- coding: utf-8 -*-
# @Author: youralien
# @Date:   2018-02-21 22:04:01
# @Last Modified by:   youralien
# @Last Modified time: 2018-02-22 01:59:06


def i_just_completed(df):
    return df[df['text'].str.contains('I just completed')]


def startswith_i_just_completed(df):
    return df[df['text'].str.startswith('I just completed')]


def i_just_completed_all(df):
    return df[df['text'].str.contains('I just completed all')]


def reddit_not_about_completed(df):
    df = df[~df['title'].str.contains('completed')]
    df = df[~df['title'].str.contains('Here is my')]
    df = df[~df['title'].str.contains("Here's my")]
    return df


def reddit_i_just_completed(df):
    return df[df['title'].str.contains('I just completed')]


def reddit_completed(df):
    df = df[df['title'].str.contains(
        r'^.*(complete|finish|solve).*$')]
    return df


def reddit_25(df):
    df = df[df['title'].str.contains(
        r'^.*(25).*$')]
    return df
