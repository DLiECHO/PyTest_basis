import geted

# q = geted.qqq()

# q.pr()

# geted.s = 4

# q.pr()

li = [3]

def cl(lii):
    print('函数内部未修改：',lii)
    lii = [99]
    print('函数内部修改：',lii)

cl(li)

print('最终输出',li)

