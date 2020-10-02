
class HyperParameterContainer:
    def __init__(self):
        # using a dictionary as the container for all the hyperparameters
        self._HyperParameterDict = {}

    def getHP(self, HP):
        if HP in self._HyperParameterDict:
            return self._HyperParameterDict[HP]
        else:
            raise ValueError("Target HyperParameter Not Found")
    
    def setHP(self, HP, newValue):
        if HP in self._HyperParameterDict:
            self._HyperParameterDict[HP] = newValue
        else:
            raise ValueError("Target HyperParameter Not Found")