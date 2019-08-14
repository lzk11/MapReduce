#!/bin/bash
STREAM_JAR_PATH="/hadoop-client/hadoop/lib/streaming-3.25.0.jar"
INPUT_FILE_PATH="word_count/"
OUTPUT_PATH="word_count_result"
hadoop fs -rmr $OUTPUT_PATH
hadoop streaming \
-jobconf mapreduce.job.reduces=1 \
-input $INPUT_FILE_PATH \
-output $OUTPUT_PATH \
-mapper "python map.py" \
-reducer "python reduce.py" \
-file "./map.py" \
-file "./reduce.py"
