# Python Candidates - Question 2

def isTriangle(a, b, c): 
      
    if (a + b <= c) or (a + c <= b) or (b + c <= a) :
        return False
    else:
        return True     
    
def isRectangle(l1, b1, l2, b2):
     
    if (l1 == l2 and b1 == b2):
        return True
    else:
        return False   
  
a,b,c = [int(i) for i in input(" Enter Sides of the Triange : ").split()]
l1,b1,l2,b2 = [int(i) for i in input(" Enter Sides of the Rectangle : ").split()]

if isTriangle(a, b, c):
    print("\nValid Triangle") 
else:
    print("\nInvalid Triangle")
    
if isRectangle(l1,b1,l2,b2):
    print("\nValid Rectangle") 
else:
    print("\nInvalid Rectangle")