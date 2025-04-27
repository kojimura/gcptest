# Eventrac > Cloud Storage > Cloud Run > upload big file

https://cloud.google.com/run/docs/triggering/storage-triggers?hl=ja#trigger-services

https://zenn.dev/kametani256/articles/297dd96bb9c410


### gen_large_file 

genarate larger file for test

```
{ time ./gen_large_file.sh; } &> time-sh.txt
{ time python3 gen_large_file.py; } &> time-py.txt
```

