import torch
from torch import nn
from torchsummary import summary

class LeNet(nn.Module):
    def __init__(self):
        super(LeNet,self).__init__()
        self.conv1 = nn.Conv2d(in_channels=1,out_channels=6,kernel_size=5,stride=1,padding=2)
        self.sigmoid = nn.Sigmoid()
        self.pool1 = nn.AvgPool2d(kernel_size=2,stride=2)
        self.conv2 = nn.Conv2d(in_channels=6,out_channels=16,kernel_size=5,stride=1,padding=0)
        self.pool2 = nn.AvgPool2d(kernel_size=2,stride=2)
        self.flatten = nn.Flatten() # 展平多维的输入数据为一维
        self.fc1 = nn.Linear(in_features=400,out_features=120)
        self.fc2 = nn.Linear(in_features=120,out_features=84)
        self.fc3 = nn.Linear(in_features=84,out_features=10)

    def forward(self,x):
        x = self.pool1(self.sigmoid(self.conv1(x)))
        x = self.pool2(self.sigmoid(self.conv2(x)))
        x = self.flatten(x)
        x = self.fc3(self.fc2(self.fc1(x)))
        return x

if __name__ == '__main__':
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(device)

    model = LeNet().to(device)
    print(summary(model, (1,28,28)))