#Main Program

#Calling from a package
import Sub.asstProg

#Calling "displayMenuFun" function inside "asstProg" module
selectOP = Sub.asstProg.displayMenuFun()

#Selecting function based on the option
while selectOP!=8:

    #Calling "searchBookFun" function inside "asstProg" module
    if selectOP==1:
        print("\n****SEARCH BOOK****")
        Sub.asstProg.searchBookFun()

    #Calling "insertBookFun" function inside "asstProg" module    
    elif selectOP==2:
        print("\n****INSERT NEW BOOK****")
        Sub.asstProg.insertBookFun()

    #Calling "insertSubFun" function inside "asstProg" module    
    elif selectOP==3:
        print("\n****INSERT SUBJECTS****")
        Sub.asstProg.insertSubFun()

    #Calling "insertChaptFun" function inside "asstProg" module    
    elif selectOP==4:
        print("\n****INSERT BOOK CHAPTERS****")
        Sub.asstProg.insertChaptFun()

    #Calling "viewChaptFun" function inside "asstProg" module
    elif selectOP==5:
        print("\n****VIEW BOOK CHAPTERS****")
        Sub.asstProg.viewChaptFun()

    #Calling "searchBookFun" function inside "asstProg" module    
    elif selectOP==6:
        print("\n****UPDATE BOOK INFORMATION****")
        Sub.asstProg.updateBookFun()

    #Calling "deltBookFun" function inside "asstProg" module
    elif selectOP==7:
        print("\n****DELETE BOOK INFORMATION****")
        Sub.asstProg.deltBookFun()

    #Validating the user inputs
    else:
        print("\nPlease insert a valid number.\n\\\\Returning to the Menu...\\\\")

    #Returning to the menu
    selectOP = Sub.asstProg.displayMenuFun()

#Exit program
print("\nThank you for using our system.\n************Goodbye!************")

#End of the program
        
        

    
        
        
        
        
