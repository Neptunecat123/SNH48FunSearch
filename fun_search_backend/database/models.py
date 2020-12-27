from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)


class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    groupname = db.Column(db.String(50))
    teamname = db.Column(db.String(50))
    pinyin = db.Column(db.String(20))
    abbr = db.Column(db.String(10))
    nickname = db.Column(db.Text)
    height = db.Column(db.Integer)
    catchphrase = db.Column(db.Text)
    hometown = db.Column(db.String(100))
    birth = db.Column(db.String(100))
    age = db.Column(db.Integer)
    grade = db.Column(db.String(50))  # pname
    joinday = db.Column(db.String(50))
    graduateday = db.Column(db.String(50))
    status = db.Column(db.Integer)
    experience = db.Column(db.Text)
    __tablename__ = "Member_info"

    def __init__(self, name, groupname, teamname, pinyin, abbr, nickname, height, catchphrase, hometown, birth, age, grade, joinday, graduateday, status, experience):
        self.name = name
        self.groupname = groupname
        self.teamname = teamname
        self.pinyin = pinyin
        self.abbr = abbr
        self.nickname = nickname
        self.height = height
        self.catchphrase = catchphrase
        self.hometown = hometown
        self.birth = birth
        self.age = age
        self.grade = grade
        self.joinday = joinday
        self.graduateday = graduateday
        self.status = status
        self.experience = experience

    def __repr__(self):
        return 'name: %r' % self.name


if __name__ == "__main__":
    db.create_all()
