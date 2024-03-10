// // import { Recorder } from 'react-voice-recorder';
// // import 'react-voice-recorder/dist/index.css';

// import React from "react";
// import { ReactMic } from "react-mic";
// import $ from "jquery";
// import { findDOMNode } from "react-dom";
// import "./App.css";
// import { useState, useEffect } from 'react';
// import axios from 'axios';

// function App() {
//   const [blobURL, setBlobURL] = useState(null);
//   const [record, setRecord] = useState(false);

//   const [transcript, setTranscript] = useState({ id: ''});
//   const [file, setFile] = useState(null);
//   const [sResults, setSResults] = useState([]);
//   const [kResults, setKResults] = useState([]);
//   const [plotUrl, setPlotUrl] = useState('');

//   const startBtnRef = React.useRef(null);
//   const stopBtnRef = React.useRef(null);
//   const processBtnRef = React.useRef(null);

//   const handleDisplayForStart = () => {
//     $(startBtnRef.current).addClass("d-none");
//     $(stopBtnRef.current).removeClass("d-none");
//   };

//   const handleDisplayForStop = () => {
//     $(stopBtnRef.current).addClass("d-none");
//     $(processBtnRef.current).removeClass("d-none");
//   };
//   // const handleDisplayForStart = () => {
//   //   const startBtn = findDOMNode(this.refs.startBtn);
//   //   $(startBtn).addClass("d-none");
//   //   const stopBtn = findDOMNode(this.refs.stopBtn);
//   //   $(stopBtn).removeClass("d-none");
//   // };

//   // const handleDisplayForStop = () => {
//   //   const stopBtn = findDOMNode(this.refs.stopBtn);
//   //   $(stopBtn).addClass("d-none");
//   //   const processBtn = findDOMNode(this.refs.processBtn);
//   //   $(processBtn).removeClass("d-none");
//   // };

//   // constructor(props) {
//   //   super(props);
//   //   this.state = {
//   //     blobURL: null,
//   //     recordedBlob: null,
//   //     record: false,
//   //   };
//   // }

//   // const startRecording = () => {
//   //   this.setState({ record: true });
//   //   this.handleDisplayForStart();
//   // };

//   // const stopRecording = () => {
//   //   this.setState({ record: false });
//   //   this.handleDisplayForStop();
//   // };

//   const startRecording = () => {
//     setRecord(true);
//     handleDisplayForStart();
//   };

//   const stopRecording = () => {
//     setRecord(false);
//     handleDisplayForStop();
//   };

//   const onData = (recordedBlob) => {
//     console.log("chunk of real-time data is: ", recordedBlob);
//   }

//   const onStop = (recordedBlob) => {
//     console.log(recordedBlob.blobURL);
//     const blobURL = recordedBlob.blobURL;
//     this.setState({ blobURL: blobURL });
//     this.onUpload();
//     return recordedBlob.blobURL;
//   };
  
//   const handleFileChange = (event) => {
//     setFile(event.target.files[0]);
//   };

//   const handleUpload = async () => {
//     if (!file) {
//       alert('Please select a file.');
//       return;
//     }

//     const formData = new FormData();
//     formData.append('file', file);

//     try {
//       const response = await fetch('http://localhost:5000/data', {
//         method: 'POST',
//         body: formData,
//       });

//       if (response.ok) {
//         const data = await response.json();
//         setTranscript(data.transcript);
//         setSResults(data.s_results);
//         setKResults(data.k_results);
//         setPlotUrl(data.plotUrl);
//       } else {
//         alert('Error uploading file.');
//       }
//     } catch (error) {
//       console.error('Error:', error);
//     }
//     console.log("Data:", { transcript, sResults, kResults, plotUrl });

//   };

//   return (
//     <div>
//       <div id="uploadContainer">
//       <ReactMic
//         visualSetting="frequencyBars"
//         // mimeType='audio/mp3'
//         record={record}
//         className="d-none"
//         onStop={onStop}
//         onData={onData}
//       />
//       <button
//         ref="startBtn"
//         className="start-btn"
//         onClick={startRecording}
//         type="button"
//       >
//         START
//       </button>
//       <button
//         ref="stopBtn"
//         className="stop-btn concentric-circles d-none"
//         onClick={stopRecording}
//         type="button"
//       >
//         STOP
//       </button>
//       {/* <button
//         ref="processBtn"
//         className="process-btn d-none"
//         onClick={onUpload}
//       >
//         Processing..
//       </button> */}
//       <br />
//       <audio src={blobURL} controls />

//         <h1>Upload new File</h1>
//         <input type="file" onChange={handleFileChange} />
//         <br />
//         <button onClick={handleUpload}>Transcribe</button>
//       </div>

//       Display the results only if data is available


