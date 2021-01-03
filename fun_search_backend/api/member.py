from database.models import Member
from database.database import db_session


def create_member(data):
    groupname = data.get("gname")
    name = data.get("sname")
    pinyin = data.get("pinyin")
    abbr = data.get("abbr")
    teamname = data.get("tname")
    grade = data.get("pname")
    nickname = data.get("nickname")
    joinday = data.get("join_day")
    height = data.get("height")
    birth = data.get("birth_day")
    hometown = data.get("birth_place")
    experience = data.get("experience")
    catchphrase = data.get("catch_phrase", "")
    blood_type = data.get("blood_type")
    status = data.get("status")
    ranking = data.get("ranking")
    pocket_id = data.get("pocket_id")
    age = data.get("age", 0)
    graduateday = data.get("graduateday", "9999-12-31")
    memberinfo = Member(name, groupname, teamname, pinyin, abbr, nickname, height, catchphrase, hometown, birth, age,
                        grade, joinday, graduateday, status, experience, blood_type, ranking, pocket_id)
    db_session.add(memberinfo)
    db_session.commit()