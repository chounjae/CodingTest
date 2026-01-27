expressions = input().split('-')

groups = []
for expression in expressions:
    numbers = list(map(int, expression.split('+')))
    total = sum(numbers)

    groups.append(total)

result = 2 * groups[0] - sum(groups)
print(result)