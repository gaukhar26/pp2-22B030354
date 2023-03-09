from datetime import date, timedelta
y = date.today() - timedelta(1)
t = date.today() + timedelta(1)
print('yesterday :',y)
print('today:',date.today())
print('tomorrow :',t)