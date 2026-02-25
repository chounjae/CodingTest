import sys
input = sys.stdin.readline

n, m = map(int, input().split())
crr_x, crr_y, curr_dir = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(n)]
cleaned = [[0] * m for _ in range(n)]

dx = [-1, 0, 1, 0] # 북, 동, 남, 서
dy = [0, 1, 0, -1]


def turn_left(curr_dir):
    return (curr_dir - 1) % 4

while True:
    if cleaned[crr_x][crr_y] == 0:
        cleaned[crr_x][crr_y] = 1

    found = False

    for _ in range(4):
        curr_dir = turn_left(curr_dir)
        next_x = crr_x + dx[curr_dir]
        next_y = crr_y + dy[curr_dir]

        if 0 <= next_x < n and 0 <= next_y < m and room[next_x][next_y] == 0 and cleaned[next_x][next_y] == 0:
            crr_x, crr_y = next_x, next_y
            found = True
            break

    if found:
        continue

    back_dir = (curr_dir + 2) % 4
    back_x = crr_x + dx[back_dir]
    back_y = crr_y + dy[back_dir]

    if 0 <= back_x < n and 0 <= back_y < m and room[back_x][back_y] == 0:
        crr_x, crr_y = back_x, back_y
    else:
        break

cleaned_count = sum(row.count(1) for row in cleaned)
print(cleaned_count)