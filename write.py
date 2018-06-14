f_write = open('lnmp -write.sh','a+',encoding='utf-8')
f_read = open('地址.txt','r+')
try:
    ret_read = f_read.readlines()
    f_write.writelines(ret_read)
    f_write.flush()
    f_write.close()
    f_read.close()
except Exception as e:
    print(e)