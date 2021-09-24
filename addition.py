# Write your addition function in the space below...
def add_two(num1, num2):
    print("The sum of " + str(num1) + " and " + str(num2) + " is " + str(int(num1)+int(num2)))


# Do not change anything below these lines
def main():
        add_two(2, 5)
        add_two(12, 9)
        add_two(-5, 2)
        add_two(-7, -3)


if __name__ == '__main__':
    main()