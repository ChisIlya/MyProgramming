def egcd(a, b):
    x = 1
    y = 0
    x1 = 0
    y1 = 1
    while b>0:
        q = a // b
        t = b
        b = a % b
        a = t
        t = x1
        x1 = x - (x1 * q)
        x = t
        t = y1
        y1 = y - (y1 * q)
        y = t
        
    return (a, x, y)

print(egcd(168, 48))
