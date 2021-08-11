#conding=utf-8
from python_pratise.task.hero import EZ,Jinx,Jenny
class Hero_Factory():
    def Create_Hero(self,hero):            #定义一个创建英雄的方法
        if hero == "jinx":
            return  Jinx()
        elif hero == "ez":
            return EZ()
        #当传入的参数都不符合上面的条件时，报出异常
        else:
            raise Exception("此英雄不在英雄工厂")


hero_factory1=Hero_Factory()     #实例化对象
jinx=hero_factory1.Create_Hero("jinx")          #实例化对象到Hero_Factory的创建英雄的方法才可以返回此英雄，对象才可以调用

jinx.fight("jenny",Jenny.hero_hp,Jenny.hero_power,)

