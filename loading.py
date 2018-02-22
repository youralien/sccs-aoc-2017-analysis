# -*- coding: utf-8 -*-
# @Author: youralien
# @Date:   2018-02-21 21:57:22
# @Last Modified by:   youralien
# @Last Modified time: 2018-02-21 23:33:46

import os
import codecs
import json
import pandas as pd


def loadtweets(path=None, sort=True):
    if not path:
        directory = os.path.dirname(os.path.realpath(__file__))
        path = os.path.join(directory, 'tweets_n.json')
    with codecs.open(path, 'r', 'utf-8') as f:
        tweets = json.load(f, encoding='utf-8')
    if sort:
        # tweets were scraped in reverse chrnological order
        tweets = tweets[::-1]
    return tweets


def loadtweetsdf(path=None, sort=True):
    df = pd.DataFrame(loadtweets(path, sort))
    df['replies'] = pd.to_numeric(df['replies'])
    df['likes'] = pd.to_numeric(df['likes'])
    df['retweets'] = pd.to_numeric(df['retweets'])
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df
