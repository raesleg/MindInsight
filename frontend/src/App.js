import './App.css';
import { useState, useEffect } from 'react';
import { Recorder } from 'react-voice-recorder';
import 'react-voice-recorder/dist/index.css';
import axios from 'axios';

// const assemblyApi = axios.create({
//   baseURL: 'https://api.assemblyai.com/v2',
//   headers: {
//     authorization: process.env.REACT_APP_ASSEMBLY_API_KEY,
//     'content-type': 'application/json',
//   },
// });

const initialState = {
  url: null,
  blob: null,
  chunks: null,
  duration: {
    h:0,
    m:0,
    s:0
  },
}

function App() {
  const [audioDetails, setAudioDetails] = useState(initialState);
  const [transcript, setTranscript] = useState({ id: ''});
  const [isLoading, setIsLoading] = useState(false);
  const [file, setFile] = useState(null);
  const [sResults, setSResults] = useState([]);
  const [kResults, setKResults] = useState([]);
  const [plotUrl, setPlotUrl] = useState('');

  const handleAudioStop = (data) => {
    setAudioDetails(data);
  };

  const handleReset = () => {
    setAudioDetails({...initialState});
    setTranscript({ id: ''})
  }

  // const handleAudioUpload = async (audioFile) => {
  //   setIsLoading(true);

  //   const {data: uploadResponse} = await assemblyApi.post('/upload',audioFile);

  //   const {data} = await assemblyApi.post('/transcript', {
  //     audio_url: uploadResponse.upload_url,
  //     sentiment_analysis: true,
  //     entity_detection: true,
  //     iab_categories: true,
  //   });

  //   setTranscript({ id: data.id });
  // }

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) {
      alert('Please select a file.');
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await fetch('http://localhost:5000/data', {
        method: 'POST',
        body: formData,
      });

      if (response.ok) {
        const data = await response.json();
        setTranscript(data.transcript);
        setSResults(data.s_results);
        setKResults(data.k_results);
        setPlotUrl(data.plotUrl);
      } else {
        alert('Error uploading file.');
      }
    } catch (error) {
      console.error('Error:', error);
    }
    console.log("Data:", { transcript, sResults, kResults, plotUrl });

  };

  return (
    <div>
      <div id="uploadContainer">
        <h1>Upload new File</h1>
        <input type="file" onChange={handleFileChange} />
        <br />
        <button onClick={handleUpload}>Transcribe</button>
      </div>

      Display the results only if data is available
      {/* {transcript && (
        <div id="audioContainer" className="right">
          <div id="speechTranscriptContainer">
            <h1>Transcript</h1>
            <p className="resultst">{transcript}</p>
          </div>
          {sResults.length > 0 && (
            <div id="SentimentContainer">
              <h1>Sentiment Analysis Results</h1>
              {sResults.map((result, index) => (
                <p key={index} className="results">{result}</p>
              ))}
            </div>
          )}
          {kResults.length > 0 && (
            <div id="KeywordContainer">
              <h1>Word highlight Results</h1>
              {kResults.map((result, index) => (
                <p key={index} className="results">{result}</p>
              ))}
            </div>
          )}
      </div>
    )}

    {plotUrl && (
      <div id="PlotContainer" className="right">
        <h1 id="plotH1">Audio Waves</h1>
        <img id="plotWave" src={`data:image/png;base64, ${plotUrl}`} width="85%" height="100%" alt="Plot" />
      </div>
    )} */}
  </div>
  );
}

export default App;
