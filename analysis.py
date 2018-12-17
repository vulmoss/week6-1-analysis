#-*-coding:utf-8-*-
#__author__ = 'anondba'

import json
import pandas as pd

def analysis(file,user_id):
    times=0
    minutes = 0
    f=open(file)
    records=json.load(f)
    for item in records:
        if item['user_id'] == 'user_id':
            times += 1
            minutes += item[item['user_id']]['minutes']
    print(times,minutes)
    return times,minutes


if __name__ == '__main__':
    analysis('user_study.json','185399')
    
