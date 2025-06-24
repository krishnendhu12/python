name=input("krishnendhu: ")
USN=input("1AY24BT023: ")
def print_zigzag(string):
    row1 = ""
    row2 = ""
    row3 = ""
    for i, ch in enumerate(string):
        if i % 4 == 0:
            row1 += ch
            row2 += " "
            row3 += " "
        elif i % 4 == 1 or i % 4 == 3:
            row1 += " "
            row2 += ch
            row3 += " "
        else:
            row1 += " "
            row2 += " "
            row3 += ch

    print(row1)
    print(row2)
    print(row3)
print_zigzag("HELLOZIGZAG")
