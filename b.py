import math
n= int (input('số tiền gửi:'))
m= int (input ('số tiền rút:'))
# 10<=n<=m<= 10^9
year=0 
year=math.log(m/n, 1+10/100)
print(int(year + 1));