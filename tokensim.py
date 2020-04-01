'''
@Author: your name
@Date: 2020-03-04 13:52:22
@LastEditTime: 2020-03-05 08:09:02
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \KGQA-welderdefine\tokensim.py
'''
from gensim import corpora, models, similarities
from collections import defaultdict
import json
import jieba
jieba.load_userdict('./dict/dict.txt')

# 加载三元组
_3d_file = open('./data/data.json', 'r', encoding='UTF-8')
data_3d = json.load(_3d_file)
_3d_file.close()
# 加载问答数据
QA_path = './QA/QA.txt'
QA_dataList = []
QA_entity = []
QA_relation = []

QA_file = open(QA_path, 'r', encoding='UTF-8')
QA_data = QA_file.read().splitlines()

for words in QA_data:
    QA_dataList.append(words.split('\t')[0])
    QA_entity.append(words.split('\t')[1])
    QA_relation.append(words.split('\t')[2])

texts = []
for line in QA_dataList:
    words = ' '.join(jieba.cut(line)).split(' ')
    texts.append(words)

frequency = defaultdict(int)  # 构建一个字典对象
for text in texts:
    for word in text:
        frequency[word] += 1
texts = [[word for word in text if frequency[word] > 1] for text in texts]

dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]

tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]

index = similarities.MatrixSimilarity(corpus_tfidf)

def get_similar(token):
    words=[]
    token = ' '.join(jieba.cut(token)).split(' ')
    for word in token:
        words.append(word.lower())
    print(words)
    new_vec = dictionary.doc2bow(words)
    new_vec_tfidf = tfidf[new_vec]  # 将待比较文档转换为tfidf表示方法
    sims = index[new_vec_tfidf]
    sims_list = sims.tolist()
    if max(sims_list) < 0.5:
        return 'NO DATA'
    else:
        QA_data_act = QA_dataList[sims_list.index(max(sims_list))]
        num = QA_dataList.index(QA_data_act)
        result = QA_entity[num]+'的'+QA_relation[num]+', '+data_3d[QA_entity[num]][QA_relation[num]]

    return result
