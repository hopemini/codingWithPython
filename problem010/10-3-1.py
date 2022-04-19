num = int(input())
def convertToTitle(columnNumber):
    return "" if columnNumber == 0 else convertToTitle((columnNumber - 1) // 26) + chr((columnNumber - 1) % 26 + ord('A'))

print(convertToTitle(num)) 
