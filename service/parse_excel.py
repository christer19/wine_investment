import pandas as pd

def get_wines_set():
    df = pd.read_excel('../Investment Grade Wines .xlsx')
    wines_set = set()
    for i in range(len(df.columns)):
        for j in df.columns:
            if not pd.isnull(df[j][i]):
                wines_set.add(df[j][i])
    return wines_set
