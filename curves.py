'''
Description: Loss and Accuracy curves can be displayed using the classes present in this module
Author: Abhishek Prajapati
Created On: 18-12-2024
'''
class LossCurve:
    '''
    Description: This displays the loss curve on the plot.
    Author: Abhishek Prajapati
    Created on: 18-12-2024
    '''
    def __init__(self):
        self.losses = []
        self.epochs = 0

    def add(self, loss: float):
        self.epochs += 1
        self.losses.append(loss)

    def get(self):
        return self.losses

class AccuracyCurve:
    '''
    Description: This displays the accuracy curves on the plot
    Author: Abhishek Prajapati
    Created on: 18-12-2024
    '''
    def __init__(self):
        self.accuracy = []
        self.epochs = 0

    def add(self, accuracy: float):
        self.epochs +=1 
        self.accuracy.append(accuracy)

    def get(self):
        return self.accuracy
    
