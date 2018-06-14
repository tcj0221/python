def cretae_mysql(name):
    try:
        import pymysql
#        global db
        db = pymysql.connect("host","user","password","database")
        def create_tables(name):
            cursor = db.cursor()
            cursor.execute("create table %s(ID int)" %name)
            db.close()
        create_tables(name)

    except Exception as e:
        f_create_log = open("mysql_create.txt","a+",encoding='utf-8')
        f_create_log.writelines(repr(e)+"\n")
        f_create_log.flush()
    return
cretae_mysql("tcj2_test")