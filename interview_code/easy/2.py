def cal_leap(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


if __name__ == '__main__':
  while True:
    year = int(input())
    print(cal_leap(year))