def str_base(n, k):
    ls = []
    alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    str = ''
    
    while n > 0:
        n, a = divmod(n, k)
        ls = [a] + ls
        
    for n in range(len(ls)):
        ls[n] = alphabet [ls[n]]
        
    for n in range(len(ls)):
        str = str + ls[n]
        
    return (str)

print(str_base(44027, 36))