import torch
from torch import nn
from torch.nn import functional as F

#实现方法1
net = nn.Sequential(nn.Linear(20, 256), nn.ReLU(), nn.Linear(256, 10))

X = torch.rand(2, 20)
net(X)


#实现方法2 通过继承nn.Module类
class MLP(nn.Module):
    def __init__(self):
        super().__init__()
        self.hidden = nn.Linear(20, 256)
        self.out = nn.Linear(256, 10)

    def forward(self, X):
        X = self.hidden(X)
        X = F.relu(X)
        X = self.out(X)
        return X
net = MLP()
net(X)


#方法3 混合搭配各种组合块
class NestedMLP(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(20, 64), nn.ReLU(),
            nn.Linear(64, 32)
        )
        self.linear = nn.Linear(32, 16)

    def forward(self, X):
        return self.linear(self.net(X))

chimera = nn.Sequential(NestedMLP(), nn.Linear(16, 20))
