n=int(input()) 
for i in range(n):
  l=[int(x) for x in input().split()]
for i in range(1,n-1):
  if l.count(i)>=2:
   print(i,end=' ')
print()
