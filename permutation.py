def permutation(l):
  if len(l)==0:
    return 0
  if len(l)==1:
    return [l]
  lst=[]
  for i in range(len(l)):
    m=l[i]
    newlst=l[:i]+l[i+1:]
    for i in permutation(newlst):
      lst.append([m]+p)
  return lst
l=list('2346')
for i in permutation(l):
  print(i)
#this code is only for single digit numbers like 2 4 5 6 not for 10 13 like that
