import datetime
import os

# check for windows nt and clear the screen
def clearScreen():
  os.system('cls' if os.name == 'nt' else 'clear')

# print swag ascii art
def badclockArt():
  print(r""" 
  _               _      _            _    
 | |             | |    | |          | |   
 | |__   __ _  __| | ___| | ___   ___| | __
 | '_ \ / _` |/ _` |/ __| |/ _ \ / __| |/ /
 | |_) | (_| | (_| | (__| | (_) | (__|   < 
 |_.__/ \__,_|\__,_|\___|_|\___/ \___|_|\_\

  """)

def badcockArt():
    print(r"""
  _               _                _    
 | |             | |              | |   
 | |__   __ _  __| | ___ ___   ___| | __
 | '_ \ / _` |/ _` |/ __/ _ \ / __| |/ /
 | |_) | (_| | (_| | (_| (_) | (__|   < 
 |_.__/ \__,_|\__,_|\___\___/ \___|_|\_\  

  """)

def goodclockArt():
  print(r"""
                        _      _            _    
                       | |    | |          | |   
   __ _  ___   ___   __| | ___| | ___   ___| | __
  / _` |/ _ \ / _ \ / _` |/ __| |/ _ \ / __| |/ /
 | (_| | (_) | (_) | (_| | (__| | (_) | (__|   < 
  \__, |\___/ \___/ \__,_|\___|_|\___/ \___|_|\_\
   __/ |                                         
  |___/                                          
  
  """)

def goodcock():
  print(r"""
                        _                _
                       | |              | |
   __ _  ___   ___   __| | ___ ___   ___| | __
  / _` |/ _ \ / _ \ / _` |/ __/ _ \ / __| |/ /
 | (_| | (_) | (_) | (_| | (_| (_) | (__|   <
  \__, |\___/ \___/ \__,_|\___\___/ \___|_|\_\
   __/ |
  |___/

  """)

def goodcat():
  print(r"""
          |\___/|
         =) oYo (=
          \  ^  /
           )=*=(
          /     \
          |     |
         /| | | |\
         \| | |_|/\
         //_// ___/
             \_)
  """)

def usrContinue():
  input("\nPress Enter to continue or Crtl+C to quit:")

clearScreen()
badclockArt()

print("hi welcome to badclock")
print("\ni guess you want to know what time it is")
usrContinue()

# ask the user for the time, if it matches the real time then they win, if not try again
i = 0
while i == 0:

  clearScreen()
  badclockArt()

  # store the current time and ask the user for their guess
  now = datetime.datetime.now().strftime("%H:%M")

  print("what time do you think it is?")
  usrTime = input("\nEnter the current time [??:??]: ")

  # check if the user entered a valid time and if they guessed the time right
  try:
    validUsrTime = datetime.datetime.strptime(usrTime, "%H:%M")
    if usrTime == now:
      clearScreen()
      goodclockArt()
      print("woa. thats right")
      i += 1
      usrContinue()

    else:
      print("no... wrong..... try again")
      usrContinue()

  except ValueError:
    clearScreen()
    badcockArt()
    print("hey are you stupid. you need to enter a valid 24hr time")
    usrContinue()


    