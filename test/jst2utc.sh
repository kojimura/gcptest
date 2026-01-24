#!/bin/bash
# convert JST to UTC

#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: $0 \"YYYY-MM-DD HH:MM\" or \"YYYY/M/D HH:MM\""
    echo "Example: $0 \"2026-01-24 13:30\""
    echo "Example: $0 \"2026/1/24 13:30\""
    exit 1
fi
input=$(echo "$1" | sed 's|/|-|g')
TZ=UTC date -d "$input JST" '+%Y-%m-%d %H:%M:%S %Z'



