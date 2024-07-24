import pickle


def LoadModel(file_path: str):
    with open(file_path, 'rb') as file:
        LoadModel = pickle.load(file)

        return LoadModel
