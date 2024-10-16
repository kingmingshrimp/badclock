import datetime

print(r""" 
  _               _      _            _    
 | |             | |    | |          | |   
 | |__   __ _  __| | ___| | ___   ___| | __
 | '_ \ / _` |/ _` |/ __| |/ _ \ / __| |/ /
 | |_) | (_| | (_| | (__| | (_) | (__|   < 
 |_.__/ \__,_|\__,_|\___|_|\___/ \___|_|\_\

""")


print("hi welcome to badclock, i guess you want to know what time it is")





now = datetime.datetime.now().strftime("%H:%M")

print(now)
print(now)