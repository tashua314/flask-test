#!/bin/env python
# coding: utf-8

import os
from flask import Flask, render_template, request, redirect, url_for
import numpy as np

app = Flask(__name__)
app.debug = True


# メッセージをランダムに表示するメソッド
def picked_up():
    messages = [
        u'こんにちは、あなたの名前を入力してください',
        u'やあ！お名前は何ですか？',
        u'あなたの名前を教えてね'
    ]
    # NumPy の random.choice で配列からランダムに取り出し
    return np.random.choice(messages)


@app.route('/')
def index():
    title = u'ようこそ'
    message = picked_up()
    print message
    # index.html をレンダリングする
    return render_template('index.html',
                           message=message, title=title)


# /post にアクセスしたときの処理
@app.route('/post', methods=['GET', 'POST'])
def post():
    title = u'こんにちは'
    if request.method == 'POST':
        # リクエストフォームから「名前」を取得して
        name = request.form['name']
        # index.html をレンダリングする
        return render_template('index.html',
                               name=name, title=title)
    else:
        # エラーなどでリダイレクトしたい場合はこんな感じで
        return redirect(url_for('index'))


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=''):
    if name == '':
        name = u'ななしさん'
    return render_template('hello.html', name=name)


@app.route('/debug')
def debug():
    return render_template('notemplate.html')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(port=port)
