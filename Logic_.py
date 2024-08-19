with open("GB_CURRENCY.py", "r") as f:
    note=f.read()

note=note.split(".")
for i in note:
    print(i)
