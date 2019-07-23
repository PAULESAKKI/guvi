x=input()

c=0

for i in x:
  if i.isdigit():
    c = c+1
    break
  
  
if c==0:
  print ('no')
else:
  print ('yes')
