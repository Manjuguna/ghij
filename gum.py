vd=int(input())
gu=0
for v in range(0,vd):
  if(pow(2,v)>vd):
    break
  gu=v-pow(2,v)
print(gu)
