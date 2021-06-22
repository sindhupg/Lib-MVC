
import sys

from mysql.connector.errors import IntegrityError
import view
import model

def startTransaction():

    view.display("")
    view.display("")
    view.display("*******Welcome to Library Management********")
    
    ch=view.displaymenu()
    #print(f"Selected option is {choice}")
    
    if ch=="1":

        choice=view.submenu()  
        
        if choice=="1":
            userinfo=view.getuserinfo()
            result=model.saveuser(userinfo)

            print(f"Returned result ={result}")
            if result==1:
                print("User saved successfully !!!")
            else:
                print("Sorry could not save")

        elif choice=="2":
            librinfo=view.getlibrarianinfo()
            result=model.savelibrarian(librinfo)

            print(f"Returned result ={result}")
            if result==1:
                print("Librarian saved successfully !!!")
            else:
                print("Sorry could not save")
        else:
            bookinfo=view.getbookinfo()
            result=model.savebooks(bookinfo)
            print(f"Returned result ={result}")
            if result==1:
                print("Books saved successfully !!!")
            else:
                print("Sorry could not save")

    elif ch=="2":

        choice=view.submenu()

        if choice=="1":
            userinfo=model.getTableInfo("user")
            view.display("")
            view.display("Users table content")
            head=["ID","Name","Contact no"]
            view.display("-----------------------------------------------")
            view.display(head)
            view.display("-----------------------------------------------")
            view.displayTable(userinfo)
            view.display("-----------------------------------------------")
            
        elif choice=="2":
            librinfo=model.getTableInfo("librarian")
            view.display("")
            view.display("Librarian table content")
            head=["ID","Name","Contact no"]
            view.display("-----------------------------------------------")
            view.display(head)
            view.display("-----------------------------------------------")
            view.displayTable(librinfo)
            view.display("-----------------------------------------------")
            
        elif choice=="3":
            booksinfo=model.getTableInfo("books")
            view.display("")
            view.display("Books table content")
            head=["ID","Author","Name","Publisher"]
            view.display("-----------------------------------------------")
            view.display(head)
            view.display("-----------------------------------------------")
            view.displayTable(booksinfo)
            view.display("-----------------------------------------------")
            



    elif ch=="3":

        choice=view.submenu()  
        print(choice)

        if choice=="1":
            user=view.getData("Enter user name : ")
            result=model.delete(user,"user")

            if result==1:
                view.display("Deleted")
            else:
                view.display("Could not delete")
        
        elif choice=="2":

            libr=view.getData("Enter lirarian name : ")
            result=model.delete(libr,"librarian")
            if result==1:
                view.display("Deleted")
            else:
                view.display("Could not delete")
        
        else:

            book=view.getData("Enter book name : ")
            result=model.delete(book,"books")
            if result==1:
                view.display("Deleted")
            else:
                view.display("Could not delete")

    elif ch=="4":
    
        choice=view.transmenu()  
        print(choice)

        if choice=="1":
            
            try:

                
                view.display("****Book Issue Form****")
                transinfo=view.gettransInfo()
                result=model.savetrans(transinfo)
                #print(f"Returned result ={result}")
                if result==1:
                    print("Transaction saved successfully !!!")
                else:
                    print("Sorry could not save Transaction")

            except IntegrityError:
                print("-------- Invalid Book ID is Given --------")
        else:
            
            bookid=view.getBookid()
            result=model.getTransinfo(bookid)

            view.displayTrans(result)
           

    elif ch=="5":
        pass

    return ch
    
        
        



if __name__=="__main__":
    
    while True:
        ch=startTransaction()
    
        if ch=="5":
            sys.exit(0)








