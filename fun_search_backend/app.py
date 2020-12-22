from flask import Flask
from database import db
import config

app = Flask(__name__)
app.config.from_object(config)


db.init_app(app)


if __name__ == "__main__":
    app.run()
