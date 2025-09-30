A = 3144
if A & (1 << 3):
    print("The 3rd bit is set")
else:
    print("The 3rd bit is unset")

if A & (1 << 0):
    print("The 0th bit is set")
else:
    print("The 0th bit is unset")

C = A | (1 << 0)
print("After setting the 0th bit in A:", C)

D = A ^ (1 << 3)
print("After flipping the 3rd bit in A:", D)
