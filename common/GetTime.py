
import time
import datetime
import random
import calendar
def get_time():
    now = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    #print(now)
    if now.count('-') != 2:
        raise ValueError('- is error')
    year, month = str(now).split('-')[0], str(now).split('-')[1]
    end = calendar.monthrange(int(year), int(month))[1]
    start_date = '%s-%s-01 00:00:00' % (year, month)
    start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S")
    stat_time = int(time.mktime(start_date.timetuple()))
    #print(start_date,stat_time)


    end_date = '%s-%s-%s 23:59:59' % (year, month, end)
    end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d %H:%M:%S")
    end_time = int(time.mktime(end_date.timetuple()))
    #print(end_date, end_time)





    return stat_time,end_time

if __name__ == '__main__':
   get_time()