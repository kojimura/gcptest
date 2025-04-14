#!/bin/bash

LINES=${1:-300}
OUTFILE="data.txt"

> "$OUTFILE"

for i in $(seq 1 $LINES); do
  ID=$(printf "%05d" "$i")
  NAME=$(printf "User%-15s" "$i")
  EMAIL="user${i}@example.com"
  EMAIL_PADDED=$(printf "%-30s" "$EMAIL")

  echo "${ID}${NAME}${EMAIL_PADDED}" >> "$OUTFILE"
done

echo "$LINES to $OUTFILE"
