#coding:utf-8
import hashlib
import time
import datetime
import commands
import os
from DataUtils.DataHelp import DataProcess

def main():
    print 'This is python script'
    da = DataProcess('textProcess')
    da.mkDir(DIR_PATH + 'data/changed_' + today)
    fileName_list = da.getDirFiles()
    for i in fileName_list:
        Separator = os.path.splitext(i)[1]
        flag = '|' if Separator == '.txt' else ','
        delteFile = DIR_PATH + 'data/changed_' + today+ '/'+ 'del_File_' + i
        addFile = DIR_PATH + 'data/changed_' + today+ '/'+  'add_File_' + i
        filePath1_old = DIR_PATH + 'data/' + yesterday + '/' + i
        filePath1_new = DIR_PATH + 'data/' + today + '/' + i
        lineNUM_old = 0
        file1_old = open(filePath1_old, 'r')
        for (num, line) in enumerate(file1_old):
            line = line.strip('\n')
            m = hashlib.md5(line)
            md5_value = m.hexdigest()
            if md5_value in da.S1_old:
                # print 'old_file_repeted_lines:'
                # print num ,dic_Id1_old[md5_value]
                continue
            da.S1_old.add(md5_value)
            da.dic_Id1_old[md5_value] = num
            lineNUM_old += 1
        print 'old_line_number:%s' % lineNUM_old

        lineNUM_new = 0
        file1_new = open(filePath1_new, 'r')
        for (num, line) in enumerate(file1_new):
            line = line.strip('\n')
            m = hashlib.md5(line)
            md5_value = m.hexdigest()
            if md5_value in da.S1_new:
                # print 'new_file_repeted_lines:'
                # print num ,dic_Id1_new[md5_value]
                continue
            da.S1_new.add(md5_value)
            da.dic_Id1_new[md5_value] = num
            lineNUM_new += 1
        print 'new_line_number:%s' % lineNUM_new
        print 'old_Set_lens:%s' % len(da.S1_old)
        print 'new_Set_lens:%s' % len(da.S1_new)
        repeatedSet1 = da.S1_old & da.S1_new
        print 'repeatedSet1_lens:%s' % len(repeatedSet1)

        for k in repeatedSet1:
            del da.dic_Id1_old[k]
            del da.dic_Id1_new[k]
        for k in da.dic_Id1_old.values():
            da.detele_dataLine_num.add(k)
        for k in da.dic_Id1_new.values():
            da.add_dataLine_num.add(k)

        print 'These lines need to detele.num:(%d)' % (len(da.detele_dataLine_num))
        print 'These lines need to add.num:(%d)' % (len(da.add_dataLine_num))

        with open(delteFile, 'w') as f:
            file1_old = open(filePath1_old, 'rU')
            for (num, line) in enumerate(file1_old):
                if num == 0:
                    line = line.strip('\n')
                    f.write(line + flag + str(num) + '\n')
                if num in da.detele_dataLine_num:
                    line = line.strip('\n')
                    # if line[-1] != ',':
                    f.write(line + flag + str(num) + '\n')
                    # else:
                    # f.write(line+str(num)+'\n')
                    print 'delFile:%s\r' % num,

        with open(addFile, 'w') as f:
            file1_new = open(filePath1_new, 'rU')
            for (num, line) in enumerate(file1_new):
                if num == 0:
                    f.write(line)
                if num in da.add_dataLine_num:
                    f.write(line)
                    print 'addFile:%s\r' % num,
        print 'file %s process done!!' % i
        da.reset()



if __name__ == '__main__':
    DIR_PATH = '/mnt/data_documentRoot/'
    today = datetime.datetime.now().strftime('%Y%m%d')
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y%m%d')
    print 'start time:'
    print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    flag = ''
    main()
    print 'end time:'
    print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print 'done'