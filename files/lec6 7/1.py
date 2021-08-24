import datetime

def add_days(cur_date, n):
    return cur_date + datetime.timedelta(days = n)

'''
cur_date = datetime.date(2016,2,10)
print(add_days(cur_date, 30))
'''