for _ in range(int(input())):
    s=input()
    words=s.split()
    result=[]
    for word in words:
        if word.isupper():
            result.append(word)
        else:
            result.append(word.capitalize())
    print(" ".join(result))
