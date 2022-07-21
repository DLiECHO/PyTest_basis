s = 1

class qqq():
    def __init__(self) -> None:
        print('?')
    
    # def pr(self):
    #     print(s)

def cl(li):
    print('函数内部未修改：',li)
    li = [1,2]
    print('函数内部修改：',li)