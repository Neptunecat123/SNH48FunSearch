import pandas as pd
from api.member import create_member

excel_file = "raw_data.xlsx"
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


def get_datas():
    ret = []
    df = pd.read_excel(excel_file)
    for _, row in df.iterrows():
        item_dict = {}
        for i in requery_item:
            item_dict[i] = row[i]
        ret.append(item_dict)

    return ret


def import_to_database(datas):
    for data in datas:
        create_member(data)


if __name__ == "__main__":
    datas = get_datas()
    import_to_database(datas)
