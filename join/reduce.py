#!/user/bin/python
import sys
def reduce():
    cur_id = None
    for line in sys.stdin:
        line = line.strip().split(' ')
        if cur_id != line[0]:
            cur_id = line[0]
            submit_time = ""
            user = ""
        if cur_id == line[0]:
            if line[1] == '0':
                submit_time = line[2]
                user = line[3]
            if line[1] == '1':
                finish_time = line[2]
                job_status = line[3]
                input_size = line[4]
                midoutput_size = line[5]
                output_size = line[6]
                if submit_time != "":
                    print(' '.join((cur_id, submit_time, user, finish_time, job_status,
                                    input_size, midoutput_size, output_size)))
if __name__ == '__main__':
    reduce()
