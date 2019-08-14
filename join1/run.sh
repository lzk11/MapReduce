#!/bin/bash
INPUT_PATH="join1/"
OUTPUT_PATH="join1_result"
hadoop fs -rmr $OUTPUT_PATH
hadoop streaming \
-jobconf mapreduce.job.reduces=2 \
-jobconf num.key.fields.for.partition=1 \
-jobconf stream.num.map.output.key.fields=2 \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner \
-input $INPUT_PATH \
-output $OUTPUT_PATH \
-mapper "python mr.py mapper" \
-reducer "pthon mr.py reducer" \
-file "./mr.py"
