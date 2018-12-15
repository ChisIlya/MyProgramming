def repeat(n):
    def decorator(genuine_function):  
        def fake_function(argument):  
            result = argument 
            for number in range(n):
                result = genuine_function(result)
            return result  
        return fake_function  
    return decorator

@repeat(2)
def plus_1(x):
    return x + 1


@repeat(0)
def mul_2(x):
    return x * 2

print(plus_1(3))  
print(mul_2(4))  
