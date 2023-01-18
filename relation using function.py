def relation(a,b):
  if(a>b):
    return("greater")
  elif(a<b):
    return("lesser")
  else:
    return("zero")
a=int(input("enter the number:"))
b=int(input("enter the number:"))
print(relation(a,b))

