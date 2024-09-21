import requests 
import json
def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
    
    if response.status_code == 200:
        emotions = formatted_response["emotionPredictions"][0]["emotion"]
        emotions_list = list(emotions.keys())
        scores_list = list(emotions.values())
        max_score_idx = scores_list.index(max(scores_list))
        dom_emo = emotions_list[max_score_idx]
        emotions['dominant_emotion'] = dom_emo

    elif response.status_code == 400:
        emotions = {'anger': None,
                      'disgust': None,
                      'fear': None,
                      'joy': None,
                      'sadness': None,
                      'dominant_emotion': None
                    }

    return emotions
    
