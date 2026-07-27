from functools import reduce

scores=[90,85,None,70,100,None,40]

adjusted_scores = [x+5 for x in scores if x is not None and x >60]

total = reduce(lambda a,b:a+b,adjusted_scores)
average = total/len(adjusted_scores)

print("Adjusted Scores:",adjusted_scores)
print("Average:",average)