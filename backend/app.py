from flask import Flask, jsonify, render_template, request, redirect, url_for, Response, redirect, flash, send_file
import os
import uuid
import speech_recognition as sr
import plotAudio
import real_time_video
from camera import VideoCamera
from flask_cors import CORS  # Import the CORS module
from flask_socketio import SocketIO, emit

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes of your Flask app
socketio = SocketIO(app)  # Initialize SocketIO
from transformers import pipeline
import subprocess

import nltk
nltk.download('punkt')  # This downloads necessary NLTK data

UPLOAD_FOLDER = 'files'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

sentiment_pipeline = pipeline("sentiment-analysis", model="finiteautomata/bertweet-base-sentiment-analysis")

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/', methods=['GET', 'POST'])
def root():
    
    EMOTIONS = ["angry" ,"disgust","scared", "happy", "sad", "surprised", "neutral"]
    transcript= sentiment_label = sentiment_rating = plotUrl = label = emotion_probability =  \
        emotion_probabilities  = base64_frame = canvas = ""
    if request.method == "POST":
        if "file" not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        file_name_mp3 = "TranscribeThis.mp3"
        full_file_name_mp3 = os.path.join(app.config['UPLOAD_FOLDER'], file_name_mp3)
        full_file_name_wav = os.path.splitext(full_file_name_mp3)[0] + ".wav"
        file.save(full_file_name_mp3)

        # Use ffmpeg to convert MP3 to WAV, force overwrite existing file
        subprocess.run(['ffmpeg', '-y', '-i', full_file_name_mp3, full_file_name_wav])

        if os.path.exists(full_file_name_wav):
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile(full_file_name_wav)

            with audioFile as source:
                data = recognizer.record(source)

            transcript = recognizer.recognize_google(data, key=None)
            print('text: ',transcript)

            # Split transcript into sentences
            # sentences = nltk.sent_tokenize(transcript)

            # Analyze sentiment for each sentence
            # for sentence in sentences:
            #     results = sentiment_pipeline(sentence)
            #     sentiment_label = results[0]['label']
            #     if sentiment_label == "NEG":
            #         sentiment = "Negative"
            #     elif sentiment_label == "POS":
            #         sentiment = "Positive"
            #     else:
            #         sentiment = "Neutral"
            #     sentiments.append((sentence, sentiment))

            # Analyze sentiment for each sentence
            results = sentiment_pipeline(transcript)
            print(results)
            sentiment_rating = results[0]['score']
            sentiment_label = results[0]['label']
            plotUrl = plotAudio.url
            label, emotion_probability, emotion_probabilities, EMOTIONS = real_time_video.facial_analysis(socketio)

            return jsonify({
                "transcript": transcript,
                "sentiment_label": sentiment_label,
                "sentiment_rating": sentiment_rating,
                "plotUrl": plotUrl
            })

        else:
            flash('Error converting file to WAV format')
        
    return render_template('Web.html', label=label, emotion_probability=emotion_probability, emotion_probabilities = emotion_probabilities, EMOTIONS=EMOTIONS, canvas=canvas)


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

# if __name__ == "__main__":
#     socketio.run(app, debug=True, use_reloader=False, threaded=True)  # Use SocketIO's run method

# @app.route('/audio')
# def serve_audio():
#     audio_file_path = 'files/TranscribeThis.wav'  # Specify the path to your audio file
#     print(audio_file_path)
#     return send_file(audio_file_path, mimetype='audio/wav')

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False, threaded=True)