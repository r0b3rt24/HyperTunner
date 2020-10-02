# This class in charge of talking to engine and scheduling excutor
from HyperParameterContainer import HyperParameterContainer
from StrategyExcutor import StrategyExcutor


class HyperTuner:
    def __init__(self, model, test_loader, train_loader):
        # init the engine
        self.model = model # model here is only a reference to the class
        self.test_loader = test_loader
        self.train_loader = train_loader
        # we should have a better scheduling system here, but for now we use a queue
        self.tasks = []
        self._update_tasks()
        # At here we should talk to the engine, since we don't have the engine, it's empty for now
    
    def _update_tasks(self):
        # This is a fake one, should update the HP from the engine
        basic_strategy = HyperParameterContainer()
        basic_strategy.addHP('lr', 0.05)
        basic_strategy.addHP('momentem', 0.5)
        basic_strategy.addHP('epoch', 1)
        self.tasks.append(basic_strategy)
    
    def tune(self):
        #TODO:
        # train, eval, talk to engin
        exe = StrategyExcutor(self.model, self.train_loader, self.test_loader, self.tasks.pop())
        exe.train()
