def multiplication_table(x1, x2, y1, y2):
    max_spaces = len(str(x2*y2)) + 1
    print((max_spaces - 1) * " " + " |", end="")
    for x in range(x1, x2 + 1):
        print(f"{x : {max_spaces}}", end="")
    print()
    for x in range(x1, x2 + 2):
        print(max_spaces * "-", end="")
    print()
    for y in range(y1, y2 + 1):
        print(f"{y : {max_spaces - 1}} |", end="")
        for x in range(x1, x2 + 1):
            print(f"{x * y : {max_spaces}}", end="")
        print()
