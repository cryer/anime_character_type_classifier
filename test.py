import torch
import torchvision.transforms as transforms
from torch.autograd import Variable
from model import myModel
from PIL import Image
import numpy as np
from config import Config as cfg

transform = transforms.Compose([
    # transforms.Resize(128),
    transforms.ToTensor()])

dic = {0:"萝莉",1:"御姐",2:"熟女"}

model = myModel().eval()
model.load_state_dict(torch.load(cfg.model_saved_path))
img = Image.open(cfg.test_img)
img.show(img)
img = img.resize((128,128))
img = transform(img).unsqueeze(0)
img = Variable(img)
out = model(img)
print(out)
pred = np.argmax(out.data.numpy())
print("这个妹子是：",dic[pred])




