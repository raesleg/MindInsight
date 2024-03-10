# import json
# import requests
# import pprint
# import base64

# def audioIntelligence():
#     transcriptEndpoint = 'https://api.assemblyai.com/v2/transcript'

#     with open('files/TranscribeThis.wav', 'rb') as audio_file:
#         audio_data = audio_file.read()

#     # Encode the audio data in Base64
#     encoded_audio_data = base64.b64encode(audio_data).decode()

#     response = requests.post(
#         transcriptEndpoint,
#         headers={'authorization': 'e8cce3e8bcc24148b66e9dc9afc22650',
#                  'content-type': 'application/json'},
#         json={
#             # 'audio_url': 'https://storage.googleapis.com/kagglesdsdata/datasets/2453651/4157904/TrancsribeThis.wav?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=databundle-worker-v2%40kaggle-161607.iam.gserviceaccount.com%2F20221005%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20221005T075352Z&X-Goog-Expires=345600&X-Goog-SignedHeaders=host&X-Goog-Signature=100d79669ab5bba3099248f70af4cd05dcfeee638f6dc7a3c5cd88665c9f756d249aa93f0bfefef4f56f98582219e9649c7a563454ba20aae213f07c20119189e984f8ee4439c1e87469c6743254e1b27908fb9d25e0fbf5a0985ccd90e3c42502819295f59956731e8812b396968f9832a52768f4db5c8648e4658a23b477d5d5664e1172d7c4d7ebfd68e1725277eb1ed15c768514b5df354959e905c525687bede8115f7b5fc629367a4ab014b88400fc12c0810a730f9da105ce0123d2150afe819ec0e7eccf59c67fb36052f0a2b3736bb837e6a502ea58cf4958878603f19a692436cecc60b1b4d1582c6f06c867072ff78fa0ef67b544af31ec6acfed',
#             # 'audio_url': 'data:audio/wav;base64,' + encoded_audio_data,
#             'audio_url': 'http://127.0.0.1:5000/audio',
#             'sentiment_analysis': True,
#             'auto_highlights': True
#         },
#     )

#     # transcript_id = response.json()['id']

#     # Check if the request was successful
#     if response.status_code == 200:
#         transcript_id = response.json()['id']
#         return transcript_id
#     else:
#         print(f"Error: {response.status_code} - {response.text}")
#         return None

#     uploadEndpoint = f'https://api.assemblyai.com/v2/transcript/rrpgku2y8z-9885-4e8c-90c2-c53e41061837'

#     response = requests.get(
#         uploadEndpoint,
#         headers={'authorization': 'e8cce3e8bcc24148b66e9dc9afc22650'},
#     )

#     response_json = response.json()
#     #print(pprint.pprint(response_json))

#     global s_results
#     s = response.json()['sentiment_analysis_results']
#     s_results = []
#     for i in s:
#         s_results.append('Text: ' + i['text'])
#         s_results.append('Sentiment: ' + i['sentiment'])
#         s_results.append('Confidence: ' + str(i['confidence']))


#     global k_results
#     k = response.json()['auto_highlights_result']['results']
#     k_results = []
#     for i in k:
#         k_results.append('Word: ' + i['text'])


# audioIntelligence()

import json
import requests
import pprint
import base64

def send_audio_for_transcription():
    transcriptEndpoint = 'https://api.assemblyai.com/v2/transcript'

    response = requests.post(
        transcriptEndpoint,
        headers={'authorization': 'e8cce3e8bcc24148b66e9dc9afc22650',
                 'content-type': 'application/json'},
        json={
            # 'audio_url': 'https://storage.googleapis.com/kagglesdsdata/datasets/2453651/4157904/TrancsribeThis.wav?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=databundle-worker-v2%40kaggle-161607.iam.gserviceaccount.com%2F20221005%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20221005T075352Z&X-Goog-Expires=345600&X-Goog-SignedHeaders=host&X-Goog-Signature=100d79669ab5bba3099248f70af4cd05dcfeee638f6dc7a3c5cd88665c9f756d249aa93f0bfefef4f56f98582219e9649c7a563454ba20aae213f07c20119189e984f8ee4439c1e87469c6743254e1b27908fb9d25e0fbf5a0985ccd90e3c42502819295f59956731e8812b396968f9832a52768f4db5c8648e4658a23b477d5d5664e1172d7c4d7ebfd68e1725277eb1ed15c768514b5df354959e905c525687bede8115f7b5fc629367a4ab014b88400fc12c0810a730f9da105ce0123d2150afe819ec0e7eccf59c67fb36052f0a2b3736bb837e6a502ea58cf4958878603f19a692436cecc60b1b4d1582c6f06c867072ff78fa0ef67b544af31ec6acfed',
            # 'audio_url': encoded_audio_data,
            'audio_url': 'http://127.0.0.1:5000/audio',
            'sentiment_analysis': True,
            'auto_highlights': True
        },
    )

    # transcript_id = response.json()['id']

    # Check if the request was successful
    if response.status_code == 200:
        transcript_id = response.json()['id']
        return transcript_id
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

def get_sentiment_analysis_results():
    uploadEndpoint = f'https://api.assemblyai.com/v2/transcript/rrpgku2y8z-9885-4e8c-90c2-c53e41061837'

    response = requests.get(
        uploadEndpoint,
        headers={'authorization': 'e8cce3e8bcc24148b66e9dc9afc22650'},
    )

    response_json = response.json()
    if response.status_code == 200:
    #print(pprint.pprint(response_json))
        s_results = []
        k_results = []

        sentiment_analysis_results = response.json().get('sentiment_analysis_results', [])
        auto_highlights_results = response.json().get('auto_highlights_result', {}).get('results', [])

        for item in sentiment_analysis_results:
            s_results.append('Text: ' + item['text'])
            s_results.append('Sentiment: ' + item['sentiment'])
            s_results.append('Confidence: ' + str(item['confidence']))

        for item in auto_highlights_results:
            k_results.append('Word: ' + item['text'])

        return s_results, k_results

    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None, None

def audioIntelligence():
    transcript_id = send_audio_for_transcription()
    if transcript_id:
        s_results, k_results = get_sentiment_analysis_results()
        return transcript_id, s_results, k_results
    else:
        return None, None, None

# Call the function
transcript_id, s_results, k_results = audioIntelligence()

# Do something with the results
print("Transcript ID:", transcript_id)
print("Sentiment Analysis Results:", s_results)
print("Auto Highlights Results:", k_results)
