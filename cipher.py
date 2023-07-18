from itertools import product
import time

#function to calculate the corresponding pliantext char from ciphertext char and correponding key
def brute(c, i):
    s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if 90 >= ord(c) >= 65:
        k = 26 - (90 - ord(c))
        tomove = (2 * i) + 1
        if k >= tomove:
            char = s[(26 + (k - tomove) - 1) % 26]
            return char
        else:
            char = s[(k + (26 - tomove) - 1) % 26]
            return char


# reading the input and output files from the text file
with open('l1-inp1.txt', 'r') as file:
    input_lines = [line.rstrip() for line in file]

# storing all the permutation of the key , repetition allowed.
fulist = []
file1 = open('result.txt', 'w')
for roll in product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], repeat=5):
    fulist.append(roll)

# measuring the time of running the application.
t = time.time()
for reslist in fulist:
    reslist = list(reslist)
    s = input_lines[1]
    res = ""
    loop = 0
    for i in range(len(s)):
        if (i + 1) % 6 == 0:
            res += " "
            loop = 0
        else:
            res += brute(s[i], reslist[loop])
            loop += 1
    if res == input_lines[0]:
        elapsed_time = time.time() - t
        file1.write(res)
        file1.write("\n")
        file1.write("time to run (in seconds): %.8f\n" % (elapsed_time,))
        file1.write("\n")
        file1.write("key below\n")
        with open('result.txt', 'w'):
            for item in reslist:
                file1.write(str(item) + " ")
        file1.write("\n")
        break
file1.close()
