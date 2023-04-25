from flask import Flask, render_template, request, jsonify
#创建Flask对象app并初始化
app = Flask(__name__)

#通过python装饰器的方法定义路由地址
@app.route("/")
#定义方法 用jinjia2引擎来渲染页面，并返回一个index.html页面
def root():
    return render_template("index.html")
#定义app在8080端口运行
app.run(port=8080)