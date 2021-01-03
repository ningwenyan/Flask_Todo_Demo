#!/usr/bin/env python
# coding=utf-8

from redis import StrictRedis

# 创建连接
redis = StrictRedis(host='192.168.0.101', port=6379, db=0)


def set(key, value, timeout=60):
    return redis.set(key, value, ex=timeout)

def get(key):
    return redis.get(key)

def delete(key):
    return redis.delete(key)



if __name__ == '__main__':
    redis.set('key', 'value',ex=60)
    print(redis.get('key'))