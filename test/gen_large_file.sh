#!/bin/bash

input_file="your_input.csv"
output_file="large_test.csv"
target_size_mb=200

input_buffer=$(cat "$input_file")
[ -z "$input_buffer" ] && echo "Error: '$input_file' empty!" &&  exit 1
input_size_bytes=$(echo -n "$input_buffer" | wc -c)
[ "$input_size_bytes" -eq 0 ] && echo "Error: input file 0 byte!" && exit 1
target_size_bytes=$((target_size_mb * 1024 * 1024))

num_repeats=$((target_size_bytes / input_size_bytes))
remainder_bytes=$((target_size_bytes % input_size_bytes))

echo "input file size: ${input_size_bytes} byte"
echo "target file size: ${target_size_bytes} byte"
echo "repeat: ${num_repeats} times"
echo "remainder: ${remainder_bytes} byte"

for i in $(seq 1 "$num_repeats"); do
  printf "%s" "$input_buffer" >> "$output_file"
done

if [ "$remainder_bytes" -gt 0 ]; then
  head -c "$remainder_bytes" "$input_file" >> "$output_file"
fi

actual_size_bytes=$(stat -c "%s" "$output_file")
actual_size_mb=$(echo "scale=2; $actual_size_bytes / (1024 * 1024)" | bc)
echo "ファイル '$output_file' を ${actual_size_mb} MB genarated"
