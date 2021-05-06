from database.models import Member, Best50
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


def create_b50(data):
    group = data.get("group", "")
    rank = data.get("rank")
    unit = data.get("unit")
    unit_from = data.get("unit_from")
    number = data.get("number")
    mem_1 = data.get("No1")
    mem_2 = data.get("No2")
    mem_3 = data.get("No3")
    mem_4 = data.get("No4")
    mem_5 = data.get("No5")
    mem_6 = data.get("No6")
    mem_7 = data.get("No7")
    mem_8 = data.get("No8")
    date = data.get("date")
    best50info = Best50(group, rank, unit, unit_from, number, members, date, time)
    db_session.add(best50info)
    db_session.commit()