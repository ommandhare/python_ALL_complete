"""
Read friends file store birth date and list of friends in dictionary
and send happy birthday email to all those who have birthday currentdate

"""

from datetime import date


friends={
    "om":date(2001,6,26),
    "hrushi":date(2000,5,12),
    "saish":date(2000,3,28),
    "nishad":date(2001,3,5)
}
today=date.today()
print(today)
for k,v in friends.items():
    if v.month==today.month and v.day==today.day:
        print("its",k,"'s ","Birthday Today")
        print("Mail: Happy Birthday",k)


print("\n")
print("OTHER friends birthdays in this month")
for k,v in friends.items():
    if v.month==today.month:
        print(k,v)