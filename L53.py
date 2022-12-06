# the authors names are: Cadyn and Sarah
# n = int(input("Pick a number \n"))
def perfect_number(n):
    x = 0
    for y in range (1,n):
        if n % y == 0:
            x = x + y
    if x == n:
        print("True")
    else:
        print("False")

perfect_number(6)
perfect_number(15)
perfect_number(1000)
perfect_number(10000)
