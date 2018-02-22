# -*- coding: utf-8 -*-
# @Author: youralien
# @Date:   2018-02-21 22:10:45
# @Last Modified by:   youralien
# @Last Modified time: 2018-02-21 23:02:24


def unique_users(df):
    return df.fullname.unique()


def num_tweets_per_unique_user(df):
    """
    (λ. borkdude)                                       44
    Walt Mankowski                                      41
    Jochem                                              40
    Joshua Carrigan                                     39
    Pete Corey                                          38
    Ardavast Dayleryan                                  32
    Todd Ginsberg                                       31
    """
    return df.fullname.value_counts()


def sort_by_highest_number_replies(df, ascending=True):
    return df.sort_values('replies', ascending=ascending)


def get_reply_noreply_dfs(df):
    return (
        df[df['replies'] == '0'],   # 4629
        df[df['replies'] != '0'])   # 1147
