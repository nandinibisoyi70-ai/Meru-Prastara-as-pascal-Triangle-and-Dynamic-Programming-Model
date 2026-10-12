# Meru-Prastara as Pascal's Triangle using Dynamic Programming

## About the Project
Meru-Prastara is an ancient Indian mathematical arrangement closely related to Pascal's Triangle. This project demonstrates how the triangle can be generated using Python and Dynamic Programming.

Each row starts and ends with `1`. Every inner value is calculated by adding the two adjacent values directly above it. Previously computed rows are stored and reused to generate the next row.

## Objectives
- Connect the Indian Knowledge System (IKS) concept of Meru-Prastara with Computer Science.
- Generate the first `n` rows of Pascal's Triangle.
- Demonstrate recurrence relations and Dynamic Programming.
- Validate normal, boundary, and invalid inputs.

## Concepts Used
- Meru-Prastara / Pascal's Triangle
- Dynamic Programming
- Lists and nested lists
- Loops and recurrence relations
- Input validation
- Time and space complexity

## Algorithm
1. Accept the number of rows `n`.
2. Reject non-integer input and negative values.
3. Create an empty list to store the triangle.
4. For each row, initialize all positions to `1`.
5. Calculate each inner value using the two adjacent values from the previous row.
6. Add the completed row to the triangle.
7. Return or print the triangle.

## Python Implementation

```python
def generate_meru_prastara(n):
    """Generate n rows of Meru-Prastara (Pascal's Triangle)."""
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer")

    if n < 0:
        raise ValueError("n must be non-negative")

    triangle = []

    for i in range(n):
        row = [1] * (i + 1)

        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle


def print_meru_prastara(n):
    triangle = generate_meru_prastara(n)

    if n == 0:
        print("(empty triangle)")
        return

    width = len(" ".join(map(str, triangle[-1])))

    for row in triangle:
        text = " ".join(map(str, row))
        print(text.center(width))


if __name__ == "__main__":
    n = 6
    print_meru_prastara(n)
```

## Sample Output

For `n = 6`:

```text
          1
         1 1
        1 2 1
       1 3 3 1
      1 4 6 4 1
    1 5 10 10 5 1
```

*Note: Spacing may vary depending on the terminal.*

## Example Test Cases

| Input (`n`) | Expected result |
|---:|---|
| `0` | `[]` |
| `1` | `[[1]]` |
| `2` | `[[1], [1, 1]]` |
| `3` | `[[1], [1, 1], [1, 2, 1]]` |
| `5` | Last row: `[1, 4, 6, 4, 1]` |
| `6` | Last row: `[1, 5, 10, 10, 5, 1]` |
| `10` | Generates 10 rows |
| `15` | Generates 15 rows |
| `-1` | Raises `ValueError` |
| `3.5` | Raises `TypeError` |

## Complexity Analysis
- **Time Complexity:** `O(n²)` — the total number of generated values is `n(n + 1) / 2`.
- **Space Complexity:** `O(n²)` — the complete triangle is stored in memory.

## Limitations
- Storing the complete triangle requires quadratic memory.
- Very large triangles are difficult to display in a terminal.
- The implementation focuses on generating the triangle and does not cover every application of Meru-Prastara in ancient Indian prosody.

## Conclusion
This project demonstrates how Meru-Prastara can be represented as Pascal's Triangle and generated using Dynamic Programming. By storing and reusing previously calculated rows, it illustrates recurrence relations, nested lists, algorithm design, and computational complexity.

## Author
**Nandini Bisoyi**  
B.Sc. Computer Science — Semester V  
Smt. Devkiba Mohansinhji Chauhan College of Commerce and Science, Silvassa  
Academic Year: 2026–2027
