srm=int(input())
mgr=0
for vit in range(0,srm):
  if(pow(2,vit)>srm):
    break
  mgr=srm-pow(2,vit)
print(mgr)
