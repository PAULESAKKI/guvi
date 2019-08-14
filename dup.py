a=map(int,input().split())
tmp=[]

for i in a:
  if i in tmp:
    print(i)
  else:
    tmp.append(i)
