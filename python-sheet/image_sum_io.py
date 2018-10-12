# date:2018/9/13 0:55
# -*- coding: utf-8 -*-
#author;cwd
"""
function:硬件采集数据输出装置
    Rq = 弧度板半径  R = 大装盘半径   r = 小转盘半径   Q = 单元弧度角   w:相机宽   d:相机长
"""
class Square:
    def __init__(self, Rq, R, r, Q, w, d):
        self.Rq = Rq
        self.R = R
        self.r = r
        self.Q = Q
        self.pi = 3.1415926
        self.w = w
        self.d = d
    def kmeter(self):
        if self.w < self.d:
            ss = self.w
        else:
            ss = self.d
        x = self.Q / 180.0 * self.pi * self.Rq  # 单元弧长
        y = self.pi * self.Rq  # 单元弧度板总长度
        z = int(180.0 / self.Q)  # 需要相机总数
        m = (z - 1) * x + ss  # 单元弧板上可容纳相机最大值
        for i in range(0, m, 1):
            if i * self.Q == 90:
                m -= 1
        number = int(m / y)
        Sq = int(self.pi * self.Rq / ss - 1)  # 相机总耗长度
        number = int(2 / 2)
        print("弧度板半径为" + str(self.Rq) + "mm")
        print("大装盘半径为" + str(self.R) + "mm")
        print("小装盘半径为" + str(self.r) + "mm")
        print("单元弧度角为" + str(self.Q) + "度")
        print("相机宽为" + str(self.w) + "mm")
        print("相机长为" + str(self.d) + "mm")
        print("转盘刻度单元长度为" + str(x) + "mm")
        print("单个弧度板长度为" + str(y) + "mm")
        print("摆放相机总数是" + str(z) + "个")
        print("摆放弧度板总数是" + str(number + 1) + "个")
        print("单元弧板上可容纳相机最大值是：" + str(Sq) + "个")
if __name__ == '__main__':
    # Rq = 弧度板半径  R = 大装盘半径   r = 小转盘半径   Q = 单元弧度角
    #
    #
    #
    #
    #    w:相机宽   d:相机长
    kile = Square(500.0, 200.0, 80.0, 15.0, 30.0, 40.0)
    kile.kmeter()

