from database import db
from database.models import Member


def create_member(data):
    name = data.get("name")
    nickname = data.get("nickname")
    catchphrase = data.get("catchphrase")
    catchphrase_his = data.get("catchphrase_his")
    hometown = data.get("hometown")
    birth = data.get("birth")
    age = data.get("age")
    grade = data.get("grade")
    joinday  = data.get("debugtime")
    graduateday = data.get("graduatetime")
    status = data.get("status")
    pinyin = data.get("pinyin")
    abbr = data.get("abbr")
    height = data.get("height")
    experience = data.get("experience")
    memberinfo = Member(name, pinyin, abbr, nickname, height, catchphrase, catchphrase_his, hometown, birth, age, grade, joinday, graduateday, status, experience)
    db.session.add(memberinfo)
    db.session.commit()