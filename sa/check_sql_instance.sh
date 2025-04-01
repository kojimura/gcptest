#!/bin/bash

SERVICE_ACCOUNT_KEY="./sakey.json"     # Service Addount key
PROJECT_ID="your-project-id"           # GCP Project ID
INSTANCE_NAME="your-instance-name"     # Cloud SQL instance
LOGFILE="./sql_check.log"              # log file

ACCESS_TOKEN=$(gcloud auth activate-service-account --key-file="$SERVICE_ACCOUNT_KEY" --quiet > /dev/null && \
               gcloud auth print-access-token)

API_URL="https://sqladmin.googleapis.com/sql/v1beta4/projects/${PROJECT_ID}/instances/${INSTANCE_NAME}"
RESPONSE=$(curl -s -H "Authorization: Bearer ${ACCESS_TOKEN}" "${API_URL}")

STATUS=$(echo "$RESPONSE" | grep -oP '"state"\s*:\s*"\K[^"]+')

TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")
if [ "$STATUS" == "RUNNABLE" ]; then
  echo "$TIMESTAMP - OK: Instance is RUNNABLE" >> "$LOGFILE"
else
  echo "$TIMESTAMP - WARNING: Instance state is [$STATUS]" >> "$LOGFILE"
  # mailx notifier
fi
