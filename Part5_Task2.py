steps = int(input("Number of the steps"))
for stepsNo in range(steps):
    s = input('Enter the strings: ')
    reverse = s[::-1]
    n = len(s)
    for i in range(1, n):
        d1 = abs(ord(s[i]) - ord(s[i - 1]))
        d2 = abs(ord(reverse[i]) - ord(reverse[i - 1]))
        if d1 != d2:
            print("Not Funny")
            break
    else:
        print("Funny")
