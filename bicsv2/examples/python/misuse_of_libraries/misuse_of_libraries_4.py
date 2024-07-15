import torch
import torch.nn as nn
import torch.optim as optim

class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.layers = nn.Sequential(
            nn.Linear(10, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, 1),
            nn.Sigmoid()
        )

    def forward(self, x):
        return self.layers(x)

def train_model(epochs):
    model = SimpleNN()
    criterion = nn.BCELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    x_train = torch.randn(1000, 10)
    y_train = torch.randint(0, 2, (1000, 1)).float()
    loss_history = []

    for _ in range(epochs):
        optimizer.grad()
        loss = criterion(model(x_train), y_train)
        loss.backward()
        optimizer.step()
        loss_history.append(loss.item())

    return loss_history
