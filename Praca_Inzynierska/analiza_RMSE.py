import jednowym_gif

f = open("jednowymiarowa/RMSE.txt", "r")

lines = f.readlines()
n = 0
x50 = 0
x25 = 0
x10 = 0
x1 = 0
x01 = 0
x001 = 0
for line in lines:
    if(float(line[:-2])<0.5 and x50 == 0):
        print("X50",n)
        x50 = 1

    if (float(line[:-2]) < 0.25 and x25 == 0):
        print("X25", n)
        x25 = 1

    if (float(line[:-2]) < 0.1 and x10 == 0):
        print("X10",n)
        x10 = 1

    if (float(line[:-2]) < 0.01 and x1 == 0):
        print("X1",n)
        x1 = 1

    if (float(line[:-2]) < 0.001 and x01 == 0):
        print("X01",n)
        x01 = 1

    if (float(line[:-2]) < 0.000102 and x001 == 0):
        print("X001",n)
        x001 = 1

    n = n + 1




f.close()
