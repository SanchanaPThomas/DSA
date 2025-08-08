for _ in range(int(input())):
    s=input()
    t=input()
    m=""
    for i in range(len(s)):
        if s[i]==t[i]:
            m+="G"
        else:
            m+="B"
    print(m)
