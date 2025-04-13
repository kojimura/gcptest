import os
from google.cloud import speech
from google.cloud import storage

def transcribe_audio(data, context):
    file_name = data['name']
    bucket_name = data['bucket']

    if not file_name.endswith(".wav"):
        print(f"Skipped non-wav file: {file_name}")
        return

    gcs_uri = f"gs://{bucket_name}/{file_name}"

    client = speech.SpeechClient()

    audio = speech.RecognitionAudio(uri=gcs_uri)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="ja-JP"
    )

    response = client.recognize(config=config, audio=audio)

    transcription = ''
    for result in response.results:
        transcription += result.alternatives[0].transcript + '\n'

    # Write transcription to GCS
    storage_client = storage.Client()
    output_bucket = storage_client.bucket(bucket_name)
    txt_blob = output_bucket.blob(file_name.replace('.wav', '.txt'))
    txt_blob.upload_from_string(transcription)

    print(f"Transcription saved as {txt_blob.name}")
