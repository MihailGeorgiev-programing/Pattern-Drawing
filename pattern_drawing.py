shape = input("Input pattern('Pattern {number of pattern}'): ")
rows = int(input("Input number of rows: "))
pattern = "*"


def right_angled_triangle(pattern):
    for i in range(rows):
        print(pattern)
        pattern += "*"


def square_with_hollow_centre(pattern):
    print(pattern * rows)
    for j in range(rows - 2):
        print("*" + (" " * (rows - 2)) + "*")
    print(pattern * rows)


def diamond(pattern):
    counter = 0

    for k in range(rows // 2):
        space = (rows // 2 - counter) * " "
        print(space + pattern * counter + pattern + pattern * counter)
        counter += 1

    print(pattern * rows)
    counter -= 1

    for m in range(rows // 2):
        space = (rows // 2 - counter) * " "
        print(space + pattern * counter + pattern + pattern * counter)
        counter -= 1


def left_angled_triangle(pattern):
    for n in range(rows, 0, -1):
        print(pattern * n)


def pyramid(pattern):
    counter = 0

    for k in range(rows):
        space = (rows - counter) * " "
        print(space + pattern * counter + pattern + pattern * counter)
        counter += 1


def main():
    if shape == "Pattern 1":
        right_angled_triangle(pattern)
    elif shape == "Pattern 2":
        square_with_hollow_centre(pattern)
    elif shape == "Pattern 3":
        diamond(pattern)
    elif shape == "Pattern 4":
        left_angled_triangle(pattern)
    elif shape == "Pattern 5":
        pyramid(pattern)
    else:
        print("Incorrect input!")
        print("Try again!")


main()
