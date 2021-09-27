import math
# Write your cone volume function in the space below...

def find_vol(radius, height):
    vol=(math.pi)*(radius**2)*(height/3)
    print("the volume of a cone with " + str(int(radius)) + " radius and " + str(int(height)) + " height is " + str(int(vol)))


# Do not change anything below these lines
def main():
    pass

if __name__ == '__main__':
    main()