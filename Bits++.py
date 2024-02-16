def execute_bit_program(n, program):
    x = 0
    for statement in program:
        if "++" in statement:
            x += 1
        elif "--" in statement:
            x -= 1
    return x
n = int(input().strip())
program = [input().strip() for _ in range(n)]
result = execute_bit_program(n, program)
print(result)