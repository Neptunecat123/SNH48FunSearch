from database.models import Member
from flask import Blueprint
import json

membertable = Blueprint('get_member_table_info', __name__)


def get_all_member_info():
    all_member = Member.query.all()
    return all_member


@membertable.route('', methods=["GET"])
def get_member_table_info():
    ret_list = []
    all_member = get_all_member_info()
    for item in all_member:
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
    return json.dumps(ret_list, ensure_ascii=False)
