# n → n/2 (n is even)
# n → 3n + 1 (n is odd)


chain = []
f_el = 2  # first el in a chain
call = 0
max_len = 0

while f_el < 1000000:
    
    n = f_el
    while n > 1:
        chain.append(n)
        if n % 2 == 0:
            n /= 2
        else: n = 3*n +1

    if len(chain) > max_len:
        max_len = len(chain)
        call = f_el

    chain.clear()
    f_el += 1
print(f'First element of longest chain = {call}')
print(f'Chain have {max_len} link')
# print(f'Chain = {chain}')