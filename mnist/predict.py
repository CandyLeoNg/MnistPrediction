import PIL.Image
import numpy as np
import torch
from .modelMnist import returnModel
from torchvision import datasets, transforms


def Predict(path):
    # 处理图片
    transform = transforms.Compose({
            transforms.ToTensor(),
            transforms.Normalize((0.1307,), (0.3081,))}
        )

    # 加载图片
    fig = PIL.Image.open(path)
    fig_1 = np.array(fig)
    fig_1 = torch.Tensor(fig_1)
    # fig_1 = transform(fig_1)
    fig_1 = fig_1.reshape(1,1,28,28)

    # 加载模型
    model = returnModel()
    model.load_state_dict(torch.load('./model.pth'))

    # print(mnist)
    # print(mnist(fig_1))
    return torch.argmax(model(fig_1),axis=1).item()
