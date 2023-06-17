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


