from datetime import datetime
from cs1033_evaluator import evaluate_lab7

def days_to_birthday(date):
    '''
    Calculates the number of days that have passed since the 1st of January 
    to the given date.

    :param date: A date string in the format of yyyy-mm-dd
    :return: The number of days to the date from 1st of January 
             (eg: date->2021-01-01, return->1)
    '''

    # Convert the date string to a datetime object
    datetime_object = datetime.strptime(date, "%Y-%m-%d")

    # Extract only the date and remove the timestamp
    date = datetime_object.date()

    # Find the number of days since the begining of the year
    num_days = date.timetuple().tm_yday

    return num_days


a=[]
fo=open('nnn.txt','r')
x=fo.read()
t=x.split()
for i in range(len(t),-1,3):
    c=t[i:i+3]
    a.append(c)
for j in range(len(a)):
    b=days_to_birthday(a[j][1])
    if a[j][2]=='F':
        day=b+500
    else:
        day=b
    y=a[j][0]+' '+a[j][1][0:4]+str(day)+' '
    fl=open("output.txt",'a')
    fl.write(y)
    fl.close()



evaluate_lab7()
