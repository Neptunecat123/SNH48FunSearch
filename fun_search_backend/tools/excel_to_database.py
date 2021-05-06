import os
import pandas as pd
from api.member import create_member, create_b50

curr_path = os.path.dirname(os.path.abspath(__file__))


def member_get_datas():
    excel_file = os.path.join("config", "raw_data.xlsx")
    requery_item = [
        "gname",
        "sname",
        "pinyin",
        "abbr",
        "tname",
        "pname",
        "nickname",
        "join_day",
        "height",
        "birth_day",
        "birth_place",
        "blood_type",
        "status",
        "ranking",
        "pocket_id",
        "experience",
        "catch_phrase"
    ]
    ret = []
    df = pd.read_excel(excel_file, sheet_name=0)
    for _, row in df.iterrows():
        item_dict = {}
        for i in requery_item:
            item_dict[i] = row[i]
        ret.append(item_dict)

    return ret


def member_import_to_database(datas):
    for data in datas:
        create_member(data)


def election_get_datas():
    excel_file = os.path.join("config", "ranking.xlsx")


def election_import_to_database(datas):
    pass


def b50_get_datas(sheet_name, date):
    # 6th date = "20191221"
    # 7th date = "20210116"
    time = int(sheet_name[0])
    requery_item = [
        "rank",
        "unit",
        "unit_from",
        "number"
    ]
    print(curr_path)
    excel_file = os.path.join(curr_path, "..", "config", "Best50.xlsx")
    ret = []
    df = pd.read_excel(excel_file, sheet_name=sheet_name)
    for _, row in df.iterrows():
        members = ""
        if row["number"] != 16:
            for i in range(1, row["number"] + 1):
                No = "No" + str(i)
                members += row[No] + "+"
            members = members.strip("+")
        else:
            members += row["No1"]
        item_dict = {}
        for i in requery_item:
            item_dict[i] = row[i]
        item_dict["group"] = ""
        item_dict["date"] = date
        item_dict["members"] = members
        item_dict["time"] = time
        ret.append(item_dict)
    return ret


def b50_import_to_database(datas):
    for data in datas:
        create_b50(data)


if __name__ == "__main__":
    # members info
    datas = member_get_datas()
    member_import_to_database(datas)
    # election info
    #
    # b50 info

    datas = b50_get_datas("7th", "20210116")
    b50_import_to_database(datas)


