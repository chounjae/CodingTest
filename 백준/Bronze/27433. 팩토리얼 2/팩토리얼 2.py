def fabo(request) :
    result = 1
    for i in range(request) :
        temp = request - i
        result *= temp
    return result





put = int(input())

print(fabo(put))