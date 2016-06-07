import rosalind

dataFile = raw_input("File name: ")
data = rosalind.readFile(dataFile)
total = ""
three = ""
for i in data:
  if len(three) > 2:
    total += rosalind.rnaToProtein[three]
    print rosalind.rnaToProtein[three]
    three = ""
    three += i
  else:
    three += i

output = open("output", 'w')
output.write(total)
