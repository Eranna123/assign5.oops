# 1.SQUARE NUMBERS AND RETURN THEIR SUM-------------------------------------------


class points:
    def __init__(self,x,y,z):
       self.x = x
       self.y = y
       self.z = z
    def square_sum(self):   
        a = self.x **2
        b = self.y **2
        c = self.z **2
        result= a + b + c 
        print("Resulted squaresum of x,y & z is :",result)

x=int(input("Enter value of x:"))     
y=int(input("Enter value of y:"))    
z=int(input("Enter value of z:"))    
object1= points(x,y,z)
object1.square_sum()



# 2.IMPLEMENT THE CALCULATOR CLASS--------------------------------------------

class calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        return num1+num2
    def subtract(self):
        return num2-num1
    def multiply(self):
        return  num1*num2
    def divide(self):
        return num2/num1   
num1 = int(input("Enter num1:"))             
num2 = int(input("Enter num2:"))  
obj = calculator(num1,num2)
print("Addition of num1 & num2:",obj.add())
print("Subtraction of num1 & num2:",obj.subtract())
print("Multiplication  of num1 & num2:",obj.multiply())
print("Division of num1 & num12:",obj.divide())

 


# #  3.  IMPLEMENT THE COMPLETE STUDENT CLASS--------------------------------------


class student:
   
    def stu_detail(self,name,rollnum):
        self.__name=name
        self.__rollnum=rollnum
        print('student details: name , age = ',self.__name , self.__rollnum)
    def setname(self,new_name): 
        self.__name = new_name         
    def setrollnum(self,new_rollnum):
        self.__rollnum =new_rollnum
    def getname(self):
        return self.__name
    def getrollnum(self):
        return self.__rollnum  
     
c = student()
name=input("Enter student name:")
rollnum=int(input('Enter rollum:'))
c.stu_detail(name,rollnum)
print ("student name:",c.getname())
print("student rollnum:",c.getrollnum())
c.setname(input("Enter New student name:"))
c.setrollnum(input('Enter New student rollnum:'))
print("New student name:",c.getname())
print("New student rollnum:",c.getrollnum()) 




# 4.  IMPLEMENT A BANKING ACCOUNT----------------------------------------------------------

class account:
    def __init__(self,title,balance):
        self.title=title
        self.balance=balance
    def my_account(self):
        print("account details:,",self.title,self.balance)    
class savingsaccount(account): 
    def __init__(self,title,balance,interest_rate):
        super().__init__(title,balance)
        self.interest_rate=interest_rate

    def my_newone(self):
        print("Account  details:",self.title,'have bank balance of Rs',self.balance,' and the rate of interest is=',self.interest_rate)    


title = input("Enter your name:")
balance = int(input('Enter bank balance:'))        
interest_rate = int(input('Enter interestrate:'))
account1= savingsaccount(title,balance,interest_rate)
account1.my_newone()



# 5. HANDLING A BANK ACCOUNT-------------------------------------------------------------


class account:
    def __init__(self,balance):
        self.balance = balance
    def getbalance(self):
        return self.balance
    def deposit(self,amount):
        self.balance += amount
    def withdrawal(self,amount):
        self.balance -= amount

class savingsaccount(account):
    def __init__(self,balance,interest_rate):
        super().__init__(balance)
        self.interest_rate = interest_rate
    def interestAmount(self):
        return self.balance * (self.interest_rate/100)
balance = int(input('enter balance:'))
deposit = int(input('enter deposit:'))
balance_2 = int(input('enter new balace:'))
withdrawal = int(input('how much you withdraw:'))
account_1 = account(balance)
account_1.deposit(deposit)
interest_rate = int(input('enter interestrate:'))
print('deposit of amount:',account_1.getbalance())
account_2 = account(balance_2)
account_2.withdrawal(withdrawal)
print('remaining amount:',account_2.getbalance())
account_interest = savingsaccount(balance_2,interest_rate)
print('total interest:', account_interest.interestAmount)
