#coding=utf-8
#类得的定义
class HouseOne:
    #类变量
    door ='red'
    floor ='white'

    def __init__(self):   ##构造函数，类实例化的时候就调用构造函数，常常在构造函数定义一些一开始就需要的饿变量
        #实例变量，在方法内需要加self进行区分，作用域为整个实例对象
        self.Kichen="shining"
        self.bathroom="wide"
        self.sofa="soft"

    def cooking(self):     #方法是实例对象中的函数
        name="Mary"
        print(f"{name}的房子可以超出的，在{self.Kichen}炒菜")
    def sleep(self):
        name = 'Bob'        #name是局部变量
        print(f"{name}的房子可以用来睡觉,在{self.sofa}上面睡觉")

Jick_house=HouseOne()     #类的实例化， 是一个 实例对象
Jick_house.cooking()
Jick_house.sleep()
# HouseOne.door="yellow"         #类的变量是可以修改的
print(HouseOne.door)
Mary_house=HouseOne
print("Jick的房子的门的颜色",Jick_house.door)
print("Mary的房子的门的颜色",Mary_house.door)   #类变量在实例化是公用的
Mary_house.door="bule"
print("Mary_house.door的颜色:",Mary_house.door)     #类变量和实例变量在使用时冲突时，优先使用实例变量







