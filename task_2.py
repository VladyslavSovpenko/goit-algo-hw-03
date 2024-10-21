import turtle


def koch_snowflake_side(length, level):
    if level == 0:
        turtle.forward(length)
    else:
        length /= 3
        koch_snowflake_side(length, level - 1)
        turtle.left(60)
        koch_snowflake_side(length, level - 1)
        turtle.right(120)
        koch_snowflake_side(length, level - 1)
        turtle.left(60)
        koch_snowflake_side(length, level - 1)


def koch_snowflake(length, level):
    for _ in range(3):
        koch_snowflake_side(length, level)
        turtle.right(120)


def main():
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-150, 100)
    turtle.pendown()

    level = int(input("Введіть рівень рекурсії (від 0 до 6): "))
    length = 300

    koch_snowflake(length, level)

    turtle.done()


if __name__ == "__main__":
    main()
