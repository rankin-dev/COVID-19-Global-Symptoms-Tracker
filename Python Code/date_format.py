import pandas as pd

df = pd.read_csv("combined_americas.csv",encoding="latin")
df['survey_date'] = df['survey_date'].astype('object')
for i in df.index:
    date = df.at[i, "survey_date"]
    res = list(str(date)) 
    res.insert(4, "/") 
    res.insert(7, "/") 
    res = ''.join(res) 
    df.at[i, "survey_date"] = str(res)
df.to_csv('covid_americas_dates.csv', index = False)
