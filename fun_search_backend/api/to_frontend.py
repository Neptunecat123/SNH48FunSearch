from database.models import Member, Election
from flask import Blueprint
from flask import request
import json

membertable = Blueprint('get_member_table_info', __name__)
electiontable = Blueprint('get_election_info', __name__)


@electiontable.route('', methods=["GET"])
def get_election_info():
    session = str(request.args.get("session", 7, type=int))
    ret_list, ret_dict = [], {}
    session_dict = {"7": "2020-08-16",}
    election_info = Election.query.filter_by(date=session_dict[session]).all()
    for item in election_info:
        ret_dict["rank"] = item.rank
        ret_dict["name"] = item.name
        ret_dict["gname"] = item.gname
        ret_dict["tname"] = item.tname
        ret_dict["votes"] = item.votes
        ret_list.append(ret_dict)
    return json.dumps(ret_list, ensure_ascii=False)



def get_all_member_info(page, per_page):
    all_member = Member.query.all()
    total_page = len(all_member) // per_page + 1
    start = (page - 1) * per_page
    end = start + per_page
    return all_member[start: end], total_page


@membertable.route('', methods=["GET"])
def get_member_table_info():
    page = request.args.get("page", 1, type=int)
    per_page = 15
    ret_list = []
    ret_dict = {}
    members, total_page = get_all_member_info(page, per_page)
    print("total_page = {}".format(total_page))
    for item in members:
        item_dict = {}
        item_dict["gname"] = item.groupname
        item_dict["name"] = item.name
        item_dict["tname"] = item.teamname
        item_dict["pname"] = item.grade
        item_dict["join_day"] = item.joinday
        item_dict["birth_day"] = item.birth
        item_dict["birth_place"] = item.hometown
        item_dict["ranking"] = item.ranking
        item_dict["status"] = item.status
        item_dict["catch_phrase"] = item.catchphrase
        ret_list.append(item_dict)
    ret_dict["data"] = ret_list
    ret_dict["total_page"] = int(total_page)
    return json.dumps(ret_dict, ensure_ascii=False)
