n= int(input());
m= int(input());
# 10<=n<=m<= 10^9
ans = 0;

while n < m:
	n = int(n/10) + n;
	ans += 1; 

print(ans);
