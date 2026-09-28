#!/bin/sh
# Fetch one Society page image: scripts/plate.sh SLUG PAGE  -> pilots/plates/<slug>_p<PAGE>.jpg
# Uses catalog/plate_offsets.tsv (printed page = leaf - offset). Only calibrated volumes work;
# calibrate a new volume by viewing one leaf and adding a row (never trust _page_numbers.json alone).
cd "$(dirname "$0")/.." || exit 1
row=$(awk -F'\t' -v s="$1" '$1==s' catalog/plate_offsets.tsv)
[ -n "$row" ] || { echo "no calibrated offset for $1" >&2; exit 1; }
item=$(echo "$row" | cut -f2); off=$(echo "$row" | cut -f4)
mkdir -p pilots/plates
curl -sL -o "pilots/plates/${1}_p$2.jpg" "https://archive.org/download/$item/page/n$(( $2 + off )).jpg" && echo "pilots/plates/${1}_p$2.jpg"
