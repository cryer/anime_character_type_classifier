import torch
import torch.nn as nn
import torchvision.models as models


class myModel(nn.Module):
    def __init__(self):
        super(myModel, self).__init__()
        resnet = models.resnet50(pretrained=True)
        modules = list(resnet.children())[:-2]
        # print(len(modules))
        self.avgpool = nn.AvgPool2d(4, stride=1)
        self.resnet = nn.Sequential(*modules)
        self.fc1 = nn.Linear(resnet.fc.in_features, 2048)
        self.fc2 = nn.Linear(2048, 512)
        self.fc3 = nn.Linear(512, 3)

    def forward(self, images):
        out = self.resnet(images)
        out = self.avgpool(out)
        out = out.view(out.size(0), -1)
        out = self.fc1(out)
        out = self.fc2(out)
        out = self.fc3(out)
        return out

