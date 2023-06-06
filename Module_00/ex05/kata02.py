import datetime

# Put this at the top of your kata02.py file
kata = (2019, 9, 25, 3, 30)

date = datetime.datetime(kata[0], kata[1], kata[2], kata[3], kata[4])
print(date.strftime("%m/%d/%Y %I:%M"))