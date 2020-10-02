import torch.nn as nn
import torch.optim as optim


class StrategyExcutor:
    def __init__(self, model, train_loader, test_loader, hyperparams_container):
        self.model = model() # initialize the model here
        self.train_loader = train_loader
        self.test_loader = test_loader
        self.criterion = nn.CrossEntropyLoss()
        self.optimizer = optim.SGD(self.model.parameters(), lr=hyperparams_container.getHP('lr'), momentum=hyperparams_container.getHP('momentem'))
        self.hyperparams_container = hyperparams_container
    
    def training(self):
        for epoch in range(self.hyperparams_container.getHP('epoch')):
            running_loss = 0.0
            for i, data in enumerate(self.train_loader, 0):
                inputs, labels = data
                self.optimizer.zero_grad()
                outputs = self.model(inputs)
                loss = self.criterion(outputs, labels)
                loss.backward()
                self.optimizer.step()
                running_loss += loss.item()
                if i % 2000 == 1999:    # print every 2000 mini-batches
                    print('[%d, %5d] loss: %.3f' %
                        (epoch + 1, i + 1, running_loss / 2000))
                    running_loss = 0.0

    def report(self):
        # test loop
        return None