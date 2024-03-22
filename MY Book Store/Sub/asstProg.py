#Assistant Program

#-----------Display menu function--------------------
def displayMenuFun():
    print("\nABC BOOKS STORE\n\n*****MENU*****\n\n1-Search Book\n2-Insert New Book\n3-Insert Subjects\n4-Insert Book Chapters\n5-View Book Chapters\n6-Update Book Information\n7-Delete book information\n8-Exit")

    #Select the option from the menu
    selectOP=int(input("\nPlease enter the number of your selected option : "))
        
    return (selectOP)
    

#------------Search book function---------------------
def searchBookFun():
    print("\nSearch available books from below...")

    import mysql.connector

    #Open database connection with a dictionary
    conDict= {'host':'localhost',
          'database':'abc_books_store',
          'user':'root',
          'password':''}

    db=mysql.connector.connect(**conDict)

    #Prepare a cursor object using cursor() method
    cursor=db.cursor()

    #Creating variables
    contOption="Y"

    #Repeat the search query based on user input Y/N    
    while contOption=='Y' or contOption=='y':
        #Read the user input
        searchWord=input("Please enter the book number(Only Numeric)/book title/author of the book/book publisher you are searching for : ")
        
        #Execute SQL query using cursor method
        searchtxt="SELECT * FROM books WHERE bookNo = '" + searchWord + "' OR title = '" + searchWord + "' OR author = '" + searchWord + "' OR publisher = '" +  searchWord + "'"
        cursor.execute(searchtxt)

        #Fetch results using fetchall() method
        data = cursor.fetchall()

        #Validate searched query results
        if data:
            #Display searched query results
            for item in data:
                print("\nBook No:",item[0])
                print("Title :",item[1])
                print("Subject Code :",item[2])
                print("Author :",item[3])
                print("Publisher :",item[4])
                print("Price :",item[5])
                print("Location :",item[6])
                print("Edition :",item[7])    
        else:
            print("\nYour searched item is not available.")

        contOption=input("Do you want to continue? (Y/N)")
        
    #Disconnect from server
    db.close()
    return
    
#--------------Insert Book Function------------------------    
def insertBookFun():
    print("\nEnter new book information from below...")
    
    import mysql.connector

    #Open database connection with a dictionary
    conDict= {'host':'localhost',
          'database':'abc_books_store',
          'user':'root',
          'password':''}

    db= mysql.connector.connect(**conDict)

    #Prepare a cursor object using cursor() method
    cursor=db.cursor()

    #Create variables
    contOption="Y"
    
    #Repeat the search query based on user input Y/N   
    while contOption=='Y' or contOption=='y':
        #Read User Input
        uBookNo=int(input("Type Book Number(Only numeric) :"))
        uTitle=input("Type Book Title :")
        uSubCode=input("Type Subject Code :")
        uAuthor=input("Type Author Name :")
        uPublisher=input("Type Publisher Name :")
        uPrice=input("Enter Book Price(Only numeric) :")
        uLocation=input("Type Book Location :")
        uEdition=input("Type Book Edition(Only numeric) :")
        uChaptCount=input("Type How Many Chapters Are There(Only numeric) :")

        #Execute SQL query using execute() method
        newBookText="INSERT INTO books (bookNo,title,subjectCode,author,publisher,price,location,edition,chapters_count) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        bookValues=(uBookNo,uTitle,uSubCode,uAuthor,uPublisher,uPrice,uLocation,uEdition,uChaptCount)
        cursor.execute(newBookText, bookValues)
        
        #Commit the change
        db.commit()

        #Display how many records added
        print("\n",cursor.rowcount,"Record Added")

        contOption=input("Do you want to continue? (Y/N)")

    #Disconnect from server
    db.close()
    return

#--------------Insert Subject Function------------------------

def insertSubFun():
    print("\nEnter new subject information from below...")
    
    import mysql.connector

    #Open database connection with a dictionary
    conDict= {'host':'localhost',
          'database':'abc_books_store',
          'user':'root',
          'password':''}

    db= mysql.connector.connect(**conDict)

    #Prepare a cursor object using cursor() method
    cursor=db.cursor()

    #Create variables
    contOption="Y"
    f=0

    #Repeat the search query based on user input Y/N
    while contOption=="Y" or contOption=="y":
        #Read User Input
        uSubCode=input("Type Subject Code (Maximum 5 characters.) :")
        uSubName=input("Type Subject Name :")
    

        #Execute SQL query using execute() method
        subTxt="INSERT INTO subject (subject_code,name) VALUES(%s,%s)"
        subValues=(uSubCode,uSubName)
        cursor.execute(subTxt, subValues)

        #Commit the change
        db.commit()

        #Display how many records added
        print("\n",cursor.rowcount,"Record Added")

        contOption=input("Do you want to continue? (Y/N)")

    #Disconnect from server
    db.close()
    return


