# -*- coding: utf-8 -*-
# @Author: youralien
# @Date:   2018-02-21 22:06:46
# @Last Modified by:   youralien
# @Last Modified time: 2018-02-22 01:32:38

from loading import loadtweets, loadtweetsdf, loadredditpostsdf


def test_loadtweets():
    tweets = loadtweets()
    print len(tweets)
    assert len(tweets) == 5776


def test_loadtweetsdf():
    df = loadtweetsdf()
    assert len(df) == 5776


def test_loadredditpostsdf():
    df = loadredditpostsdf()
    print len(df)
