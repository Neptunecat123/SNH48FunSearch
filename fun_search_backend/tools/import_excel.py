import pandas as pd
from sqlalchemy import create_engine

input_file = r"../ranking.xlsx"


def read_election_excel(file):
    ret_dict = {}
    df = pd.read_excel(file)
    ret_dict["date"] = ["2020-08-16"] * 48
    ret_dict["rank"] = range(1, 49)
    ret_dict["member"] = list(df.name)
    ret_dict["gname"] = list(df.gname)
    ret_dict["tname"] = list(df.tname)
    ret_dict["votes"] = list(df.votes)

    return ret_dict


def input_database(data, table):
    engine = create_engine("mysql+pymysql://root:SNH48group!@localhost:3306/snh48?charset=utf8")
    df_write = pd.DataFrame(data)
    df_write.to_sql(table, engine, index=False, if_exists='append')


if __name__ == "__main__":
    election_data = read_election_excel(input_file)
    input_database(election_data, "election_info")
