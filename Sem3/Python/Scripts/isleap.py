def is_leap(year):
    #return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)
    if year%4==0:
        if year % 400==0 or year%100!=0:
            return True
    else:
    	return False
    
year = int(input())
print(is_leap(year))
		