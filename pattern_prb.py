#right half pyramid problem 
n = 3
def right_half_pyramid(n):
    count = n
    while count>=1:
        print("*"*count)
        count-=1

# right_half_pyramid(5)

#using nested loop
def right_half_nested(n):
    for i in range(n,0,-1):
        for j in range(i,0,-1):
            print("*", end="")
        print()

right_half_nested(4)