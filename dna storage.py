t = int(input())

while t > 0:
    n = int(input())
    s = input()
    encoded_string=""
    encoding_map={"00":"A","01":"T","10":"C","11":"G"}
    for i in range(0,n,2):
        pair=s[i:i+2]
        encoded_string+=encoding_map[pair]
    print(encoded_string)
    t -= 1
