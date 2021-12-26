import cv2



from deepface import DeepFace


def face_exp(photo):

    img = cv2.imread(photo)
    result = DeepFace.analyze(img, actions=['emotion'])
    return result["dominant_emotion"]

def gender_age(photo):
    img = cv2.imread(photo)
    obj = DeepFace.analyze(img, actions=['age', 'gender'])

    return obj['age'], obj['gender']

