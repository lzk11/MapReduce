#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
import os
import sys
def mapper():
    filepath = os.environ["map_input_file"]    # 获取多个文件
    filename = os.path.split(filepath)[-1]
    for line in sys.stdin:
        if line.strip() == "":         # 输入为NUL不处理
            continue
        fields = line[:-1].split()
        job_id = fields[0]
        if filename == 'jobsubmit.20090515':     # 判断文件名字
            submit_time = fields[1]
            user = fields[2]
            print ' '.join((job_id, '0', submit_time, user))    # 给记录添加标签‘0’
        elif filename == 'jobfinish.20090515':
            finish_time = fields[1]
            job_status = fields[2]
            input_size = fields[3]
            midoutput_size = fields[4]
            output_size = fields[5]
            print ' '.join((job_id, '1', finish_time, job_status, input_size, midoutput_size, output_size))   # 给记录添加标签‘1’

if __name__=='__main__':
    mapper()
