from flask import Flask, render_template, request, redirect, url_for
import speech_recognition as sr
import AudioIntelligence
import plotAudio
# import facialAnalysis

app = Flask(__name__)

# @app.route('/')
# def index():
#     # return render_template('index.html')
#     return {"members": ["member1","member2","member3"]}

# if __name__ == "__main__":
#     app.run(debug=True)

@app.route('/', methods=['GET', 'POST'])
def audio():
    #transcript = s_results = k_results = plotUrl = f_results = ""
    transcript = s_results = k_results = plotUrl = ""
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

        plotUrl = plotAudio.url

        # f_results = facialAnalysis.f_results

    #return render_template('Web.html', transcript=transcript, s_results=s_results, k_results=k_results, plotUrl=plotUrl, f_results=f_results)
    return render_template('Web.html', transcript=transcript, s_results=s_results, k_results=k_results, plotUrl=plotUrl)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False, threaded=True)

