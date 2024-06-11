def robot_transfer(matrix, k):
    n = len(matrix)
    count = 0

    def parse_coordinates(coord_str):
        x, y = map(int, coord_str.split(','))
        return x, y

    def simulate_moves(start_x, start_y):
        x, y = start_x, start_y
        moves = 0

        while moves < k:
            next_x, next_y = parse_coordinates(matrix[x][y])
            moves += 1

            if next_x == start_x and next_y == start_y:
                return moves == k

            x, y = next_x, next_y

        return False

    for i in range(n):
        for j in range(n):
            if simulate_moves(i, j):
                count += 1

    return count

# Example usage
matrix = [
    ["0,1", "0,0", "1,2"],
    ["1,1", "1,0", "0,2"],
    ["2,1", "2,0", "0,0"]
]
k = 2

result = robot_transfer(matrix, k)
print(result)