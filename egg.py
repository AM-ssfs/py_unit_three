# Start writing your functions below this line
def top():
    print("  _______")
    print(" /       \\")
    print("/         \\")
def bottom():
    print("\         /")
    print(" \_______/")
def mid():
    print("-\"-'-\"-'-\"-")
def main():
    # all of your function calls should go here. Remove the word "pass" before adding function calls.
    for x in range(2):
        top()
        bottom()
        mid()
    bottom()
    top()
    mid()
    bottom()
if __name__ == '__main__':
    main()