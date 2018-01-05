n, m, k = map(int, input().strip().split())
rows_with_tracks = {}
for track in range(k):
    r, c1, c2 = map(int, input().strip().split())
    if r not in rows_with_tracks:
        rows_with_tracks[r] = []
    rows_with_tracks[r].append((c1, c2))
total = n * m
for tracks in rows_with_tracks.values():
    # Sort by left value then right value of track (lexicographic)
    tracks.sort()
    right = 0
    for c1, c2 in tracks:
        # Take away contribution from this train track not counted already.
        if c1 > right:
            # No overlap with previous tracks.
            total -= (c2 - c1 + 1)
        elif c2 > right:
            total -= c2 - right
        if c2 > right:
            right = c2
print(total)
