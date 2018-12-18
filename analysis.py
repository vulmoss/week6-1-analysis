#-*-coding:utf-8-*-
#__author__ = 'anondba'

import json
import pandas as pd

def analysis(file, user_id):
    """从 file json 文件中统计出 user_id 指定用户的学习数据, 纯 python 实现

    Args:
        file(str): json file name
        user_id(int): user id
    """

    times = 0
    minutes = 0

    try:
        f = open(file) #打开文件
        records = json.load(f) #将json加载
        for item in records: #遍历没一行
            if item['user_id'] != user_id: #行中的user_id的值不等于输入的数值
                continue   #不相等的话就跳过这条数据
            times += 1  #这个user_id的数值的times加1
            minutes += item['minutes'] #minutes的值是行中的minnutes的相加
        f.close() #关闭文件
    except:  #没有文件的话，except
        pass 
    print(times,minutes)
    return times, minutes


if __name__ == '__main__':
    analysis('user_study.json',199071)
    
