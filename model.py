from roboflow import Roboflow

rf = Roboflow(api_key="gjujWflgfLCs7D2Xq3Z3")
project = rf.workspace().project("aicook-lcv4d")
model = project.version(3).model

# infer on a local image

#return a list of the ingredigent as list
def predictions(image):
    prediction_raw=model.predict(image, confidence=40, overlap=30).json()
    list_pred = prediction_raw.get('predictions')
    ingredients = []
    for i in list_pred:
        ingredients.append(i.get("class"))

    return ingredients

#print(predictions('istockphoto-1094166778-612x612.jpg'))

