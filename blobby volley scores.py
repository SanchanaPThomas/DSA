t = int(input())

while t > 0:
    n = int(input())
    s = input()
    alice_score=0
    bob_score=0
    server='A'
    for winner in s:
        if server==winner:
            if winner=='A':
                alice_score+=1
            else:
                bob_score+=1
        else:
            if server=='A':
                server='B'
            else:
                server='A'
    print(alice_score,bob_score)
    t -= 1
