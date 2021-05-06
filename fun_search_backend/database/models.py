from sqlalchemy import Column, Integer, String, Text
from database.database import Base


class Best50(Base):
    __tablename__ = "best50"
    id = Column(Integer, primary_key=True, autoincrement=True)
    group = Column(String(50))
    rank = Column(Integer)
    unit = Column(String(500))
    unit_from = Column(String(500))
    number = Column(Integer)
    mem_1 = Column(String(20))
    mem_2 = Column(String(20))
    mem_3 = Column(String(20))
    mem_4 = Column(String(20))
    mem_5 = Column(String(20))
    mem_6 = Column(String(20))
    mem_7 = Column(String(20))
    mem_8 = Column(String(20))
    date = Column(String(20))
    # Best50(group, rank, unit, unit_from, number, members, date)
    def __init__(self, group, rank, unit, unit_from, number, members, date, time):
        self.group = group
        self.rank = rank
        self.unit = unit
        self.unit_from = unit_from
        self.number = number
        self.date = date
        self.mem_1


    def __repr__(self):
        return 'unit: %r; date: %r' % (self.unit, self.date)



class Election(Base):
    __tablename__ = "election"
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(String(50))
    member = Column(String(50))
    rank = Column(Integer)
    votes = Column(Integer)
    gname = Column(String(10))
    tname = Column(String(10))

    def __repr__(self):
        return 'name: %r' % self.member


class Member(Base):
    __tablename__ = "member"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    groupname = Column(String(50))
    teamname = Column(String(50))
    pinyin = Column(String(20))
    abbr = Column(String(10))
    nickname = Column(Text)
    height = Column(Integer)
    catchphrase = Column(Text)
    hometown = Column(String(100))
    birth = Column(String(100))
    age = Column(Integer)
    grade = Column(String(50))  # pname
    joinday = Column(String(50))
    graduateday = Column(String(50))
    status = Column(Integer)
    experience = Column(Text)
    blood_type = Column(String(50))
    ranking = Column(Integer)
    pocket_id = Column(String(100))

    def __init__(self, name, groupname, teamname, pinyin, abbr, nickname, height, catchphrase, hometown, birth, age,
                 grade, joinday, graduateday, status, experience, blood_type, ranking, pocket_id):
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
        self.blood_type = blood_type
        self.ranking = ranking
        self.pocket_id = pocket_id

    def __repr__(self):
        return 'name: %r' % self.name
