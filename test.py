
def getcode(a):
    if a == 1:
        x = 35
        y = 35
        code = str(x) + ',' + str(y)
        print(code)
    elif a in (2,3,4):
        x = 35 + (a-1)*70
        y = 35
        code = str(x) + ',' + str(y)
        print(code)
    elif a == 5:
        x = 35
        y = 35 + 70
        code = str(x) + ',' + str(y)
        print(code)
    else:
        x = x = 35 + (a-1)*70
        y = 35 + 70
        code = str(x) + ',' + str(y)
        print(code)

    return code



# codes = []
# for i in range(8):
#     code = getcode(i+1)
#     codes.append(code)
#
# print(codes)

# codestr = input('请输入坐标: ')
# codelist = codestr.split(',')
# codes = []
# for i in codelist:
#     code = getcode(int(i))
#     codes.append(code)
#     pass
# print(codes)
#
# code = ''
# for i in codes:
#     code = code + ',' + i
#     pass
#
# print(code[1:])
