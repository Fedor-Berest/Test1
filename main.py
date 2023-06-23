# s = 'abcbabcbb'
# syms_counter = {}
# for sym in s:
#     syms_counter[sym] = syms_counter.get(sym, 0) + 1
#
# print(syms_counter)
#
# print('hello!')
#
#
# print('changes')


#1 способ, но как я понял так нельзя
def check_palindrom(str):
    return str == ''.join(reversed(str))


print(check_palindrom('aboba'))


#2 способ может быть так тоже нельзя
def check_palindrom(str):
    return str == str[::-1]

print(check_palindrom('aba'))


#3 способ
def check_palindrom(str):
    for a in range(len(str)):
        if str[a] != str[-a - 1]:
            return False

    return True
print(check_palindrom('abba'))

print('aaa')