#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
x = str(number)
y = x[-1]
z = int(y)
if number < 0:
 z = -(z)
if number < 0:
    print("The last digit of %d is %s and is less than 6 and not 0" % (number, z))
elif number > 0 and z < 6:
    print("The last digit of %d is %s and is less than 6 and not 0" % (number, z))
elif number > 0 and z > 6:
    print("The last digit of %d is %s and is greater than 6 and not 0" % (number, z))
elif z == 0:
    print("The last digit of %d is %s and is 0" % (number, z))
