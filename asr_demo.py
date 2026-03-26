import whisper

model = whisper.load_model("base")
result = model.transcribe("audio/dubbing.mp3", language="zh")
print(result["text"])

with open("asr_result.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])