def melodious_password(n):
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxz"
    alternate = [vowels, consonants]
    passwords = []
    # Start with vowel or consonant depending on j = 0 or 1.
    for j in range(2):
        current_passwords = [""]
        for i in range(n):
            new_passwords = []
            while current_passwords:
                password = current_passwords.pop()
                for c in alternate[(i + j) % 2]:
                    new_passwords.append(password + c)
            current_passwords = new_passwords
        passwords.extend(current_passwords)
    return passwords


n = int(input())
for password in melodious_password(n):
    print(password)
