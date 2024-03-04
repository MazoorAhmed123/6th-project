names = ("manzoor", "Tayyab", "Asas")
comps = ("dell", "HBL", "NBP")
zipped = zip(names, comps)

for (a, b) in zipped:
    print(f"Name: {a}, Company: {b}")
