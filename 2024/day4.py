def count_word(data) -> int:
    rows, cols = len(data), len(data[0])
    word = 'XMAS'
    word_len = len(word)
    res = 0

    directions = [
        (-1, -1), # up left
        (-1, 0),  # up
        (-1, 1),  # up right
        (0, 1),   # right
        (1, 1),   # right down
        (1, 0),   # down
        (1, -1),  # left down
        (0, -1),  # left
    ]

    def check_direction(row, col, row_delta, col_delta) -> bool:
        for i in range(word_len):
            r, c = row + i * row_delta, col + i * col_delta
            if r < 0 or r >= rows or c < 0 or c >= cols or data[r][c] != word[i]:
                return False
        return True

    for row in range(rows):
        for col in range(cols):
            for row_delta, col_delta in directions:
                if check_direction(row, col, row_delta, col_delta):
                    res += 1

    return res

def count_x_mas(data) -> int:
    rows, cols = len(data), len(data[0])
    count = 0

    def check_x_mas(row, col)-> bool:
        if row - 1 < 0 or row + 1 >= rows or col - 1 < 0 or col + 1 >= cols:
            return False

        res1 = (
            (data[row - 1][col - 1] == 'M' and data[row][col] == 'A' and data[row + 1][col + 1] == 'S') and
            (data[row + 1][col - 1] == 'M' and data[row][col] == 'A' and data[row - 1][col + 1] == 'S')
        )
        res2 = (
            (data[row - 1][col - 1] == 'M' and data[row][col] == 'A' and data[row + 1][col + 1] == 'S') and
            (data[row + 1][col - 1] == 'S' and data[row][col] == 'A' and data[row - 1][col + 1] == 'M')
        )
        res3 = (
            (data[row - 1][col - 1] == 'S' and data[row][col] == 'A' and data[row + 1][col + 1] == 'M') and
            (data[row + 1][col - 1] == 'S' and data[row][col] == 'A' and data[row - 1][col + 1] == 'M')
        )
        res4 = (
            (data[row - 1][col - 1] == 'S' and data[row][col] == 'A' and data[row + 1][col + 1] == 'M') and
            (data[row + 1][col - 1] == 'M' and data[row][col] == 'A' and data[row - 1][col + 1] == 'S')
        )
        return res1 or res2 or res3 or res4

    for row in range(rows):
        for col in range(cols):
            if check_x_mas(row, col):
                count += 1

    return count


with open('input4.txt') as file:
    data = [line.strip() for line in file]

print(count_word(data))

print(count_x_mas(data))