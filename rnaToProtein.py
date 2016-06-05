import rosalind

data = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
three = ""
for i in data:
  if len(three) > 2:
    print rosalind.rnaToProtein[three]
    three = ""
    three += i
  else:
    three += i
