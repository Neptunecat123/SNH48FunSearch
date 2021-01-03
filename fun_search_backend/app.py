from flask import Flask
from database.database import init_db
import config
from tools.excel_to_database import get_datas, import_to_database

app = Flask(__name__)
app.config.from_object(config)

# 初始化db
# init_db()


if __name__ == "__main__":
    # 初始化写入人员信息excel数据
    # with app.app_context():
    #     datas = get_datas()
    #     import_to_database(datas)
    app.run()
