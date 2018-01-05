from math import pi


def calculate_expected_square_iterative(n, k):
    """Calculates the expected square of the size of a randomly picked final
    component. Equivalent to all radii being 1."""
    # Conditioning on first step we just solve the case 1, 1, 1,..., 1, 2.
    x = 1
    for i in range(k):
        current_n = n - (k - 1) + i
        current_k = i + 1
        mu = current_n / (current_n - 1)
        sigma_squared = (current_n - 2) / (current_n - 1) ** 2
        E_N = (current_n - 1) / (current_n - current_k)
        E_N_squared = x
        if current_k == 1:
            # Edge case to prevent division by zero.
            x = (current_n + 2) / (current_n - 1)
            continue
        x = sigma_squared * (E_N - (E_N_squared - E_N) / (current_n - 2)) + (mu ** 2) * E_N_squared
    return x


n, k = map(int, input().strip().split())
radii = [int(s) for s in input().strip().split()]

if k == 0:
    print(pi * sum(r ** 2 for r in radii))
else:
    mu = sum(radii) / n
    sigma_squared = sum((r - mu) ** 2 for r in radii) / n
    E_N = n / (n - k)
    E_N_squared = calculate_expected_square_iterative(n, k)

    total_area = pi * (n - k) * (sigma_squared * (E_N - (E_N_squared - E_N) / (n - 1)) + (mu ** 2) * E_N_squared)
    print(total_area)

# # RECURSIVE
# def calculate_expected_square(n, k):
#     """Calculates the expected square of the size of a randomly picked final
#     component. Equivalent to all radii being 1."""
#     if k == 0:
#         return 1
#     elif k == 1:
#         return (n + 2) / (n - 1)
#     # Conditioning on first step we just solve the case 1, 1, 1,..., 1, 2.
#     mu = n / (n - 1)
#     sigma_squared = (n - 2) / (n - 1) ** 2
#     E_N = (n - 1) / (n - k)
#     E_N_squared = calculate_expected_square(n - 1, k - 1)
#     return sigma_squared * (E_N - (E_N_squared - E_N) / (n - 2)) + (mu ** 2) * E_N_squared


# def calculate_expected_square(n, k):
#     """Calculates the expected square of the size of a randomly picked final
#     component. Equivalent to all radii being 1."""
#     if k == 0:
#         return 1
#     elif k == 1:
#         return (n + 2) / (n - 1)
#     # Conditioning on first step we just solve the case 1, 1, 1,..., 1, 2.
#     mu = n / (n - 1)
#     sigma_squared = (n - 2) / (n - 1) ** 2
#     # cov = (n + 1) / (n - 1) - mu ** 2
#     E_N = (n - 1) / (n - k)
#     E_N_squared = calculate_expected_square(n - 1, k - 1)
#     # print(n, k)
#     # print("Solving: " + "1 " * (n - 2) + "2", "with n = ", n - 1, "k = ", k - 1)
#     # print("mu", mu)
#     # print("cov", cov)
#     # print("sigma_squared", sigma_squared)
#     # print("E_N", E_N)
#     # print("E_N_squared", E_N_squared)
#     return sigma_squared * (E_N - (E_N_squared - E_N) / (n - 2)) + (mu ** 2) * E_N_squared
#     # return sigma_squared * E_N + (E_N_squared - E_N) * cov + (mu ** 2) * E_N_squared
#     # return (mu ** 2) * E_N_squared


# if k == 0:
#     print(pi * sum(radii) **2)
# else:
#     mu = sum(radii) / n
#     # pairs = sum(radii) ** 2 - sum(r ** 2 for r in radii)
#     # pairs /= n * (n - 1)
#     # cov = pairs - mu ** 2
#     sigma_squared = sum((r - mu) ** 2 for r in radii) / n
#     # Calculate E[N] and E[N^2] where N is the random variable counting the
#     # number of original creatures in a randomly picked final creature.
#     # Think of this by starting with each of the n - k final creatures with size 1.
#     # We then distribute k units randomly across these so we have
#     # N = 1 + X_1 + ... + X_k   where X_i ~ Ber(1 / (n - k))
#     #   = 1 + Y                 where Y ~ Bin (k, 1 / (n - k))
#     E_N = n / (n - k)
#     E_N_squared = calculate_expected_square(n, k)

