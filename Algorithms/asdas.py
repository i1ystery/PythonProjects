import pandas as pd
data = pd.read_csv("https://raw.githubusercontent.com/mlcollege/ai-academy/main/05-Zaklady-datove-analyzy/data/nehody_cyklistu.csv", sep=';')
data.head()
data['datum'] = pd.to_datetime(data['datum'])
print(data['datum'].dtype)
data['dvt'] = data['datum'].dt.weekday
weekDay = {0:'pondeli', 1:'utery', 2:'streda', 3:'ctvrtek', 4:'patek', 5:'sobota', 6:'nedele'}
data['dvt'] = data['dvt'].map(weekDay)
data['mesic'] = data['datum'].dt.month
data['dvt'].value_counts().plot.bar()
print("Počty nehod pro jednotlivé dny v týdnu.")