def square(x):
    if not isinstance(x, (int, float)):
        raise TypeError("引数は整数または浮動小数点数でなければなりません")
    return x ** 2

try:
    print(square(4))         
except TypeError as e:
    print(e)

try:
    print(square(3.5))       
except TypeError as e:
    print(e)

try:
    print(square("文字列")) 
except TypeError as e:
    print(e)

