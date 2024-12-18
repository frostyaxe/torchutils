from torchinfo import summary

class ModelInfo:

    def __init__(self, model, input_size):
        self.model_info = summary(model,input_size=input_size)

    def get(self):
        return self.model_info