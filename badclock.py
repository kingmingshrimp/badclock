import datetime
import os

# check for windows and clear the screen
os.system('cls' if os.name == 'nt' else 'clear')

# print swag ascii art
print(r""" 
  _               _      _            _    
 | |             | |    | |          | |   
 | |__   __ _  __| | ___| | ___   ___| | __
 | '_ \ / _` |/ _` |/ __| |/ _ \ / __| |/ /
 | |_) | (_| | (_| | (__| | (_) | (__|   < 
 |_.__/ \__,_|\__,_|\___|_|\___/ \___|_|\_\

""")


print("hi welcome to badclock")
print("i guess you want to know what time it is")
input("[Press Enter to continue...]")

# initialise loop
correct = "False"

while bool(correct) != True:

    break


now = datetime.datetime.now().strftime("%H:%M")

#answer = input("Enter yes or no: ")
#if answer.lower() == "yes":
#    print("YES!!!")
#elif answer.lower() == "no":
#    print("Oh no")
#else: print("Please enter yes or no.")