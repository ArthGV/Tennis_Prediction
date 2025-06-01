

class ModelPrediction:

    INPUT_SHAPE: int = 2

    def __init__(self, model_path:str):
        self.model = load_model(model_path)

    def predict(self, dict_p_1: dict, dict_p_2: dict, dict_match: dict):
        input = self.build_input(dict_p_1, dict_p_2, dict_match)
        prediction = self.model(input)
        return prediction
    
    def build_input(self, dict_p_1: dict, dict_p_2: dict, dict_match: dict):
        something
        return input
        