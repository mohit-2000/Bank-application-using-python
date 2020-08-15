#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#installing libraries
def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)

install_and_import('string')
install_and_import('random')

#import libraries
import random
import string

#create new account class
class NewAccount(object):
    
    #defining all the variables of class NewAccount in init function
    def __init__(self):   
        self.fname = ""
        self.lname = ""
        self.acc = ""
        self.tobeshown = []
        self.__tobehidden = []
        self.__password = ""
        self.__pin = ""
        self.__minbal = 0
        self.__typeofaccount = ""
        self.__passpin = open('myfile.txt', 'a')
        self.__id = 0
        self.new=[]

     #to generate password and pin of new user & this function is also inherited in class ExistingUser & this function will be overrided by function of ExistingUser having same name
    def PassPinGenerator(self,a):
        self.__pin = random.randint(1000,9999)
        low = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        upp = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','S','T','U','V','W','X','Y','Z']
        num=[0,1,2,3,4,5,6,7,8,9]
        spe=['£','$','%','@','?','#']
        self.__password = ''.join([random.choice(low),random.choice(upp),str(random.choice(num)),random.choice(spe),random.choice(low),random.choice(upp),str(random.choice(num)),random.choice(spe)])

    #taking input from the user to create new account & storing the data in a file
    def CreateAccount(self):
        self.fname = input("Enter first Name : ")
        self.lname = input("Enter last Name : ")
        self.__typeofaccount = (input("Enter C for current account and D for deposit account : ")).upper()
        flag=1
        while(flag==1):
            try:
                
                self.__minbal = int(input("Minimum balance you would like to deposite(must be more than 1 euro and must be in integer) : "))
                if self.__minbal>=1:
                    flag=0
            except:
                print("the balance you enter must be in integer format and should not be 0")
        line=""
        with open('myfile.txt') as file:
            for line in (file.readlines() [-1:]): 
                pass
        if line=="":
            self.__id = '1'
            if self.__typeofaccount=="C":
                self.acc = "cur0001"
            elif self.__typeofaccount=="D":
                self.acc = "dep0001"
        else:
            idm = ""
            i=0
            while(line[i]!=" "):
                idm = idm + line[i]
                i=i+1
            self.__id=int(idm)+1
            print(self.__id)
            
                
            if self.__typeofaccount=="C":
                if self.__id>0 and self.__id<10:
                    self.acc = "cur000"+str(self.__id)            
                elif self.__id>9 and self.__id<100:
                    self.acc = "cur00"+str(self.__id)
                elif self.__id>99 and self.__id<1000:
                    self.acc = "cur0"+str(self.__id)
                elif self.__id>999:
                    self.acc = "cur"+str(self.__id)
                    
            elif self.__typeofaccount=="D":
                if self.__id>0 and self.__id<10:
                    self.acc = "dep000"+str(self.__id)            
                elif self.__id>9 and self.__id<100:
                    self.acc = "dep00"+str(self.__id)
                elif self.__id>99 and self.__id<1000:
                    self.acc = "dep0"+str(self.__id)
                elif self.__id>999:
                    self.acc = "dep"+str(self.__id)
        
       
    #  this function is used to display new user details.
    def displayandstore(self):        
        print("====== Your all Data is ==========")
        print("Name : ",self.fname," ",self.lname)
        if self.__typeofaccount=='C':
            self.__typeofaccount="Current"
            
        elif self.__typeofaccount=='D':
            self.__typeofaccount="Deposite"
        print("Account Type : ",self.__typeofaccount)
        print("Your PIN : ",self.__pin)
        print("Your Password : ",self.__password)
        print("Your Account number : ",self.acc)
        print("Total Balance : ",self.__minbal)
        print("=======================================================================")
        L = [str(self.__id)," ",self.acc," ",self.__typeofaccount," ",self.__password," ",self.fname," ",self.lname," ",str(self.__minbal)," ",str(self.__pin),"\n"]

        self.__passpin.writelines(L)
        self.__passpin.close()
    #this function will be inherited in class BankersStaff and providing necessary details.
    def Dataforbankers(self):
        self.__passpin = open("myfile.txt")
        string_list = (self.__passpin).readlines()
        self.__passpin.close()
        for i in range(0,len(string_list)):
            var=(string_list[i]).split(" ")
            storing=[var[4],var[5],var[1]]
            (self.tobeshown).append(storing)
            
    #this function is inherited in ExistingUser class & it is used to find a particular account in the file    
    def forexistinguser(self,acc_num):
        file1 = open('myfile.txt', 'r')
        Lines = file1.readlines()
        for line in Lines: 
            few = line.split(" ")
            var = few[len(few)-1]
            few = few[0:len(few)-1]
            few.append(var[0:len(var)-1])
            if(few[1]==acc_num):
                self.new = few
        
