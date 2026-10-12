"""Generate and display Meru-Prastara (Pascal's Triangle)."""


def generate_meru_prastara(n):
    """Return the first n rows of Meru-Prastara.

    Args:
        n: Number of rows to generate.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.

    Returns:
        A list containing n rows of Pascal's Triangle.
    """
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer")

    if n < 0:
        raise ValueError("n must be non-negative")

    triangle = []

    for row_index in range(n):
        row = [1] * (row_index + 1)

        if row_index > 0:
            previous_row = triangle[row_index - 1]

            for column_index in range(1, row_index):
                row[column_index] = (
                    previous_row[column_index - 1]
                    + previous_row[column_index]
                )

        triangle.append(row)

    return triangle


def format_meru_prastara(triangle):
    """Return a centered string representation of the triangle."""
    if not triangle:
        return "(empty triangle)"

    width = len(" ".join(map(str, triangle[-1])))
    return "\n".join(
        " ".join(map(str, row)).center(width)
        for row in triangle
    )


def print_meru_prastara(n):
    """Generate and print n rows of Meru-Prastara."""
    triangle = generate_meru_prastara(n)
    print(format_meru_prastara(triangle))


def main():
    """Read the number of rows and display the triangle."""
    try:
        n = int(input("Enter the number of rows: "))
        print_meru_prastara(n)
    except (ValueError, TypeError) as error:
        print(f"Invalid input: {error}")


if __name__ == "__main__":
    main()
