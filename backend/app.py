from flask import Flask, jsonify, render_template, request, redirect, url_for
import speech_recognition as sr
import AudioIntelligence
import plotAudio
import real_time_video
# import facialAnalysis
from flask_cors import CORS  # Import the CORS module
from flask_socketio import SocketIO, emit

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes of your Flask app
socketio = SocketIO(app)  # Initialize SocketIO

# @app.route('/')
# def index():
#     # return render_template('index.html')
#     return {"members": ["member1","member2","member3"]}

# if __name__ == "__main__":
#     app.run(debug=True)


# @app.route('/data', methods=['GET', 'POST'])
# def audio():
#     transcript = s_results = k_results = plotUrl = ""

#     if request.method == "POST":
#         print("FORM DATA RECEIVED")

#         if "file" not in request.files:
#             return jsonify({"error": "No file provided"})

#         file = request.files["file"]
#         if file.filename == "":
#             return jsonify({"error": "No file selected"})

#         recognizer = sr.Recognizer()
#         audioFile = sr.AudioFile(file)

#         with audioFile as source:
#             data = recognizer.record(source)

#         transcript = recognizer.recognize_google(data, key=None)
#         print(transcript)

#         AudioIntelligence.audioIntelligence()
#         s_results = AudioIntelligence.s_results
#         k_results = AudioIntelligence.k_results
#         plotUrl = plotAudio.url

#     return jsonify({
#         'transcript': transcript,
#         's_results': s_results,
#         'k_results': k_results,
#         'plotUrl': plotUrl
#     })

@app.route('/', methods=['GET', 'POST'])
def audio():
    #transcript = s_results = k_results = plotUrl = f_results = ""
    EMOTIONS = ["angry" ,"disgust","scared", "happy", "sad", "surprised", "neutral"]
    transcript = s_results = k_results = plotUrl = label = emotion_probability =  \
        emotion_probabilities  = base64_frame = canvas = ""
    if request.method == "POST":
        print("FORM DATA RECEIVED")

        if "file" not in request.files: return redirect(request.url)

        file = request.files["file"]
        if file.filename == "": return redirect(request.url)
            
        if file:
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile(file)
            with audioFile as source:
                data = recognizer.record(source)
            transcript = recognizer.recognize_google(data, key=None)
            print(transcript)

        AudioIntelligence.audioIntelligence()
        s_results = AudioIntelligence.s_results
        k_results = AudioIntelligence.k_results
        label, emotion_probability, emotion_probabilities, EMOTIONS = real_time_video.facial_analysis(socketio)
        plotUrl = plotAudio.url

    return render_template('Web.html', transcript=transcript, s_results=s_results, k_results=k_results, plotUrl=plotUrl, base64_frame=base64_frame,
                           label=label, emotion_probability=emotion_probability, emotion_probabilities = emotion_probabilities, EMOTIONS=EMOTIONS, canvas=canvas)


if __name__ == "__main__":
    socketio.run(app, debug=True, use_reloader=False, threaded=True)  # Use SocketIO's run method

