from flask import Flask
import config
from api.to_frontend import membertable, electiontable, b50table
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(config)
CORS(app, resources=r'/*')

app.register_blueprint(membertable, url_prefix="/membertable")
app.register_blueprint(electiontable, url_prefix="/electiontable")
app.register_blueprint(b50table, url_prefix="/b50table")


if __name__ == "__main__":
    app.run()
