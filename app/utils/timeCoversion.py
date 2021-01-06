#!/usr/bin/env python
# coding=utf-8

from datetime import datetime


def utc2local(utc_dtm):
    # UTC 时间转本地时间（ +8:00 ）
    local_tm = datetime.fromtimestamp(0)
    utc_tm = datetime.utcfromtimestamp(0)
    offset = local_tm - utc_tm
    real_date = utc_dtm + offset
    return real_date.strftime("%Y-%m-%d %H:%M:%S")

def local2utc(local_dtm):
    # 本地转UTC -8:00
    return datetime.utcfromtimestamp(local_dtm.timestamp())



if __name__ == "__main__":

    utc_tm = datetime.utcnow()
    print( "src utc time:\t", utc_tm.strftime("%Y-%m-%d %H:%M:%S") )

    # UTC 转本地
    local_tm = utc2local(utc_tm)
    print( "tran loc time:\t", local_tm.strftime("%Y-%m-%d %H:%M:%S") )

    # 本地转 UTC
    utc_tran = local2utc(local_tm)
    print( "tran utc time:\t", utc_tran.strftime("%Y-%m-%d %H:%M:%S") )