//       {/* {transcript && (
//         <div id="audioContainer" className="right">
//           <div id="speechTranscriptContainer">
//             <h1>Transcript</h1>
//             <p className="resultst">{transcript}</p>
//           </div>
//           {sResults.length > 0 && (
//             <div id="SentimentContainer">
//               <h1>Sentiment Analysis Results</h1>
//               {sResults.map((result, index) => (
//                 <p key={index} className="results">{result}</p>
//               ))}
//             </div>
//           )}
//           {kResults.length > 0 && (
//             <div id="KeywordContainer">
//               <h1>Word highlight Results</h1>
//               {kResults.map((result, index) => (
//                 <p key={index} className="results">{result}</p>
//               ))}
//             </div>
//           )}
//       </div>
//     )}

//     {plotUrl && (
//       <div id="PlotContainer" className="right">
//         <h1 id="plotH1">Audio Waves</h1>
//         <img id="plotWave" src={`data:image/png;base64, ${plotUrl}`} width="85%" height="100%" alt="Plot" />
//       </div>
//     )} */}
//   </div>
//   );
// }

// export default App;

// import React, { useState, useRef } from "react";
// import { ReactMic } from "react-mic";
// import $ from "jquery";
// import { findDOMNode } from "react-dom";
// import "./App.css";
// import axios, { formToJSON } from 'axios';


// // class App extends React.Component {
// function App() {

//   const [blobURL, setBlobURL] = useState(null);
//   const [record, setRecord] = useState(false);
//   const [transcript, setTranscript] = useState({ id: ''});
//   const [sResults, setSResults] = useState([]);
//   const [kResults, setKResults] = useState([]);
//   const [plotUrl, setPlotUrl] = useState('');


//   const startBtnRef = useRef(null);
//   const stopBtnRef = useRef(null);
//   const processBtnRef = useRef(null);
  
//   const handleDisplayForStart = () => {
//     $(startBtnRef.current).addClass("d-none");
//     $(stopBtnRef.current).removeClass("d-none");
//   };

//   const handleDisplayForStop = () => {
//     $(stopBtnRef.current).addClass("d-none");
//     $(processBtnRef.current).removeClass("d-none");
//   };

//   const startRecording = () => {
//     setRecord(true);
//     handleDisplayForStart();
//   };

//   const stopRecording = () => {
//     setRecord(false);
//     handleDisplayForStop();
//   };

//   const onData = (recordedBlob) => {
//     console.log("chunk of real-time data is: ", recordedBlob);
//   };
  
//   const onUpload = async (blob) => {
//   };

//   const onStop = (recordedBlob) => {
//     console.log("Recording stopped");
//     setBlobURL(recordedBlob.blobURL);
//     convertToWav(recordedBlob.blob);
//     console.log(recordedBlob)
//     console.log('2',recordedBlob.url)
//     console.log('3',recordedBlob.blob)
//   };


//   const convertToWav = async (recordedBlob) => {
//     // Create a new Blob object with the recorded data
//     const blob = new Blob([recordedBlob], { type: 'audio/wav' });
//     console.log(blob)
  
//     // Create a new FormData object to send the WAV blob
//     const formData = new FormData();
//     formData.append('audio', blob, 'recorded_audio.wav');
  
//     // Send a POST request to your Flask backend
//     try {
//       const response = await fetch('http://localhost:5000/data', {
//         method: 'POST',
//         body: formData,
//       });

//       console.log(response.body)
  
//       if (response.ok) {
//         const data = await response.json();
//         console.log(data)
//         setTranscript(data.transcript);
//         setSResults(data.s_results);
//         setKResults(data.k_results);
//         setPlotUrl(data.plotUrl);

//         console.log('Audio uploaded successfully!');
//         console.log("Data:", { transcript, sResults, kResults, plotUrl });

//         // Handle success
//       } else {
//         console.error('Error uploading audio:', response.statusText);
//         // Handle error
//       }
//     } catch (error) {
//       console.error('Error uploading audio:', error.message);
//       // Handle error
//     }
//     // console.log("Data:", { transcript, sResults, kResults, plotUrl });

//   };
  
//   return (
//     <div className="App">
//       <ReactMic
//         visualSetting="frequencyBars"
//         record={record}
//         className="d-none"
//         onStop={onStop}
//         onData={onData}
//       />
//       <button
//         ref={startBtnRef}
//         className="start-btn"
//         onClick={startRecording}
//         type="button"
//       >
//         START
//       </button>
//       <button
//         ref={stopBtnRef}
//         className="stop-btn concentric-circles d-none"
//         onClick={stopRecording}
//         type="button"
//       >
//         STOP
//       </button>
//       <button
//         ref={processBtnRef}
//         className="process-btn d-none"
//         onClick={onUpload}
//       >
//         Processing..
//       </button>
//       <br />
//       <audio src={blobURL} controls />
//     </div>
//   );
// }

// export default App;
