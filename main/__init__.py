#################################
# __init__ 把當前目錄當作package 在其中做初始化動作
#################################
import logging
from logging.handlers import TimedRotatingFileHandler

from elasticsearch import Elasticsearch
from flask import Flask, jsonify
from werkzeug.utils import import_string

from .config import config

es = Elasticsearch("https://localhost:9200", basic_auth=("elastic", "helloworld"), verify_certs=False)


##########
# 工廠模式
# 初始化 Flask對象可以是package或檔案 __name__是系統變數，該變數指的是該py檔的名稱
##########
def create_app(config_name, blueprints):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    for i in blueprints:
        import_name = import_string(i)
        app.register_blueprint(import_name)

    formatter = logging.Formatter("%(asctime)s [%(filename)s:%(lineno)d][%(levelname)s] - %(message)s")
    handler = TimedRotatingFileHandler(
        "./log/event.log", when="D", interval=1, backupCount=15, encoding="UTF-8", delay=True, utc=True
    )
    app.logger.addHandler(handler)
    handler.setFormatter(formatter)

    @app.cli.command("init")
    @app.route("/init")
    def init():
        return jsonify({"Success": True})

    return app
