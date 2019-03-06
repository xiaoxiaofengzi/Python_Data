import datetime
import time

def holiday(d, s="20180101", e="20181231"):
    hol = {"20180101", "20180215", "20180216", "20180217", "20180218", "20180219", "20180220",
           "20180221", "20180405", "20180406", "20180407", "20180429", "20180430", "20180501"
           "20180616", "20180617", "20180618", "20180922", "20180923", "20180924", "20181001",
           "20181002", "20181003", "20181004", "20181005", "20181006", "20181007", "20181230",
           "20181231"}
    work = {"20180211", "20180224", "20180408", "20180428", "20180929", "20180930", "20181229"}
    s1 = datetime.datetime.strptime(s, '%Y%m%d')
    e1 = datetime.datetime.strptime(e, '%Y%m%d')
    if not isinstance(d, str):
        print("Please input string date")
        return -1
    else:
        d1 = datetime.datetime.strptime(d, '%Y%m%d')
        if d1 > e1 or d1 < s1:
            print("not in 2018 year")
            return -1
        elif d in hol:
            return 2
        elif d in work:
            return 0
        elif d1.weekday() in (5, 6):
            return 1
        else:
            return 0


if __name__ == "__main__":
    day = "20181201"
    print(holiday(day))