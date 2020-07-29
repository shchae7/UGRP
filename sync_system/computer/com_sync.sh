#!/usr/bin/bash

while inotifywait -r -e create ./upload
do
    rsync -avz ./upload/ ./download
done
