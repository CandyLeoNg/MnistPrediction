import torch
from torch.functional import F
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

class Net(torch.nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = torch.nn.Conv2d(1, 10, kernel_size=5)
        self.conv2 = torch.nn.Conv2d(10, 20, kernel_size=5)
        self.pooling = torch.nn.MaxPool2d(2)
        self.fc = torch.nn.Linear(320, 10)

    def forward(self, x):
        batch_size = x.size(0) # batch_size = 32
        x = F.relu(self.pooling(self.conv1(x)))
        x = F.relu(self.pooling(self.conv2(x)))
        x = x.view(batch_size, -1)
        return self.fc(x)

if __name__ == '__main__':
    # 将数据集转换成张量并且归一化
    transform = transforms.Compose({
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))}
    )
    # 下载数据集，download= True表示从网络下载，本文已经下载好了这里设置为False
    train_data = datasets.MNIST(root='./mnist_data', train=True, download=False, transform=transform)
    test_data = datasets.MNIST(root='./mnist_data', train=False, download=False, transform=transform)
    # 构造小批量数据，训练集一般要随机，所以shuffle=True
    train_loader = DataLoader(dataset=train_data, batch_size=32, shuffle=True)
    # 测试集不用shuffle
    test_loader = DataLoader(dataset=test_data, batch_size=32, shuffle=False)

    model = Net()
    criterion = torch.nn.CrossEntropyLoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

    max_acc = 0
    for epoch in range(10):
        running_loss = 0
        for i, data in enumerate(train_loader):
            inputs, label = data
            print(inputs.shape)
            y_predict = model(inputs)
            loss = criterion(y_predict, label)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            running_loss += loss.item()

        # 预测
        correct = 0
        total = 0
        with torch.no_grad():
            for data in test_loader:
                inputs, label = data
                y_pred = model(inputs)
                _, predicted = torch.max(y_pred.data, dim=1)
                total += label.size(0)
                correct += (predicted == label).sum().item()

        print(f'Epoch: {epoch + 1}, ACC on test: {correct / total}')
        if correct>max_acc:
            max_acc = correct
            print("save mnist...")
            torch.save(model.state_dict(), 'model.pth')


