import torch
from torch import nn
import torch.nn.functional as F

class CenterdLayer(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, X):
        return X - X.mean()
layer = CenterdLayer()
layer(torch.FloatTensor([1, 2, 3, 4, 5]))

net = nn.Sequential(nn.Linear(8, 128), nn.ReLU(), CenterdLayer())
Y =net(torch.rand(4, 8))
print(Y.mean())


