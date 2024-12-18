from matplotlib import pyplot as plt
from curves import LossCurve, AccuracyCurve
from info import ModelInfo

class Metrics:
    '''
    Description: This displays the metrics provided by the user
    author: Abhishek Prajapati
    created_on: 18-12-2024
    '''
    def __init__(self, *args):
        self.args = args
        self.fig, (self.ax1, self.ax2) = plt.subplots(1, 2, figsize=(20, 4))
        plt.subplots_adjust(left=0.2, right=0.6, bottom=0.2, top=0.8)

    def display(self):
        '''
        Description: Displays the plots based on the metrics provided by the user.
                     Currently it supports loss and accuracy curves and model summary.
        author: Abhishek Prajapati
        created_on: 18-12-2024
        '''
        for arg in self.args:
            if isinstance(arg, LossCurve):
                self.ax1.set_xlabel('Epoch')
                self.ax1.set_ylabel('Loss', color='tab:red')
                self.ax1.plot(range(1, arg.epochs+1), arg.get(), color='tab:red', label='Training Loss')
                self.ax1.tick_params(axis='y', labelcolor='tab:red')
            if isinstance(arg, AccuracyCurve):
                ax2 = self.ax1.twinx()  
                ax2.set_ylabel('Accuracy', color='tab:blue')  
                ax2.plot(range(1, arg.epochs+1), arg.get(), color='tab:blue', label='Training Accuracy')
                ax2.tick_params(axis='y', labelcolor='tab:blue')
            if isinstance(arg, ModelInfo): 
                self.ax2.set_title("Model Info")
                self.ax2.axis('off')
                self.ax2.set_facecolor('white')
                self.ax2.text(0.5, 0.5, str(arg.get()), ha='left', va='center', fontsize=8, wrap=True)
        # Title and display the legend
        plt.title('Metrics')
        self.fig.tight_layout()  # Adjust the layout to prevent overlap
        plt.show()