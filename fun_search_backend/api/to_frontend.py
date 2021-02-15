from database.models import Member
from flask import Blueprint
from flask import request
import json

membertable = Blueprint('get_member_table_info', __name__)


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
    ret_json = {}
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
    ret_json["data"] = ret_list
    ret_json["total_page"] = total_page
    print((ret_json))
    return json.dumps(ret_json, ensure_ascii=False)
