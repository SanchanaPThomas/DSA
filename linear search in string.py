s=input()
m=input()
for i in range(len(s)):
    if s[i]==m:
        print(i)
        break
else:
    print(-1)
