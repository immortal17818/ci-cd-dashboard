import psycopg2
import pandas as pd

conn = psycopg2.connect(
   database="d1guna15qoe5e7", user='fshapqtsdayqbl', password='ecaa90102f14cd3d127fb75eeb69103bb937a6ef773e0bb0c8cf545b2157edc7', host='ec2-54-86-224-85.compute-1.amazonaws.com', port= '5432'
)

conn.autocommit = True

cursor = conn.cursor()
cursor.execute('''SELECT Id from graphdata''')

result = cursor.fetchone();
print(result)

conn.commit()
conn.close()

# cursor = conn.cursor()
# cursor.execute("DROP TABLE IF EXISTS graphdata")

# sql ='''CREATE TABLE graphdata(
#     ID int NOT NULL,
#     Date varchar(55),
#     MaxT varchar(25),
#     MinT varchar(25),
#     WindSpeed varchar(25),
#     Humidity varchar(25),
#     Precipitation varchar(25),
#     PRIMARY KEY (ID)
#     )'''

# cursor.execute(sql)
# print("Table created successfully........")
# conn.commit()
# conn.close()

# cursor.execute("INSERT INTO graphdata (Date, MaxT, MinT, WindSpeed, Humidity, Precipitation) VALUES ({},{},{},{},{},{})".format(str(df['Date'][i]),str(df['MaxT'][i]),str(df['MinT'][i]),str(df['WindSpeed'][i]),str(df['Humidity'][i]),str(df['Precipitation'][i])))
# conn.commit()
# print("Records inserted........")



# df = pd.read_csv("data/agriculture_data.csv")

# conn.autocommit = True
# cursor = conn.cursor()

# for i in range(len(df)):
#     postgres_insert_query = """ INSERT INTO graphdata (ID, Date, MaxT, MinT, WindSpeed, Humidity, Precipitation) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
#     record_to_insert = (str(i),str(df['Date'][i]),str(df['MaxT'][i]),str(df['MinT'][i]),str(df['WindSpeed'][i]),str(df['Humidity'][i]),str(df['Precipitation'][i]))
#     cursor.execute(postgres_insert_query, record_to_insert)
#     conn.commit()
#     print("Records inserted........")

# conn.close()
# print("Done")