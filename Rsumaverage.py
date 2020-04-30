import  itertools
myfile = open('6_digit_code.txt', 'w')
for i in itertools.product(range(10), repeat=6):
  myfile.write("%s\n" % ''.join(map(str, i)))  
myfile.close()