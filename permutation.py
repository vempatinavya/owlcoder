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