#-----------------------------------------------------------------------------------------------------------------------------
#it is inheriting the NewAccount class
#this class in inherited the NewAccount class for accessing the username and account number of all the users in the file
class BankersStaff(NewAccount):

    #this function initialize all the variables & functions of new account class and access them except variables such as pin & password,etc
    def __init__(self):
        NewAccount.__init__(self)

    #this function is used to print all the required data
    def bankers(self):
        print("PRIVATE MEMBERS OF NEWACCOUNT : ",self.fname)
        print("=====================================================")
        print("------------ Neccassary Deatils are ------------- ")
        print("Name","Account Number")
        for i in range(0,len(self.tobeshown)):
            print(self.tobeshown[i][0]+" "+self.tobeshown[i][1]," ",self.tobeshown[i][2])

#-----------------------------------------------------------------------------------------------------------------------------
#it is inheriting the NewAccount class
#this class is created for users whose data data is already stored in a file & user can access the data and change the data
class ExistingUser(NewAccount):

    
    #this function is used to initialize all the variables of ExistingUser class as well as NewAccount class because this class inherit the NewAccount class
    def __init__(self,acc_num):
        self.acc_num = acc_num
        NewAccount.__init__(self)
    
    #the function with the same name is present in NewAccount class since both functions taking same number of arguments 
    #as parameter & existing class inheriting the NewAccount class, function of ExistingUser class will override the function with same name 
    #inherited from the NewAccount class.This makes tha polymorphism in the code
    
    def PassPinGenerator(self,variable):
        print("Enter 1 if you want to change your PIN")
        print("Enter 2 if you want to change your password")
        print("Enter 3 if you want to check your Balance")
        choice = input("Enter your CHOICE : ")
        if choice=='1':
            variable[7] = random.randint(1000,9999)
        elif choice=='2':
            low = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
            upp = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','S','T','U','V','W','X','Y','Z']
            num=[0,1,2,3,4,5,6,7,8,9]
            spe=['£','$','%','@','?','#']
            variable[3] = ''.join([random.choice(low),random.choice(upp),str(random.choice(num)),random.choice(spe),random.choice(low),random.choice(upp),str(random.choice(num)),random.choice(spe)])
        elif choice=='3':
            print("Your Account Balance is : ",variable[6])
        my_file = open("myfile.txt")

        string_list = my_file.readlines()
        my_file.close()

        string_list[int(variable[0])-1] = str(variable[0])+" "+str(variable[1])+" "+str(variable[2])+" "+str(variable[3])+" "+str(variable[4])+" "+str(variable[5])+" "+str(variable[6])+" "+str(variable[7])+"\n"
        my_file = open("myfile.txt", "w")
        new_file_contents = "".join(string_list)

        my_file.write(new_file_contents)
        my_file.close()

        readable_file = open("myfile.txt")
        read_file = readable_file.read()
    
    #current password and pin is printed with the help of this function
    def credentials(self,myentries):
        print()
        print("Your Current PIN is : ",myentries[7])
        print()
        print("Your Current Password is : ",myentries[3])
        print()
                
            
#-----------------------------------------------------------------------------------------------------------------------------
        
flag='1'

#loop to execute the program 
while(flag=='1'):
    print("Enter 1 if you are new user")
    print("Enter 2 if you are Existing user")
    print("Enter 3 if you are banker staff")
    option = int(input("Enter your choice : "))
    
    #this if condition is execute when we want to create a new account
    if option==1:
        obj=NewAccount()
        obj.CreateAccount()
        obj.PassPinGenerator([])
        obj.displayandstore()
    
    #this if condition is execute when we need to make changes in the existing account
    elif option==2:
        attempt=1
        flag=1
        while(attempt<4 and flag==1):
            acc_num = input("Enter your Account number : ")
            obj2 = ExistingUser(acc_num)
            obj2.forexistinguser(acc_num)
            print("Attempt count: ",attempt)
            count=0
            c=[]
            try:
                for i in (obj2.new)[3]:
                    c.append(i)
                
                for i in range(0,2):
                    x=random.choice(c)
                    ind=c.index(x)
                    ind=ind+1
                    print("Enter the password character of location ",ind," : ",end="")
                    nmnm = input()
                    if x==nmnm:
                        count=count+1
                if count==2:
                    try:
                        if (acc_num==(obj2.new)[1]):
                            obj2.credentials(obj2.new)
                            flag=0
                    except:
                        print("You enter wrong account no./password")
                    attempt=attempt+1
                else:
                    print("Your have entered wrong password value")
            except:
                print("Account You would like to find Does not exist ")
        if flag==0:
            obj2.PassPinGenerator((obj2.new))
        else:
            print("You can not change any thing since you lost your all ",attempt-1," attempts")
    #this if condition will execute when staff of bank wants to access the username and account number
    elif option==3:
        obj3 = BankersStaff()
        obj3.Dataforbankers()
        obj3.bankers()
    #if user choice selection is wrong then else block will be executed
    else:
        print("WRONG SELECTION")
        
    #if user enter 1 then the program will continue or it will be terminated
    flag = input("Enter 1 for continue or anything else to exit : ")

