enable API
```
gcloud services enable \
  speech.googleapis.com \
  cloudfunctions.googleapis.com \
  storage.googleapis.com \
  pubsub.googleapis.com
```
resource
```
gsutil mb -l asia-northeast1 gs://sp2txt-169249332871/
mkdir sp2txt && cd sp2txt && touch main.py requirements.txt
```
doding

deply
```
gcloud functions deploy transcribe_audio \
  --runtime python310 \
  --trigger-resource sp2txt-169249332871 \
  --trigger-event google.storage.object.finalize \
  --region asia-northeast1 \
  --entry-point transcribe_audio \
  --memory 512MB \
  --timeout 540s
```
test
```
curl -O https://storage.googleapis.com/cloud-samples-data/speech/brooklyn_bridge.wav
ffmpeg -i brooklyn_bridge.wav -ac 1 -ar 16000 -acodec pcm_s16le output_mono.wav
gsutil cp ./output_mono.wav gs://sp2txt-169249332871/
gsutil ls gs://sp2txt-169249332871/
```
