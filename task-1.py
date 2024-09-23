def roman_to_integer(roman: str) -> int:
    roman_digits = [('M', 1000), ('D', 500), ('C', 100), ('L', 50), ('X', 10), ('V', 5), ('I', 1)]

    value_map = dict(roman_digits)

    length = len(roman)
    result = 0

    for index in range(length - 1, -1, -1):
        current_value = value_map[roman[index]]
        if index < length - 1 and current_value < value_map[roman[index + 1]]:
            result -= current_value
        else:
            result += current_value

    return result

print(roman_to_integer("MCMXCIV"))  
print(roman_to_integer("LVIII"))    
print(roman_to_integer("IX"))       
