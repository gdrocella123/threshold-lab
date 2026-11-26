from abc import ABC, abstractmethod

class Model(ABC):
    def __init__(self):
        pass

    @abstractmethod    
    def train(self):
        pass

    @abstractmethod
    def get_confusion_matrix(self, threshold):
        pass