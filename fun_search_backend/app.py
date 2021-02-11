from flask import Flask
from database.database import init_db
import config
from tools.excel_to_database import get_datas, import_to_database
from api.to_frontend import membertable
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(config)
CORS(app, resources=r'/*')

# 初始化db
# init_db()

app.register_blueprint(membertable, url_prefix="/membertable")


if __name__ == "__main__":
    # 初始化写入人员信息excel数据
    # with app.app_context():
    #     datas = get_datas()
    #     import_to_database(datas)
    app.run()
