"""BootstrapのFlaskへの導入"""

from flask import Flask, render_template

# Flaskのインスタンスを生成
app = Flask(__name__)


# トップページのルーティング
@app.route("/")
def index():
    """トップページを表示する関数"""
    return render_template("index.html")

# About ページのルーティング
@app.route('/about')
def about():
    return render_template('about.html')

# 記事詳細（Sample Post）ページのルーティング
@app.route('/post')
def post():
    return render_template('post.html')

# お問い合わせ（Contact）ページのルーティング
@app.route('/contact')
def contact():
    return render_template('contact.html')
