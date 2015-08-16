# 環境構築
## まずはじめに
```
$ brew install node.js
$ brew install pip
$ sudo pip install virtualenv
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
$ npm install bower -g
$ npm install -g grunt-cli
$ npm install grunt --save-dev
$ npm install grunt-bower-task --save-dev // grunt-bower-task のインストール
$ grunt bower:install
```

## githubなどからcssやjsを追加する場合
### 自動の場合
```
$ bower install <name> --save
$ grunt bower:install
```
#### バージョン指定する場合
```
# ex) 特定のバージョン
$ bower install jquery#1.9.1
# ex) 有るバージョンの最新
$ bower install jquery#1
$ grunt bower:install
```

### 手動の場合
1. bower.jsonに追記
1. `grunt bower:install` を実行


## 参考
* [Bower入門(基礎編)](http://yosuke-furukawa.hatenablog.com/entry/2013/06/01/173308)
* [Bower入門(応用編)](http://yosuke-furukawa.hatenablog.com/entry/2013/06/04/085537)
* [bowerでインストールしたファイルの配置を設定するにはgrunt-bower-taskが便利](http://kyohei8.hatenablog.com/entry/2013/11/17/145316)


# 開発
## まずはじめに
```
$ source env/bin/activate // Pythonの実行環境を仮想環境で準備
```

## ローカルでの動作確認
```
$ python hello.py
```

## 参考
* [続いてはPython（Flask）でHeroku!](http://qiita.com/kounoike/items/6fc31fe051e5d688f136)
* [Flask - クイックスタート](https://flask-docs-ja.readthedocs.org/en/latest/quickstart/#id6)
* [ウェブアプリケーションフレームワーク Flask を使ってみる](http://qiita.com/ynakayama/items/2cc0b1d3cf1a2da612e4)
* [VIRTUALENV について](http://blog1.erp2py.com/2011/07/virtualenv.html)
