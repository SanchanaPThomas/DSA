for _ in range(int(input())):
    n=int(input())
    n_str=str(n)
    digit_sum=sum(int(digit) for digit in n_str)
    print(digit_sum)
