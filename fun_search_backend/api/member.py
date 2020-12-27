from database import db
from database.models import Member


def create_member(data):
    name = data.get("name")
    nickname = data.get("nickname")
    groupname = data.get("groupname")
    teamname = data.get("teamname")
    catchphrase = data.get("catchphrase")
    hometown = data.get("hometown")
    birth = data.get("birth")
    age = data.get("age")
    grade = data.get("grade")
    joinday = data.get("joinday")
    graduateday = data.get("graduateday", default="9999-12-31")
    status = data.get("status")
    pinyin = data.get("pinyin")
    abbr = data.get("abbr")
    height = data.get("height")
    experience = data.get("experience")
    memberinfo = Member(name, groupname, teamname, pinyin, abbr, nickname, height, catchphrase, hometown, birth, age, grade, joinday, graduateday, status, experience)
    db.session.add(memberinfo)
    db.session.commit()