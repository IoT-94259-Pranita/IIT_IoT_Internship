def function_overlapping(list1,list2):
    for item in list1:
       if item in list2:
           return True
       return False
    
list1=input("Enter elements of first list=")
list2=input("Enter elements of second list=")

if function_overlapping(list1,list2):
    print("The list have atleast one common element")
else:
    print("The list have no common element")