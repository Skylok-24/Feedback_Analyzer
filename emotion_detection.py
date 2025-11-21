import requests , json

def emotion_detector(text_to_analyse) :
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url=url,json=myobj,headers=headers)
    json_format = json.loads(response.text)
    anger_score =  json_format['emotionPredictions'][0]['emotion']['anger']
    disgust_score = json_format['emotionPredictions'][0]['emotion']['disgust']
    fear_score = json_format['emotionPredictions'][0]['emotion']['fear']
    joy_score = json_format['emotionPredictions'][0]['emotion']['joy']
    sadness_score = json_format['emotionPredictions'][0]['emotion']['sadness']
    dominant_sc = -1.0
    dominant_n = None
    emotion_dict = json_format['emotionPredictions'][0]['emotion']
    for (name,value) in emotion_dict.items() :
        if value > dominant_sc :
            dominant_n = name
            dominant_sc = value

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_n
    }