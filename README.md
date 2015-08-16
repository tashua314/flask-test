# まずはじめに
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

# githubなどからcssやjsを追加する場合
## 自動の場合
```
$ bower install <name> --save
$ grunt bower:install
```
### バージョン指定する場合
```
# ex) 特定のバージョン
$ bower install jquery#1.9.1
# ex) 有るバージョンの最新
$ bower install jquery#1
$ grunt bower:install
```

## 手動の場合
1. bower.jsonに追記
1. `grunt bower:install` を実行


# 参考
* [Bower入門(基礎編)](http://yosuke-furukawa.hatenablog.com/entry/2013/06/01/173308)
* [Bower入門(応用編)](http://yosuke-furukawa.hatenablog.com/entry/2013/06/04/085537)
* [bowerでインストールしたファイルの配置を設定するにはgrunt-bower-taskが便利](http://kyohei8.hatenablog.com/entry/2013/11/17/145316)
