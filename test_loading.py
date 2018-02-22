# -*- coding: utf-8 -*-
# @Author: youralien
# @Date:   2018-02-21 22:06:46
# @Last Modified by:   youralien
# @Last Modified time: 2018-02-21 22:08:45

from loading import loadtweets


def test_loadtweets():
    tweets = loadtweets()
    print len(tweets)
    assert len(tweets) == 5776

if __name__ == '__main__':
    test_loadtweets()
