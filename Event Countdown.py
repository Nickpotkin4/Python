import datetime

today = datetime.date.today() 

print("🌟Event Countdown Timer🌟")
print()
event = input("Input the event > ")
print()
year = int(input("Input the year > "))
print()
month = int(input("Input the month > "))
print()
day = int(input("Input the day > "))  
print()
eventDate = datetime.date(year, month, day)

difference = eventDate - today
difference = difference.days

if difference > 0:
  print(f"{event} is {difference} day(s) away!")
elif difference < 0:
  print(f"😭😭😭😭😭😭😭 You missed it by {difference} days!")
else:
  print(f"🎉🎉{event} is today! 🎉🎉")
