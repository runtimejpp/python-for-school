# function of a circle 
# with test case 


from math import pi


def circle_area(r):
    return pi*(r**2)

radii = [2, 3, 4, -3, 2+5j, True, "radius"]
message = "Area of Circle with r = {radius} is {area}"

# Test function
for r in radii:
    A = circle_area(r)
    print(message.format(radius=r, area=A))


new_message = "{Jason}, This is incorrect"
print(new_message)
