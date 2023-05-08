import mysql.connector 

try:
    mydb = mysql.connector.connect(
        host="localhost",
        port="3306",
        user="root",
        password="justforyou1104",
        database="testdb",
        charset="utf8"
        )
    mycursor = mydb.cursor()
    sqlformula = "insert into 角色 (名字,稀有度,命途) values (%s,%s,%s)"
    character = [("三月七","四星","存護"),
                 ("丹恆","四星","巡獵"),
                 ("停雲","四星","同偕"),
                 ("娜塔莎","四星","豐饒"),
                 ("虎克","四星","毀滅")]
    mycursor.execute("select * from 角色")
    myresult = mycursor.fetchall()
    for row in myresult:
        print(row)
        
    mydb.commit()
except mysql.connector.Error as e:
    print("error")
    print(e)






