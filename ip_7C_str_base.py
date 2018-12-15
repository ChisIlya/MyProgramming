def str_base(n, k):
    ls = []
    alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    number_in_k_base = ''
    
    while n > 0:
        n, a = divmod(n, k)
        ls = [a] + ls
        
    for n in range(len(ls)):
        ls[n] = alphabet [ls[n]]
        
    for n in range(len(ls)):
        number_in_k_base = number_in_k_base + ls[n]
        
    return (number_in_k_base)

print(str_base(44027, 36))