#     total_area = pi * (n - k) * (sigma_squared * (E_N - (E_N_squared - E_N) / (n - 1)) + (mu ** 2) * E_N_squared)
#     # total_area = pi * (n - k) * (sigma_squared * E_N + (E_N_squared - E_N) * cov + (mu ** 2) * E_N_squared)
#     print(total_area)

#     # print("mu", mu)
#     # print("pairs", pairs)
#     # print("cov", cov)
#     # print("sigma_squared", sigma_squared)
#     # print("E_N", E_N)
#     # print("E_N_squared", E_N_squared)


# from math import pi


# n, k = map(int, input().strip().split())
# radii = [int(s) for s in input().strip().split()]

# if n == 1:
#     print(pi * radii[0] **2)
# else:
#     mu = sum(radii) / n
#     pairs = sum(radii) ** 2 - sum(r ** 2 for r in radii)
#     pairs /= n * (n - 1)
#     cov = pairs - mu ** 2
#     sigma_squared = sum((r - mu) ** 2 for r in radii) / n
#     # Calculate E[N] and E[N^2] where N is the random variable counting the
#     # number of original creatures in a randomly picked final creature.
#     # Think of this by starting with each of the n - k final creatures with size 1.
#     # We then distribute k units randomly across these so we have
#     # N = 1 + X_1 + ... + X_k   where X_i ~ Ber(1 / (n - k))
#     #   = 1 + Y                 where Y ~ Bin (k, 1 / (n - k))
#     E_N = 1 + k / (n - k)
#     E_N_squared = 1 + k / (n - k) * (3 + (k - 1) / (n - k))

#     total_area = pi * (n - k) * (sigma_squared * E_N + (E_N_squared - E_N) * cov + (mu ** 2) * E_N_squared)
#     print(total_area)

#     print("mu", mu)
#     print("pairs", pairs)
#     print("cov", cov)
#     print("sigma_squared", sigma_squared)
#     print("E_N", E_N)
#     print("E_N_squared", E_N_squared)


# r_1 r_2 r_3 ... r_n

# k = 1

# + \sigma 2 r_i r_j

# / (n (n - 1) / 2)

# E[X]
# var[X]
# E[X^2] = var[x] - E[X] ^2
# X ~ Unif[r_1,....,r_n]
# Y | X = r_i ~ Unif[r_1,...,r_n] \ {r_i}
# E[Y] = \sigma E[Y | X = r_i] P(X = r_i) = 1 / n (n - 1) (n - 1) \sigma r_i = E[X]

# E[X + Y + Z] = E[X] + E[Y] + E[Z]

# E[(X_1 + X_2 + X_3) ^2] ? X_i ~ Unif[r_1, ...., r_n] not indep.




# We have n - k creatures after k seconds with radii X_1 , .... , X_n-k.
# X_i identically distributed but not independent.
# E[X_1 ^2 + X_2 ^2 + ... + X_n ^2] = E[X_1 ^2] + .... + E[X_n-k ^2]
#                                   = (n - k) * E[X_i ^2]
#                                   = (n - k) * (var(X_i) + E[X_i] ^ 2)
#                                   = (n - k) * (sigma^2 E[N] + mu^2 E[N^2])

# X_i | N = m = Y_1 + .... + Y_m
# sample of random number of terms

# var(X_i) = N * var(Y_i) + N(N-1) cov(Y_i, Y_j) = N * sigma^2 + N(N-1) * cov
# Y_i ~ Unif[r_1, ..., r_n]

# E[X_i] = N * E[Y_i] = N * mu

# X_i
# size    probability
# k + 1   2 ^ k / (n (n - 1) ... (n - k + 1))
# k       2 /
# .
# .
# .
# 1      (n - 2) (n - 3) (n - 4) .... (n - 1 - k) / n (n - 1) .... (n - k + 1) = (n - k) (n -k - 1) / n (n - 1)
