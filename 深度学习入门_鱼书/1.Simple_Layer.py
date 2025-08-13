# 实现计算图中的简单层
# 层的实现不中有两个共通的方法：
# 1. forward：前向传播
# 2. backward：反向传播

'''
自己对backward层构建的一些理解
1.首先是定义最终的部分为（∂𝐿/∂z）
2.然后前面的部分为（∂z/∂y）和（∂z/∂x）
3. ∂z/∂y = ∂z/∂x * ∂x/∂y
   ∂z/∂x = ∂z/∂y * ∂y/∂x

__init__中是否要定义self.x和self.y
取决于是否需要在backward中使用前向传播的输入值
'''

import numpy as np


# 乘法层
class MulLayer:
    def __init__(self):
        self.x = None
        self.y = None

    def forward(self,x,y):
        self.x = x
        self.y = y
        out = x * y
        return out

    def backward(self, dout):
        '''
        dout 通常表示该层的输出相对于损失函数的梯度，即∂𝐿/∂𝑦
        '''
        dx = dout * self.y
        dy = dout * self.x
        return dx, dy

# 加法层
class AddLayer:
    def __init__(self):
        '''
        加法层不需要初始化参数，关键在于反向传播时是否需要用到前向传播中的输入值
        '''
        pass

    def forward(self,x,y):
        self.x = x
        self.y = y
        out = x + y
        return out

    def backward(self, dout):
        dx = dout
        dy = dout
        return dx, dy

# ReLU层
class ReLU:
    def __init__(self):
        self.mask = None

    def forward(self,x):
        self.mask = (x <= 0)
        out = x.copy()
        out[self.mask] = 0
        return out
    def backward(self, dout):
        dout[self.mask] = 0
        dx = dout
        return dx

#Affine层
class AffineLayerL:
    def __init__(self, W, b):
        self.W = W
        self.b = b
        self.x = None
        self.dW = None
        self.db = None
    def forward(self, x):
        self.x = x
        out = np.dot(self.x, self.W) + self.b
        return out
    def backward(self, dout):
        self.dW = np.dot(dout, self.x.T)
        self.db = np.sum(dout, axis=0) #每次求和都会消除指定的维度，保留其他维度
        dx = np.dot(dout, self.W.T)
        return dx
