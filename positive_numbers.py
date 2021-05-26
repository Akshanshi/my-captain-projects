list1 = [12,14,-95,3]
list2 = [12,-7,5,64,-14]
def positive(n):
    for i in n:
        if i>=0:
            print(i)
print("list 1 positives")           
list1_positive =positive(list1)
print("list 2 positives")
list2_positive= positive(list2)
