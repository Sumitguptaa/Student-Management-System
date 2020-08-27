import os

global liststd
liststd = ["Ravi","Priya","Amit","Piyush"]


def manage():
    x="#"  * 30
    y ="=" * 28

    #printing welcome message and options for this program
    print("""

 ----------------------------------------------------------------------------------------------
|==============================================================================================|
|==========================    Student Management System    ===================================|
|==============================================================================================|
 ----------------------------------------------------------------------------------------------

Enter 1 : To view Student's List
Enter 2 : To Add New Student
Enter 3 : To Search Student
Enter 4 : To Remove Student




        """)
    try:#using Exception For Validation

        uinput = int(input("Please Select An Above Option: "))
    except ValueError:
        exit("\n That is not a number")
                     
    else:
        print("\n")

    #checking using option

    if(uinput == 1):
                     print("List Student")
                     for i in liststd:
                         print("=> {}".format(i))
    elif(uinput == 2):
                     newstd = input("Enter New Student: ")
                     if(newstd in liststd):
                         print("\nThis student is Already in Database".format(newstd))
                     else:
                         liststd.append(newstd)
                         print("\n=> New Student Successfully Add\n".format(newstd))
                         for i in liststd:
                               print("=> {}".format(i))
    elif(uinput == 3):
                               sr = input("Enter Student Name To Search: ")
                               if(sr in liststd):
                                   print("\n=>  Record Found Of Student ()".format(sr))
                               else:
                                   print("\n=>  Record Not Found Of Student ()".format(sr))
    elif(uinput == 4):
                               rm = input("Enter Student Name To Remove: ")
                               if(rm in liststd):
                                   liststd.remove(rm)
                                   print("\n=>  Student Successfully Deleted\n".format(rm))
                                   for i in liststd:
                                       print("=> {}".format(i))
                               else:
                                   print("\n  No Record Found Of This Student\n".format(rm))
    elif(uinput <1 or uinput>4):
                               print("Please Enter Valid option")



manage()

def runagain():
                               run = input("\n Do you want to Run Again(y/n): ")
                               if(run.lower() == 'y'):
                                   manage()
                                   runagain()
runagain()

