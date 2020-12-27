import pandas as pd
from api.member import create_member

excel_file = "raw_data.xlsx"

def get_datas():
    ret = []
    df = pd.read_excel(excel_file)
    print(df['sname'].values)

def import_to_database(datas):
    for data in datas:
        create_member(data)
