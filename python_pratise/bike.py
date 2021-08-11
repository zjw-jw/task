#coding=utf-8

class Bicycle:
    def run(self,miles):
        print(f"脚踩里程数{miles}公里，好累呀！")

class EBicycle(Bicycle):
    volume=10

    def fill_charge(self,vol):
        """

        :param vol: 充电量
        :return:
        """
        self.volume = self.volume + vol
        # print(f"充电之后的电量:{self.volume}")

        pass

    def run2(self,miles):           #电量自动骑行
        vol_mile=self.volume * 10

        if vol_mile >= miles:
            print(f"充电之后骑行的公里数:{vol_mile}公里")
        elif vol_mile < miles:
           by_miles =miles - vol_mile
           print(f"脚踩骑行里程{by_miles}公里")
           print(f"电量骑行里程:{vol_mile}公里")
           self.run(by_miles)   #通过self.  子类调用父类的方法
           # 如果方法重写，还想调用父类的方法
           super().run(by_miles)


Eb =EBicycle()
# Eb.run(1000)
Eb.run2(1000)

# Ee=EBicycle()
# bb=Bicycle()
# bb.run(100)
# Ee.fill_charge(100)
# Ee.run2(1200)
# Ee.run(100)





