
def GetPrediction(model, inputs: list):

    names = {
        0: 'Iris_Setosa',
        1: 'Iris_Versicolour',
        2: 'Iris_Virginica'

    }

    prediction = model.predict([inputs])[0]
    return names[prediction]
