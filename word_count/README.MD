利用streaming实现MapReduce，完成词频统计。map reduce 用python编写
====
文件说明
----
    map.py: 对输入进行，输出为[word, 1]的形式
    reduce.py: 对map.py文件的输出作为输入，统计每个单词的数量，最后输出到文件word_count_result
    run.sh: mapreduce运行脚本，需要配置STREAM_JAR_PATH, INPUT_FILE_PATH和OUTPUT_PATH未知的hadoop集群路径
    word: 存储了需要进行统计的单词的数量
执行指令：
----
    chomod +x run.sh
    ./run.sh


