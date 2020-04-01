'''
@Author: your name
@Date: 2020-02-27 16:29:04
@LastEditTime: 2020-03-05 08:03:56
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \dataset\dataset.py
'''
from string import digits
import os
import json
import jieba
import numpy as np

remove_digits = str.maketrans('', '', digits)

file_data = []
file_datas = []
pre_json = {}
data_json={}

path_list = os.listdir('./')

for filename in path_list:
    file_list = []
    if os.path.splitext(filename)[1] == '.txt':
        file = open('./'+filename, encoding='UTF-8')
        file_list += file.read().splitlines()
        file.close()
        file_datas.append(file_list)
        
for file_data in file_datas:
    print(file_data)
    KG_data=[]
    entity_head = []
    entity_tail = []
    relation = file_data[0]
    for i in range(1,len(file_data),2):
        data_buf = file_data[i]
        # data_buf = data_buf.replace('.','')
        entity_head.append(data_buf.lower())

    for i in range(2,len(file_data),2):
        entity_tail.append(file_data[i])
    
    for i in range(len(entity_head)):
        buf_list = []
        buf_list.append(entity_head[i])
        buf_list.append(relation)
        buf_list.append(entity_tail[i])
        KG_data.append(buf_list)

    # 生成三元组   
    for i in range(len(KG_data)): 
        data_json.setdefault(KG_data[i][0],{})[KG_data[i][1]] = KG_data[i][2]
    # for key in data_json.keys():
    #     for key2 in data_json[key].keys():
    #         pre_json.setdefault(KG_data[i][0],{})[KG_data[i][1]] = data_json[key][key2]
    data_file = open('./data/data.json', 'w', encoding='UTF-8')
    json.dump(data_json, data_file, ensure_ascii=False)
    data_file.close()



    # 生成字典
    dict_file = open('./dict/dict_buf.txt', 'a+', encoding='UTF-8')
    for i in range(len(KG_data)):
        dict_file.write(KG_data[i][0]+' nz'+'\n')
        dict_file.write(KG_data[i][1]+' nz'+'\n')
    dict_file.close()

    # 生成问题
    QA_file = open('./QA/QA_buf.txt', 'a+', encoding='UTF-8')
    for i in range(len(KG_data)):
        if KG_data[i][1] =='定义' or KG_data[i][1] == '概念':
            QA_file.write(KG_data[i][0]+'的定义是什么'+'\t'+KG_data[i][0]+'\t'+KG_data[i][1]+'\n')
            QA_file.write(KG_data[i][0]+'的概念是什么'+'\t'+KG_data[i][0]+'\t'+KG_data[i][1]+'\n')
            QA_file.write('什么是'+KG_data[i][0]+'的定义'+'\t'+KG_data[i][0]+'\t'+KG_data[i][1]+'\n')
            QA_file.write('什么是'+KG_data[i][0]+'的概念'+'\t'+KG_data[i][0]+'\t'+KG_data[i][1]+'\n')
            QA_file.write('什么是'+KG_data[i][0]+'\t'+KG_data[i][0]+'\t'+KG_data[i][1]+'\n')
            QA_file.write(KG_data[i][0]+'是什么'+'\t'+KG_data[i][0]+'\t'+KG_data[i][1]+'\n')
            QA_file.write(KG_data[i][0]+'定义'+'\t'+KG_data[i][0]+'\t'+KG_data[i][1]+'\n')
            QA_file.write(KG_data[i][0]+'概念'+'\t'+KG_data[i][0]+'\t'+KG_data[i][1]+'\n')
            QA_file.write(KG_data[i][0]+'\t'+KG_data[i][0]+'\t'+KG_data[i][1]+'\n')
    QA_file.close()

#清洗数据，文本去重
lines_seen=set()
data_file_buf = open('./dict/dict_buf.txt', 'r', encoding='UTF-8')
data_file = open('./dict/dict.txt', 'w', encoding='UTF-8')
for line in data_file_buf:
    if line not in lines_seen:
        data_file.write(line)
        lines_seen.add(line)
data_file_buf.close()
data_file.close()

data_file_buf = open('./QA/QA_buf.txt', 'r', encoding='UTF-8')
data_file = open('./QA/QA.txt', 'w', encoding='UTF-8')
for line in data_file_buf:
    if line not in lines_seen:
        data_file.write(line)
        lines_seen.add(line)
data_file_buf.close()
data_file.close()

# 删除中间文件
os.remove('./dict/dict_buf.txt')
os.remove('./QA/QA_buf.txt')

