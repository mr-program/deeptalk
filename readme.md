# Deeptalk专业问答系统

项目地址:https://github.com/mr-program/deeptalk.git

Deeptalk是Deepthink平台开源的一款专业问答系统.系统使用简单.适合小型的问答应用开发.

操作步骤:

1.准备问答数据,例如,定义.txt;数据的第一行是关系描述,第二行是头实体,第三行是尾实体,后面以此类推.

2.准备好数据后,dataset.py,生成问答数据和词典,同时生成json三元组

3.运行index.py,通过访问http://127.0.0.1:5000即可访问数据,进行问答交互了.