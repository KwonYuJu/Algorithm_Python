def is_palindrome(num):
    str_num = str(num)
    return str_num == str_num[::-1]

while True:
    num = input()
    if num == '0':
        break
    if is_palindrome(num):
        print('yes')
    else:
        print('no')