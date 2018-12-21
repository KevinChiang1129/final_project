data = input().split()
for h in range(5):
  data[h] = int(data[h])
  
a,b,c,x0,n = data[0],data[1],data[2],data[3],data[4]

ans = []
for i in range(n):
  if i == 0:
    x = (a * x0 + b) % c
  else:
    x = (a * x + b) % c
  ans.append(x)

print(*ans)