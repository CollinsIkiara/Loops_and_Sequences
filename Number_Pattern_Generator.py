#Number Pattern Generator

def number_pattern(n):
    if not isinstance(n, int):
        return 'Argument must be an integer value.'
    elif n < 1:
        return 'Argument must be an integer greater than 0.'
    else:
        result = []
        for i in range(1, n + 1):
            result.append(str(i))
        return ' '.join(result)

print(number_pattern(1.4))
print(number_pattern(-1))
print(number_pattern(4))