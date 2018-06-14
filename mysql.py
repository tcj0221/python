try:
    import pymysql
    db = pymysql.connect("host","user","password","database")
    cursor = db.cursor()
    cursor.execute("show tables")
    table = cursor.fetchall()
    #print("tables is %s: " % table)
    print(table)
    db.close()
except Exception as e:
    f_log = open("mysql.log","a+",encoding="utf-8")
    f_log.writelines(repr(e)+"\n")
    f_log.flush()
    f_log.close()

