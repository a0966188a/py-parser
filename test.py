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



def Btn2_Click():
    cnn=ConnectSQL(dbName,userName,pwd)


    
    cursor = cnn.cursor()  # 開啟連線
    cursor.execute("SELECT @@VERSION;")
    cursor.close()  # 關閉連線
    print("成功-連線成功")

Btn2_Click()