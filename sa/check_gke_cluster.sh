#!/bin/bash

SERVICE_ACCOUNT_KEY="./test-sa.json"
PROJECT_ID="your-project-id"
REGION="us-central1"
CLUSTER_NAME="my-test-cluster"
LOGFILE="./gke_check.log"

ACCESS_TOKEN=$(gcloud auth activate-service-account --key-file="$SERVICE_ACCOUNT_KEY" --quiet > /dev/null && \
               gcloud auth print-access-token)

API_URL="https://container.googleapis.com/v1/projects/${PROJECT_ID}/locations/${REGION}/clusters/${CLUSTER_NAME}"

RESPONSE=$(curl -s -H "Authorization: Bearer ${ACCESS_TOKEN}" "$API_URL")
STATUS=$(echo "$RESPONSE" | jq -r '.status')
TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")
if [ "$STATUS" == "RUNNING" ]; then
  echo "$TIMESTAMP - OK: Cluster is RUNNING" >> "$LOGFILE"
else
  echo "$TIMESTAMP - WARNING: Cluster status is [$STATUS]" >> "$LOGFILE"
  # mail alert ..
fi
