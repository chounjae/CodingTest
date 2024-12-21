num = int(input())
cuttybear = 0
for i in range(num) :
    compare = input()
    if compare == 'ENTER' :
        history = set()
    elif compare not in history :
        cuttybear += 1
        history.add(compare)
print(cuttybear)