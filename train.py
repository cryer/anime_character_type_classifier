import torch
import torch.nn as nn
import torchvision.datasets as dsets
import torchvision.transforms as transforms
from torch.autograd import Variable
from model import myModel
from config import Config as cfg
import matplotlib.pyplot as plt

transform = transforms.Compose([
    # transforms.RandomHorizontalFlip(),
    transforms.ToTensor()])

train_dataset = dsets.ImageFolder(root=cfg.train_path,transform=transform)


train_loader = torch.utils.data.DataLoader(dataset=train_dataset,
                                           batch_size=cfg.batch_size,
                                           num_workers=cfg.num_workers,
                                           shuffle=cfg.shuffle)

model = myModel()
if cfg.use_gpu:
    model = model.cuda()


criterion = nn.CrossEntropyLoss()
params = list(model.fc1.parameters()) + list(model.fc2.parameters()) + list(model.fc3.parameters())
optimizer = torch.optim.Adam(params, lr=cfg.lr)

if __name__ == '__main__':
    for epoch in range(20):
        for step, (images, labels) in enumerate(train_loader):
            if cfg.use_gpu:
                images = Variable(images).cuda()
                labels = Variable(labels).cuda()

            optimizer.zero_grad()
            output = model(images)
            loss = criterion(output, labels)
            loss.backward()
            optimizer.step()

            if step % 10 ==0:
                print("epoch %s,step %s ,loss %s"%(epoch,step,str(loss.data.cpu())))
        if (epoch+1) % 5 == 0:
            torch.save(model.state_dict(), "checkpoints/anime_%s.pth" % epoch)

torch.save(model.state_dict(), cfg.model_saved_path)


