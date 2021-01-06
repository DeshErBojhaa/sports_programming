n = int(input())
ans = [0] * n

print('XOR 1 2')
a_X_b = int(input())

print('AND 1 2')
a_A_b = int(input())

print('XOR 2 3')
b_X_c = int(input())

print('AND 2 3')
b_A_c = int(input()) 

a_X_c = a_X_b ^ b_X_c
print('AND 1 3')
a_A_c = int(input())

X = a_X_b + (2 * a_A_b)
Y = b_X_c + (2 * b_A_c)
Z = a_X_c + (2 * a_A_c)

a = (X + Z - Y) // 2
b = a_X_b ^ a
c = a_X_c ^ a
# print(a_X_b, b_X_c, a_X_c)
# print(a_A_b, b_A_c, a_A_c)

# print(X, Y, Z)
# print(a, b, c)

ans[0] = a
ans[1] = b
ans[2] = c

for i in range(3, n):
    print(f'XOR 1 {i+1}')
    a_X_i = int(input())
    ans[i] = a_X_i ^ a

print('!', *ans)
