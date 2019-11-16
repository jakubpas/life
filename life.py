import random,os,time
G=range(9)
B=[[random.getrandbits(1)for x in G]for y in G]
R={(1,2):1,(1,3):1,(0,3):1}
while True:
 b=[[0for x in G]for y in G]
 os.system('clear')
 for r in G:
  for c in G:
   n=0
   for X in[-1,0,1]:
    for Y in[-1,0,1]:
     n+=B[(r+X)%9][(c+Y)%9]
   n=n-B[r][c]
   b[r][c]=R.get((B[r][c],n),0)
 B=b
 for x in G:
  for y in G:
   print(B[x][y],end='')
  print()
 time.sleep(1)
