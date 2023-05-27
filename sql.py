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
    selectformula = "select * from 光錐資料表"
    deleteformula = "delete from 光錐資料表 where 光錐名稱 = '於夜色中'"

    mycursor = mydb.cursor()
    selectformula = "select * from 光錐資料表"
    sqlformula = "insert into 光錐資料表 (光錐名稱,故事,命途,攻擊力,生命力,防禦力,效果) \
                  values (%s,%s,%s,%s,%s,%s,%s)"
    new_data = [("於夜色中","省略","巡獵","123","456","789","省略"),
                ("拂曉之前","省略","智識","123","114","514","省略"),
                ("論劍","省略","巡獵","987","654","321","省略")]
    mycursor.executemany(sqlformula,new_data)
    mydb.commit()
    mycursor.execute(selectformula)
    myresult = mycursor.fetchall()
    for row in myresult:
        print(row)
    

except mysql.connector.Error as e:
    print("error")
    print(e)


"""     selectformula = "select * from 光錐資料表"
    deleteformula = "delete from 光錐資料表 where 光錐名稱 = '於夜色中'" 
        deleteformula = "delete from 光錐資料表 where 光錐名稱 = '於夜色中'" 
         mycursor.execute("delete from 角色 where 名字 = '虎克'")  
        mycursor.execute("select * from 角色")  """

