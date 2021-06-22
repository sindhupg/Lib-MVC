def displaymenu():

    menu="""
    1.Insertion
    2.Display
    3.Remove
    4.Book Transaction
    5.Exit
    Enter your choice : """
    print(menu)
    choice=input()

    return choice

def submenu():

    menu="""
    1.User
    2.Librarian
    3.Books
    Enter your choice : """
    print(menu)
    choice=input()

    return choice

def transmenu():

    menu="""
    1.Issue book
    2.Get book
    Enter your choice : """
    print(menu)
    choice=input()

    return choice

def getuserinfo():
    print("Enter name and contact no of users")
    name=input("Name : ")
    cont=input("Contno : ")
    users=(name,cont)
    return users

def getlibrarianinfo():
    print("Enter name and contact no of librarian")
    name=input("Name : ")
    cont=input("Contno : ")
    librn=(name,cont)
    return librn
   

def getbookinfo():
    print("Enter book details..")
    author=input("Author : ")
    name=input("Name : ")
    publisher=input("Publisher : ")
    
    books=(author,name,publisher)
    return books
def gettransInfo():
    rented_date=input("Rented date(yyyy-mm-dd) : ")
    rented_user=input("Rented user : ")
    bookid=input("Book ID : ")
    
    transinfo=(rented_date,rented_user,bookid)
    return transinfo
     
def getData( msg):

    print(msg)
    data=input()
    return data

def display(msg):
    print(msg)

def displayTable( table):

    for row in table:
        print(row)

def getBookid():

    print("")
    bookid=input("Enter Bookid : ")
    return bookid

def displayTrans(res):

    if res["status"]==0:
        print("")
        print("Book ID does not exist in Transactin table")
    else:
        
        print("")
        print("Transactin History")
        print("")

        print("Book id : ",res["bid"])
        print("Rented date : ",res["rd"])
        print("Rented user : ",res["ru"])
        print("Due days : ",res["days"])
        
        days=res["days"]

        if days<20:
            print("No fine amount")
        elif days>=20:

            baseamount=20
            totalamount=0

            incri=5
            while days>20:
                
                totalamount+=baseamount+incri
                incri+=5

                days-=5
            
            totalamount+=baseamount

            print("Fine Amount : ",totalamount)
