"""
2元买瓶酒
2瓶换瓶酒
4盖换瓶酒
10块钱能喝几瓶
"""


def caculate():
    #瓶子
    bottle = 0
    #盖子
    shell = 0
    #现金
    cash = 10
    #酒
    wine = 0
    i = 0
    wine = int(cash / 2)
    bottle = wine
    shell = wine
    print ("第一次花10块钱买",wine,"瓶酒")
    print ("现在共有",bottle,"个瓶子,",shell,"个盖子")
    print ("开始换酒：")
    while 1:
        i += 1
        print ("第",i,"次：")
        if bottle >= 2:
            bottle -= 2
            wine += 1
            bottle += 1
            shell += 1
            print ("-------------用瓶子换--------------")
            print ("用2个瓶子换了1瓶酒，现在共喝了",wine,"瓶酒")
            drinkWine(bottle,shell)
            print ("==================循环分割线===================")
        elif shell >= 4:
            shell -= 4
            shell += 1
            bottle += 1
            wine += 1
            print ("+++++++++++++用盖子换++++++++++++++")
            print ("用4个盖子换了1瓶酒，现在共喝了",wine,"瓶酒")
            drinkWine(bottle,shell)
            print ("==================循环分割线===================")
        else:
            print ("现在共喝了",wine,"瓶酒")
            print ("瓶子和盖子都不够换了，现在有",bottle,"个瓶子",shell,"个盖子")
            break
    

def drinkWine(bottle,shell):
    print ("现在还有",bottle,"个瓶子")
    print ("现在有",shell,"个盖子")
