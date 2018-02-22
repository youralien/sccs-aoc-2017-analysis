# -*- coding: utf-8 -*-
# @Author: youralien
# @Date:   2018-02-21 21:57:22
# @Last Modified by:   youralien
# @Last Modified time: 2018-02-21 22:08:24

import os
import codecs
import json


def loadtweets(path=None):
    if not path:
        directory = os.path.dirname(os.path.realpath(__file__))
        path = os.path.join(directory, 'tweets_n.json')
    with codecs.open(path, 'r', 'utf-8') as f:
        tweets = json.load(f, encoding='utf-8')
    return tweets
