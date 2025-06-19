
#In this task I am going to calculate the area of area of complex shapes like a trapezoid
# or an ellipse.

#Formula to calculate the area of trapezoid

#area= 1/2*a*b*h

# a,b are lengths of the two parallel sides (bases)
#h = height (perpendicular distance between bases)

def area_trapezoid(a,b,h):
    return (1/2)*(int(a)*int(b)*h)


a,b=(input("Enter bases: ").split())
h=int(input("Enter height: "))

if(int(a)<0 or int(b)<0 or h<0):
    print("Length can never be negative!")
else:
    print("Area of trapezoid is: ",area_trapezoid(a,b,h))
    


#Formula to calculate the area of ellipse


#Area=π×a×b

# a = semi-major axis (longest radius)
# b = semi-minor axis (shortest radius)



def area_ellipse(a,b):
    return 3.1417*a*b


min_ax=int(input("Enter semi-minor axis: "))
max_ax=int(input("Enter semi-major axis: "))

print("Area of ellipse is: ",area_ellipse(min_ax,max_ax))