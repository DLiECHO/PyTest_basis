import random

def randomListChange(listNum: list, start: int, end: int) -> None:
    '''将数列第一个数随机与后续一个数做交换'''
    ranNum = random.randint(start,end)
    listNum[0] = listNum[ranNum] + listNum[0]
    listNum[ranNum] = listNum[0] - listNum[ranNum]
    listNum[0] = listNum[0] - listNum[ranNum]

bg_color_judge = [1, 1, 1]
bg_color_step = [0.01, 0.03, 0.06]

def colorChange(bg_color: list) -> None:
    # 声明函数中的这两个变量是全局变量
    global bg_color_step, bg_color_judge
    for i in range(3):
        if bg_color_judge[i] == 1:
            bg_color[i] = bg_color[i] + bg_color_step[i]
        else:
            bg_color[i] = bg_color[i] - bg_color_step[i]
        
        # 当某颜色值超出255，则赋值255，且使其后续不再递增，反而递减
        # 三个递增/减值做一次随机顺序变换
        if bg_color[i] > 255:
            bg_color[i] = 255
            bg_color_judge[i] = 0
            randomListChange(bg_color_step, 1, 2)
            # print(bg_color_step)
        
        # 当某颜色值超出255，则赋值255，且使其后续不再递增，反而递减
        # 三个递增/减值做一次随机顺序变换：step[0]随机与[1]或[2]交换
        elif bg_color[i] < 0:
            bg_color[i] = 0
            bg_color_judge[i] = 1
            randomListChange(bg_color_step, 1, 2)
            # print(bg_color_step)