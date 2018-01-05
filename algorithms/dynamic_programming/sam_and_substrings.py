N_string = input().strip()
mod = 1000000007
result = 0
substrings_ending_here = 0
for i, c in enumerate(N_string, start=1):
    digit = int(c)
    substrings_ending_here = (10 * substrings_ending_here + i * digit) % mod
    result = (result + substrings_ending_here) % mod
print(result)
