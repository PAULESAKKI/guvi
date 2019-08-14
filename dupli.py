a=map(int,input().split())
tmp=[]

for i in a:
  if i not in tmp:
    tmp.append(i)
    print(i)
