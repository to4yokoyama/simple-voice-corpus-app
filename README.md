# 📢 simple-voice-corpus-app

This is a simple Streamlit web app that allows you to record speech audio (WAV) based on a list of text prompts, useful for creating speech corpora.

## ✨ Features

- Reads text prompts from `metadata.csv`
- Records audio from your browser microphone
- Trims silence using FFmpeg
- Saves audio as WAV files into the `wavs/` directory
- Playback support for recorded files

## 🗂 File Structure

```
.
├── app.py              # Main Streamlit app
├── metadata.csv        # Prompt list with filename, text, and optional description
├── wavs/               # Output directory for recorded WAV files
├── requirements.txt    # Python dependencies
└── Dockerfile          # Optional Docker build file
```

## 📋 metadata.csv format

Each line should be:

```
filename.wav|author|lang|Text prompt
```

Example:

```
audio1.wav|john|EN|Hello, how are you?
audio2.wav|john|EN|The weather is nice today.
```

## 🚀 How to Run

### Option 1: Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

### Option 2: Run with Docker

```bash
docker build -t corpus-recorder .
docker run -p 8501:8501 -v $(pwd)/wavs:/app/wavs corpus-recorder
```

---

## 🛠 Dependencies

- `streamlit`
- `pydub`
- `ffmpeg` (installed system-wide or via Docker)
- `streamlit-audiorecorder`

## 📄 License

MIT License
