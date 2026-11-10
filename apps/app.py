"""BootstrapのFlaskへの導入"""

from flask import Flask, render_template

# Flaskのインスタンスを生成
app = Flask(__name__)


# トップページのルーティング
@app.route("/")
def index():
    """トップページを表示する関数"""
    return render_template("index.html")
