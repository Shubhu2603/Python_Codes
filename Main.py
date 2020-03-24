import math
def Input():
    no=float(input("Enter the number"))
    return no

def main():
    ip=Input()
    print(math.fabs(ip))

if __name__=="__main__":
    main()