#! /bin/bash

OUTPUT_PATH="join_result"
INPUT_PATH="join"
hadoop fs -rmr $OUTPUT_PATH
hadoop streaming \
-D mapred.reduce.tasks=1 \
-D mapred.map.tasks=1 \
-D num.key.fields.for.partition=1 \
-D stream.num.map.output.key.fields=2 \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner \
-input $INPUT_PATH \
-output $OUTPUT_PATH \
-mapper "python map.py" \
-reducer "python reduce.py" \
-file "./map.py" \
-file "./reduce.py"


