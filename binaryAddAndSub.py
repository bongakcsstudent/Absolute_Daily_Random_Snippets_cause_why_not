#Binary Calculation
#Literally no error catch lmao, just shitting myself
user_Choice = input("Choose the letter of action: (a) Addition (b) Subtraction ")
inputOne = int(input("First decimal value: "))
inputTwo = int(input("Second decimal value: "))
bi_nu = ""  

if user_Choice == "a":
    user_input = inputOne + inputTwo
else:
    user_input = inputOne - inputTwo

while user_input > 0:
    rem = user_input % 2
    bi_nu = str(rem) + bi_nu
    user_input = user_input // 2  

print("Binary:", bi_nu)




