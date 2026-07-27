from functools import reduce

scores=[90,85,None,70,100,None,40]

after_filter = list(filter(lambda x:x!=None, scores))

after_filter=list(filter(lambda x:x>60,after_filter))

after_map = list(map(lambda x:x+5,after_filter))

total=reduce(lambda x,y:(x+y),after_map)
print(total/len(after_map))

