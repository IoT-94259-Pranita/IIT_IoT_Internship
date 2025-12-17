import geometry as g

print("1.Area of Circle")
print("2.Area of Rectangle")

choice=int(input("Enter your choice:"))

if(choice==1):
    r=float(input("Enter the radius of circle="))
    print(f"Area of circle={g.circle(r)}")
else:
    len=float(input("enter length of rectangle="))
    ben=float(input("enter breadth of rectangle="))
    print(f"Area of rectangle={g.rectangle(len,ben)}")