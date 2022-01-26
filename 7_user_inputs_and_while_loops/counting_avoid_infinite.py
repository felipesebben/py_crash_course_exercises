#this one is ok:
x = 1
while x <= 5:
    print(x)
    x += 1

#Yet this loop runs forever!
x = 1
while x <= 5:
    print(x)

#since x always equals 1, True condition will always be met and the loop will never stop.
#CTRL-C or close the terminal!