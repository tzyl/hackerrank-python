def calculate_number_of_turns(A):
    number_of_turns = 0
    n = len(A)
    i = 0
    while i < n:
        while i < n and A[i] == 1:
            i += 1
        # Now start of a sub-game.
        j = i
        while j < n and not (A[j] == 1 and (j == n - 1 or A[j + 1] == 1)):
            j += 1
        number_of_turns += max(j - i - 2, 0)
        i = j + 1
    return number_of_turns


g = int(input())
for game in range(g):
    n = int(input())
    A = [int(s) for s in input().split()]
    number_of_turns = calculate_number_of_turns(A)
    print("Alice" if number_of_turns % 2 == 1 else "Bob")
