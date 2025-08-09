# 实现计算图中的简单层
# 层的实现不中有两个共通的方法：
# 1. forward：前向传播
# 2. backward：反向传播

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
