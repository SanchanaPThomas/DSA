t = int(input())

while t > 0:
    s = input()
    vowels="aeiou"
    for i in range(len(s)-2):
        if s[i] in vowels and s[i+1] in vowels and s[i+2] in vowels:
            print("Happy")
            break
    else:
        print('Sad')
    t -= 1
