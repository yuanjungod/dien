import random

fi = open("local_test", "r")
ftrain = open("local_train_splitByUser", "w")
ftest = open("local_test_splitByUser", "w")

while True:
    rand_int = random.randint(1, 10)
    noclk_line = fi.readline().strip()
    clk_line = fi.readline().strip()
    if noclk_line == "" or clk_line == "":
        break
    if rand_int == 2:
        ftrain.write(noclk_line + "\n")
        ftest.write(clk_line + "\n")
        # print(">> ftest", noclk_line)
        # print >> ftest, clk_line
    else:
        ftrain.write(noclk_line + "\n")
        ftrain.write(clk_line + "\n")
        # print >> ftrain, noclk_line
        # print >> ftrain, clk_line
