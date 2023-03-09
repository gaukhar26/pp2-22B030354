from datetime import datetime, time
def diff_sec(dt2, dt1):
  timedelta = dt2 - dt1
  return timedelta.days * 24 * 3600 + timedelta.seconds
date1 = datetime.strptime('20-04-2022 13:45:45', '%d-%m-%Y %H:%M:%S')
date2 = datetime.now()
print("\n%d seconds" %(diff_sec(date2, date1)))
print()