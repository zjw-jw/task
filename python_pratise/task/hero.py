#coding=utf-8
#定义一个英雄基类
class HeroBase():
    #类变量，hp,power,类具有的属性
    hero_hp =""
    hero_power = ""
    hero_name=""

    #定义类的方法
    def fight(self,enemy_name,enemy_power,enemy_hp):

        """

        :param enemy_power:   敌人的攻击力 ,
        :param enemy_hp:       敌人的血量
        :return:
        """

        hero_final_hp=self.hero_hp - enemy_power
        enemy_final_hp=enemy_hp - self.hero_power
        if hero_final_hp > enemy_final_hp :
            print(f"{self.hero_name}赢了")
        elif hero_final_hp < enemy_final_hp :
            print(f"{enemy_name}赢了")
        else :
            print("打成平手")
#定义一个EZ英雄继承父类HeroBase的所有属性和方法
class EZ(HeroBase):
    hero_hp = 1100             #父类的属性重写
    hero_power = 190
    hero_name ="EZ"

#定义一个Jinx英雄继承父类HeroBase的所有属性和方法
class Jinx(HeroBase):
    hero_hp = 1000
    hero_power = 210
    hero_name = "Jinx"

class Jenny(HeroBase):
    hero_hp = 1200
    hero_power = 850
    hero_name = "jenny"


# ez=EZ()          #EZ类实例化对象Ez
# jinx=Jinx()       #Jinx类实例化对象Jinx
# ez.fight("Jinx",Jinx.hero_hp,Jinx.hero_power)     #在这里Jinx是敌人  ,引用类的属性