#------------Insert Book Chapters Function-------------------
def insertChaptFun():
    print("\nEnter new chapter information from below...")
    
    import mysql.connector

    #Open database connection with a dictionary
    conDict= {'host':'localhost',
          'database':'abc_books_store',
          'user':'root',
          'password':''}

    db= mysql.connector.connect(**conDict)

    #Prepare a cursor object using cursor() method
    cursor=db.cursor()

    #Read User Input
    uBookNo=input("Type Book No(Only Numeric) :")

    #Create Variable
    contOption="Y"
    f=0

    #Repeat the search query based on user input Y/N
    while contOption=="Y" or contOption=="y":

        #Read other inputs
        uChaptNo=input("Type Chapter Number(Only Numeric) :")
        uChaptTitle=input("Type Chapter Title :")
        uStartPg=input("Type starting page number of the chapter(Only Numeric) :")
        uEndPg=input("Type ending page number of the chapter(Only Numeric) :")

        #Enter chapters
        chapters=input("Please enter the chapter as a text here :")
        with open(uBookNo + "_" + uChaptNo + ".txt","w")as f:
            f.write(chapters)
            f.close() 
        
        #Execute SQL query using execute() method
        chaptTxt="INSERT INTO book_chapter (bookNo,chapterNo,chapter_title,starting_page_No,ending_page_No) VALUES(%s,%s,%s,%s,%s)"
        chaptValues=(uBookNo,uChaptNo,uChaptTitle,uStartPg,uEndPg)
        cursor.execute(chaptTxt, chaptValues)

        #Commit the change
        db.commit()

        #Display how many records added
        print("\n",cursor.rowcount,"Record Added")

        contOption=input("Do you want to continue? (Y/N)")
    
    #Disconnect from server
    db.close()
    return

#--------------View Book Chapters Function-------------------
def viewChaptFun():
    print("\nSelect a book from below to view its chapters...")
    
    import mysql.connector

    #Open database connection with a dictionary
    conDict= {'host':'localhost',
          'database':'abc_books_store',
          'user':'root',
          'password':''}

    db=mysql.connector.connect(**conDict)

    #Prepare a cursor object using cursor() method
    cursor=db.cursor()

    #Execute SQL query using cursor method
    cursor.execute("SELECT bookNo, title, chapters_count FROM books")

    #Fetch results using fetchall() method
    data = cursor.fetchall()

    #Display query results
    for item in data:
        print("\nBook No:",item[0])
        print("Book Title:",item[1])
        print("Available Chapters Count :",item[2])  
        
    #Disconnect from server
    db.close()
    
    #Create Variables
    contOption='Y'
    f=0

    #Repeat the search query based on user input Y/N
    while contOption=='Y' or contOption=='y':
        #Read user inputs
        ubookNo=input("\nEnter the Book Number(Only Numeric) :")
        uChaptNo=input("Enter the Chapter Number :")
        f=open(ubookNo + "_" + uChaptNo + ".txt","r")
        print("\n" + f.read())

        contOption=input("Do you want to continue? (Y/N)")
    
    return
    
#-------------Update book function--------------------------
def updateBookFun():
    print("\nUpdate book information from below...")

    import mysql.connector

    #Open database connection with a dictionary
    conDict= {'host':'localhost',
              'database':'abc_books_store',
              'user':'root',
              'password':''}

    db= mysql.connector.connect(**conDict)

    #Prepare a cursor object using cursor() method
    cursor=db.cursor()

    #Create Variables
    contOption="Y"

    #Repeat the search query based on user input Y/N
    while contOption=="Y" or contOption=="y":
        #Get user inputs on updates
        uBookNo=input("Enter the Book Number(Only Numeric) :")
        columnName=input("Enter what needs to be changed(bookNo/title/subjectCode/author/publisher/price/location/edition/chapters_count) :")
        newValue=input("Enter new value/Text :")
        

        #Execute SQL query using execute() method
        updValue= " UPDATE books SET " + columnName + "= '" + newValue + "' WHERE bookNo =" + uBookNo
        cursor.execute(updValue)

        #Commit the change
        db.commit()

        #Validate update query results
        if cursor.rowcount==0:
            print("\nYour data cannot be updated. Please check and insert the correct Book Number.")
        else:
            #Display how many records added
            print("\n",cursor.rowcount,"Record Updated")
            
        contOption=input("Do you want to continue? (Y/N)")

    #Disconnect from server
    db.close()
    return
    
#-----------------Delete book function--------------------------------
def deltBookFun():
    print("\nDelete unnecessary records from below...")
    
    import mysql.connector

    #Open database connection with a dictionary
    conDict= {'host':'localhost',
          'database':'abc_books_store',
          'user':'root',
          'password':''}

    db= mysql.connector.connect(**conDict)

    #Prepare a cursor object using cursor() method
    cursor=db.cursor()

    #Create Variables
    contOption="Y"

    #Repeat the search query based on user input Y/N
    while contOption=="Y" or contOption=="y":
        #Get user input on deleting information
        uBookNo=input("Enter the Book Number(Only Numeric) :")

        #Execute SQL query using execute() method
        cursor.execute("DELETE FROM books WHERE bookNo =" + uBookNo + "")
        cursor.execute("DELETE FROM book_chapter WHERE bookNo =" + uBookNo + "")

        #Commit the change
        db.commit()

        #Validate update query results
        if cursor.rowcount==0:
            print("\nYour data cannot be deleted. Please check and insert the correct Book Number.")
        else:
            #Display how many records deleted
            print("\n",cursor.rowcount,"Record Deleted")
            
        contOption=input("Do you want to continue? (Y/N)")

    #Disconnect from server
    db.close()
    return

    
    
    
    

    
    
