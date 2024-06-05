
def toBinary(number, bits, bini):
    for x in range(bits):
        if pow(2, bits - x - 1) <= number:
            bini += "1"
            number -= pow(2, bits - x - 1)
        else:
            bini += "0"
    return bini


def CompleteTo2(bits, bini):
    bini = bini.replace("0", "2")
    bini = bini.replace("1", "0")
    bini = bini.replace("2", "1")
    for x in range(bits):
        if int(bini[bits - x - 1]) + 1 == 2:
            bini = bini[:bits - x - 1] + "0" + bini[siv - x:]
        else:
            bini = bini[:bits - x - 1] + "1" + bini[siv - x:]
            break
    return bini


num = int(input("Enter Number: "))
siv = int(input("Enter Bits: "))
binary = ""
binary = toBinary(num, siv, binary)
binary = CompleteTo2(siv, binary)
print("hapoch: "+binary)
print("hello world")


