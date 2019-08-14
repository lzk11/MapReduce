利用streaming实现MapReduce，完成作业提交信息和作业完成信息的join操作
====
文件说明：
----
    jobfinish: 作业完成信息表
    jobsubmit: 作业提交信息表
    run.sh: 执行脚本
    map.py: 分别对jobfinish和jobsubmit的文件内容添加标签1和2
    reduce.py: 按照标签对1和2进行join操作
执行指令：
    chmod +x run.sh
    ./run.sh