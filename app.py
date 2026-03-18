import pymssql

"""
使用 pymssql 對資料庫進行連接
"""
server = "fmpc"
database = "stocks1"
user = "Heart"
password = "1111"   
'''密碼洩漏問題'''




connect = pymssql.connect(server, user, password, database,tds_version=)
print("db登入成功")

