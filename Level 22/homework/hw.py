def string_to_int(data):
    data = data.strip()

    if not data:
        return "invalid Input"

    if data.startswith('-'):
        if data[1:].isdigit():
            return int(data)
        else:
            return "invalid Input"
            
    if data.isdigit():
        return int(data)
    else:
        return "invalid Input"

#შემიწმება:
print(string_to_int("123"))      # შედეგი: 123
print(string_to_int("-456"))     # შედეგი: -456
print(string_to_int("12a3"))     # შედეგი: invalid Input
print(string_to_int("-78!9"))    # შედეგი: invalid Input
print(string_to_int("50.5"))     # შედეგი: invalid Input