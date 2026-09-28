#!/bin/sh
# Re-fetch archive.org OCR text for the Princeton Wyclif Society set (gitignored; ~40 MB).
cd "$(dirname "$0")/.." && mkdir -p sources/ia-ocr
for i in $(seq -w 1 33); do
  id=latinworks${i}wycl
  [ -s sources/ia-ocr/$id.txt ] || curl -sL -o sources/ia-ocr/$id.txt "https://archive.org/download/$id/${id}_djvu.txt"
done
