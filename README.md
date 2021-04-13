# Zuri-Task-4
Zuri Internship, Backend - Django track. Fourth task

# How to use
- Instantiate the object with the Budget class
- The Budget class accepts one parameter; the name of the object
- The deposit method accepts one argument; how much you want to depositt
- The withdraw method accepts one argument; how much you want to withdraw
- The balanceFunc method accepts no argument; prints your current balance
- The transfer method accepts two arguments:
    - The first being how much you want to transfer
    - The second being the name of the the object you want to transfer to

# You can use the ffg to test run the code
pp = Budget("food")  
pp.deposit(100)  
qq = Budget("Home")  
qq.deposit(450)  
pp.balanceFunc()  
qq.withdraw(150)  
qq.balanceFunc()  
print("*"*25)  
qq.transfer(50, pp)  
qq.balanceFunc()  
pp.balanceFunc()  
