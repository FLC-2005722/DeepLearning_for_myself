import torch
from torch import nn

#构建单隐藏层的MLP(多层感知机)
#输入层有4个节点，隐藏层有8个节点，输出层有1
net = nn.Sequential(nn.Linear(4, 8), nn.ReLU(), nn.Linear(8, 1))
X = torch.randn(size=(2, 4))
net(X)

#net(2)是最后一层的输出
print(net(2).state_dict())