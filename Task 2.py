def int_to_string(n):

    if n == 0:
        return "0"

    result = ""
    negative = False

    if n < 0:
        negative = True
        n = -n

    while n > 0:
        digit = n % 10            
        result += chr(ord('0') + digit)
        n //= 10                    

    result = result[::-1]

    if negative:
        result = "-" + result

    return result



number = int(input("Введіть ціле число: "))
string_number = int_to_string(number)

print("Число:", number)
print("Рядкове представлення:", string_number)