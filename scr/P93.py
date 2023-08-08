import itertools

def evaluate(expression):
    try:
        return eval(expression)
    except ZeroDivisionError:
        return None
    except SyntaxError:
        return None

def generate_expressions(digits):
    operators = ['+', '-', '*', '/']
    expressions = []
    for permutation in itertools.permutations(digits):
        for op1 in operators:
            for op2 in operators:
                for op3 in operators:
                    expressions.append(f'({permutation[0]}{op1}{permutation[1]}){op2}{permutation[2]}{op3}{permutation[3]}')
                    expressions.append(f'({permutation[0]}{op1}{permutation[1]}{op2}{permutation[2]}){op3}{permutation[3]}')
                    expressions.append(f'{permutation[0]}{op1}({permutation[1]}{op2}{permutation[2]}){op3}{permutation[3]}')
                    expressions.append(f'{permutation[0]}{op1}({permutation[1]}{op2}{permutation[2]}{op3}{permutation[3]})')
                    expressions.append(f'{permutation[0]}{op1}{permutation[1]}{op2}({permutation[2]}{op3}{permutation[3]})')
    return expressions

def consecutive_positive_integers(digits):
    expressions = generate_expressions(digits)
    results = set()
    for expr in expressions:
        value = evaluate(expr)
        if value is not None and value > 0 and int(value) == value:
            results.add(int(value))
    i = 1
    while i in results:
        i += 1
    return i - 1

max_consecutive = 0
max_digits = None

for combination in itertools.combinations(range(1, 10), 4):
    count = consecutive_positive_integers(combination)
    if count > max_consecutive:
        max_consecutive = count
        max_digits = combination

print(''.join(str(d) for d in max_digits))