n= int(input());
m= int(input());
# 10<=n<=m<= 10^9
ans = 0;
pre = 1;

# ~300 AC

while(float(n * pre) < m):
	ans += 1;
	pre = float(pre * (1.1));

print(ans);
