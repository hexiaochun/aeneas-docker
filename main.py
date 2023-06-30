from fastapi import FastAPI, UploadFile, File, HTTPException
import tempfile
import os
import subprocess
from typing import List

app = FastAPI()

@app.post("/generate_subtitles/")
async def generate_subtitles(audio: UploadFile = File(...), text: UploadFile = File(...)):
    # Checking if the audio file has .mp3 or .wav extension and text file has .txt extension
    if audio.filename.split('.')[-1] in ['mp3', 'wav'] and text.filename.endswith('.txt'):
        # Create temporary directory
        with tempfile.TemporaryDirectory() as temp_dir:
            audio_file_path = os.path.join(temp_dir, audio.filename)
            text_file_path = os.path.join(temp_dir, text.filename)
            output_srt_path = os.path.join(temp_dir, "output.srt")
            
            # Save received files to temporary directory
            with open(audio_file_path, 'wb+') as audio_file:
                audio_file.write(await audio.read())
            with open(text_file_path, 'wb+') as text_file:
                text_file.write(await text.read())
            
            # Execute the command to generate subtitles
            try:
                subprocess.check_call([
                    "python3", "-m", "aeneas.tools.execute_task",
                    audio_file_path, text_file_path, 
                    "task_language=zho|os_task_file_format=srt|is_text_type=plain",
                    output_srt_path
                ])
            except subprocess.CalledProcessError as e:
                raise HTTPException(status_code=500, detail="Subtitles generation failed.")
            
            # Return the generated subtitle file to the user
            with open(output_srt_path, 'r') as f:
                output_srt = f.read()
            return output_srt
    else:
        raise HTTPException(status_code=422, detail="Invalid input file types. Expected .mp3, .wav for audio and .txt for text")
