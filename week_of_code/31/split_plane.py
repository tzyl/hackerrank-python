from collections import defaultdict


horizontal_lines = defaultdict(list)
vertical_lines = defaultdict(list)
horizontal_lines_keys = []
vertical_lines_keys = []

q = int(input().strip())
for query in range(q):
    n = int(input().strip())
    for line in range(n):
        x1, y1, x2, y2 = map(int, input().strip().split())
        if x1 == x2:
            if not vertical_lines[x1]:
                # First time we've seen a vertical line at this x.
                vertical_lines_keys.append(x1)
            vertical_lines[x1].append((min(y1, y2), max(y1, y2)))
        elif y1 == y2:
            if not horizontal_lines[y1]:
                # First time we've seen a horizontal line at this y.
                horizontal_lines_keys.append(y1)
            horizontal_lines[y1].append((min(x1, x2), max(x1, x2)))

    horizontal_lines_keys.sort()
    vertical_lines_keys.sort()

    # Create a planar graph by adding vertices at intersections to use
    # Euler's formula to get the number of faces.
    v = 2 * n
    e = n
