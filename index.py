'''
@Author: your name
@Date: 2020-03-03 11:17:40
@LastEditTime: 2020-03-04 17:44:44
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \KGQA-welderdefine\index.py
'''
from flask import Flask, render_template, jsonify, make_response, request
from tokensim import get_similar
import jieba

app = Flask(__name__)


@app.route("/say", methods=['GET', 'POST'])
def Hello():
    message=''
    get_data = request.args.to_dict()
    message=get_similar(get_data['data'])
    response = make_response(jsonify(message))    
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return response


@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
