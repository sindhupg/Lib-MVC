
import config as cf

def saveuser(userinfo):

    sql="insert into user(name,contno) values(%s,%s)"
    cf.mycursor.execute(sql,userinfo)
    
    val=cf.mycursor.rowcount
    cf.mydb.commit()

    return val


def savelibrarian(userinfo):

    sql="insert into librarian(name,contno) values(%s,%s)"
    cf.mycursor.execute(sql,userinfo)
    
    val=cf.mycursor.rowcount
    cf.mydb.commit()

    return val

def savebooks(userinfo):

    sql="insert into books(author,name,pub_comp) values(%s,%s,%s)"
    cf.mycursor.execute(sql,userinfo)
    
    val=cf.mycursor.rowcount
    cf.mydb.commit()

    return val


def savetrans(transinfo):

    sql="insert into trans(rented_date,rented_user,bookid) values(%s,%s,%s)"
    cf.mycursor.execute(sql,transinfo)
    
    val=cf.mycursor.rowcount
    cf.mydb.commit()

    return val


def delete( data,tablename):

    sql="delete from "+tablename+" where name='"+data+"'"
    cf.mycursor.execute(sql)
    
    val=cf.mycursor.rowcount
    cf.mydb.commit()

    return val

def getTableInfo( tablename):
    
    sql="select * from "+tablename+" order by id"
    cf.mycursor.execute(sql)
  
    result = cf.mycursor.fetchall()
    

    table=[]
    for row in result:
    
        table.append( list(row))

    return table

def getTransinfo( bookid):

    sql="select id,rented_date,rented_user,bookid,datediff(curdate(),rented_date) as days from trans where bookid="+bookid
    cf.mycursor.execute(sql)
  
    row = cf.mycursor.fetchone()

    if cf.mycursor.rowcount==1:
        result={
            "status":1,
            "id":row[0],
            "rd":row[1],
            "ru":row[2],
            "bid":row[3],
            "days":row[4]
        }
    else:
        result={

            "status":0
        }

    return result