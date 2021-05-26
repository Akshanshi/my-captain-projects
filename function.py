def most_frequent(string):
    d= dict()
    for key in string:
        if key not in d:
            d[key]= 1
        else:
            d[key]+=1
    return d
a= input("please enter a string:")
b= [most_frequent(a)]
c= sorted(b[0].items(), key= lambda x:x[1], reverse= True)
print(c)
