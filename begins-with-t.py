#Program to see if day starts with a T

print('This little program will check if today is a day starting with a T')

#how to get to today's day
import datetime
today = datetime.datetime.now()
print ('today is ', today.strftime('%A'))

#check if first letter of today is a T
letter = today.strftime('%A')[0]
print ('first letter is', letter)

if letter == "T":
    print("today starts with a T")
else:
    print("today does not start with a T")