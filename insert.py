import pymssql
import random
import time



import pyodbc

dbName = "stocks1"
userName = "Heart"
pwd = "1111"  

def ConnectSQL(dbName,userName,pwd):
    srv = "localhost"
    sqlConn = ("DRIVER={ODBC Driver 17 for SQL Server};SERVER=" +
               srv + ";DATABASE=" + dbName + ";UID=" + userName + ";PWD=" + pwd)
    try:
        coxn = pyodbc.connect(sqlConn)
        return coxn
    except Exception as e:
        print("失敗", str(e))



TSQL="INSERT INTO stocks(sid,sname,price)VALUES(?,?,?)"
try:
    connect=ConnectSQL(dbName,userName,pwd)
    # connect = pymssql.connect(server, user, password, database)
    cursor = connect.cursor()
    

    
    
       


    for i in range(1,30):
        # 產生亂數 介於( 1850~ 1905)
        rp = random.randint(1850,1905)
        cursor.execute(TSQL, ("2330","TSMC",rp))


        # pymssql 預設設定 autocommit = false
        cursor.commit()
        print(f'第{i}次擷取,金額 {rp}')
        if( i < 30 ):  
            time.sleep(3)   # 如果還在回圈內就 休眠 5秒



    print("資料寫入完畢")

    
    cursor.close()
    connect.close()




except Exception as e: 
    print(f'連線失敗: 原因{e}')