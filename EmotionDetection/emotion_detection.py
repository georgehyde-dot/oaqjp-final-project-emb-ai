import requests
import json

def emotion_detector(text_to_analyse):
    # print(text_to_analyse)
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    body = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = body, headers=headers)
    if response:
        # print(response)
        text_response = json.loads(response.text)
    
    anger_score = text_response['emotionPredictions'][0]['emotion']['anger']
    disgust_score = text_response['emotionPredictions'][0]['emotion']['disgust']
    fear_score = text_response['emotionPredictions'][0]['emotion']['fear']
    joy_score = text_response['emotionPredictions'][0]['emotion']['joy']
    sadness_score = text_response['emotionPredictions'][0]['emotion']['sadness']
    dominant = max(anger_score, disgust_score, fear_score, joy_score, sadness_score)

    scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant
    }
        
    if response.status_code == 400:

        scores =  {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    return scores

def main():
    print(emotion_detector("I hate working long hours."))

if __name__ == "__main__":
    main()