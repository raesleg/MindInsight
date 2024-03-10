from flask import Flask, render_template, request, redirect, flash, send_file
import os
import uuid
import speech_recognition as sr
import AudioIntelligence
import plotAudio
# import facialAnalysis
import subprocess

UPLOAD_FOLDER = 'files'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/', methods=['GET', 'POST'])
def root():
    transcript = s_results = k_results = plotUrl = ""
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

        # Use ffmpeg to convert MP3 to WAV
        subprocess.run(['ffmpeg', '-i', full_file_name_mp3, full_file_name_wav])

        if os.path.exists(full_file_name_wav):
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile(full_file_name_wav)

            with audioFile as source:
                data = recognizer.record(source)

            transcript = recognizer.recognize_google(data, key=None)
            print(transcript)

        else:
            flash('Error converting file to WAV format')

        AudioIntelligence.audioIntelligence()
        s_results = AudioIntelligence.s_results
        k_results = AudioIntelligence.k_results

        plotUrl = plotAudio.url

    return render_template('Web.html', transcript=transcript, s_results=s_results, k_results=k_results, plotUrl=plotUrl)

@app.route('/audio')
def serve_audio():
    audio_file_path = 'files/TranscribeThis.wav'  # Specify the path to your audio file
    print(audio_file_path)
    return send_file(audio_file_path, mimetype='audio/wav')

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False, threaded=True)


# from flask import Flask, jsonify, render_template, request, redirect, url_for
# import speech_recognition as sr
# import AudioIntelligence
# import plotAudio
# # import facialAnalysis
# from flask_cors import CORS  # Import the CORS module
# from io import BytesIO

# app = Flask(__name__)
# CORS(app)  # Enable CORS for all routes of your Flask app


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

#         if 'audio' not in request.files:
#             return jsonify({"error": "No audio provided"})
        
#         audio_file = request.files['audio']
        
#         if audio_file.filename == '':
#             return jsonify({"error": "No audio selected"})
        
#         # Read the audio file data from memory
#         audio_data = audio_file.read()

#         if "file" not in request.files:
#             return jsonify({"error": "No file provided"})

#         # file = request.files["file"]
#         # if file.filename == "":
#         #     return jsonify({"error": "No file selected"})

#         recognizer = sr.Recognizer()
#         # audioFile = sr.AudioFile(file)
#         audioFile = sr.AudioFile(audio_data)

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

# @app.route('/data', methods=['POST'])
# def audio():
#     transcript = s_results = k_results = plotUrl = ""

#     if 'audio' not in request.files:
#         return jsonify({"error": "No audio provided"})

#     audio_file = request.files['audio']
#     if audio_file.filename == '':
#         return jsonify({"error": "No audio selected"})
    
#     audio_data = audio_file.read()

#     # Create a file-like object from the audio data
#     audio_file_like = BytesIO(audio_data)

#     from pydub import AudioSegment
#     audio = AudioSegment.from_file(audio_file_like, format="wav")

#     recognizer = sr.Recognizer()
#     with sr.AudioFile(audio_file_like) as source:
#         data = recognizer.record(source)

#     transcript = recognizer.recognize_google(data, key=None)
#     print(transcript)

#     AudioIntelligence.audioIntelligence()
#     s_results = AudioIntelligence.s_results
#     k_results = AudioIntelligence.k_results
#     plotUrl = plotAudio.url

#     return jsonify({
#         'transcript': transcript,
#         's_results': s_results,
#         'k_results': k_results,
#         'plotUrl': plotUrl
#     })

# @app.route('/', methods=['GET', 'POST'])
# def audio():
#     #transcript = s_results = k_results = plotUrl = f_results = ""
#     transcript = s_results = k_results = plotUrl = ""
#     if request.method == "POST":
#         print("FORM DATA RECEIVED")

#         if "file" not in request.files: return redirect(request.url)

#         file = request.files["file"]
#         if file.filename == "": return redirect(request.url)
            
#         if file:
#             recognizer = sr.Recognizer()
#             audioFile = sr.AudioFile(file)
#             with audioFile as source:
#                 data = recognizer.record(source)
#             transcript = recognizer.recognize_google(data, key=None)
#             print(transcript)

#         AudioIntelligence.audioIntelligence()
#         s_results = AudioIntelligence.s_results
#         k_results = AudioIntelligence.k_results

#         plotUrl = plotAudio.url

#         # f_results = facialAnalysis.f_results

#     #return render_template('Web.html', transcript=transcript, s_results=s_results, k_results=k_results, plotUrl=plotUrl, f_results=f_results)
#     return render_template('Web.html', transcript=transcript, s_results=s_results, k_results=k_results, plotUrl=plotUrl)


# if __name__ == "__main__":
#     app.run(debug=True, use_reloader=False, threaded=True)

