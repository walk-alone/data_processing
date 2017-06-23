#coding:utf-8
import hashlib
import time
print 'start time:'
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

fileName_old = ['./old/allic.csv','./old/allic_emea.csv','./old/allic_asia.csv']
fileName_new = ['./new/allic.csv','./new/allic_emea.csv','./new/allic_asia.csv']

filePath1_old = fileName_old[2]
filePath1_new = fileName_new[2]

delteFile = './changed/allic_asia_delFile.csv'
addFile = './changed/allic_asia_addFile.csv'

S1_old = set()
dic_Id1_old = {}
S1_new = set()
dic_Id1_new = {}
detele_dataLine_num = []
add_dataLine_num = []

lineNUM_old = 0
file1_old = open(filePath1_old,'r')
for (num,line) in enumerate(file1_old):
    line = line.strip('\n')
    m = hashlib.md5(line)
    md5_value = m.hexdigest()
    if md5_value in S1_old:
        # print 'old_file_repeted_lines:'
        # print num ,dic_Id1_old[md5_value]
        continue
    S1_old.add(md5_value)
    dic_Id1_old[md5_value] = num
    lineNUM_old +=1
print 'old_line_number:%s' % lineNUM_old

lineNUM_new = 0
file1_new = open(filePath1_new,'r')
for (num,line) in enumerate(file1_new):
    line = line.strip('\n')
    m = hashlib.md5(line)
    md5_value = m.hexdigest()
    if md5_value in S1_new:
        # print 'new_file_repeted_lines:'
        # print num ,dic_Id1_new[md5_value]
        continue
    S1_new.add(md5_value)
    dic_Id1_new[md5_value] = num
    lineNUM_new +=1
print 'new_line_number:%s' % lineNUM_new
########################################################
print 'old_Set_lens:%s' % len(S1_old)
print 'new_Set_lens:%s' % len(S1_new)

repeatedSet1 = S1_old & S1_new

print 'repeatedSet1_lens:%s' % len(repeatedSet1)
#print repeatedSet1
# diffSet1 = S1_old - repeatedSet1
# diffSet2 = S1_new - repeatedSet1

for i in repeatedSet1:
    del dic_Id1_old[i]
    del dic_Id1_new[i]

for i in dic_Id1_old.values():
    detele_dataLine_num.append(i)

for i in dic_Id1_new.values():
    add_dataLine_num.append(i)


print 'These lines need to detele.num:(%d)\t %s' % (len(detele_dataLine_num),detele_dataLine_num)
print 'These lines need to add.num:(%d)\t %s' % (len(add_dataLine_num),add_dataLine_num)

####################################################################
with open(delteFile, 'w') as f:
    file1_old = open(filePath1_old, 'r')
    f.write('Manufacturer_Part,Alternate_Part,Description,RoHS_Non_Compliant,NCNR,Obsolete_Part,ECCN,Schedule_B,HTSN,Unspsc,Unspsc_Version,Stock_Location,Stock_Quantity,MOQ,Multi,Manufacturer,Package,Step_Price,Price_Currency,Datasheet_URL,Product_Image_URL,0\n')
    for (num, line) in enumerate(file1_old):
        if num in detele_dataLine_num:
            line = line.strip('\n')
            #if line[-1] != ',':
            f.write(line + ','+str(num) + '\n')
            #else:
                #f.write(line+str(num)+'\n')
            print 'delFile:%s' % num

# with open(addFile, 'w') as f:
#     file1_new = open(filePath1_new, 'r')
#     f.write('Manufacturer_Part,Alternate_Part,Description,RoHS_Non_Compliant,NCNR,Obsolete_Part,ECCN,Schedule_B,HTSN,Unspsc,Unspsc_Version,Stock_Location,Stock_Quantity,MOQ,Multi,Manufacturer,Package,Step_Price,Price_Currency,Datasheet_URL,Product_Image_URL')
#     for (num, line) in enumerate(file1_new):
#         if num in add_dataLine_num:
#             f.write(line)
#             print 'addFile:%s' % num

print 'end time:'
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print 'done'