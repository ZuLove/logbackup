#! /usr/bin/python
#-*-coding:utf-8 -*-

import zipfile
import os,re
from server_ini import *
from Print_Info import *

def zipfolder():
    empty_dirs = []
    print 'Creating archive %s' %(s_time2+".zip")
    log_dir_len = len(log_dir)-1
    with zipfile.ZipFile(zip_file,'a',zipfile.ZIP_DEFLATED) as zip_obj:
        for root,dirs,files in os.walk(log_dir):
            empty_dirs.extend([os.path.join(root, dir)[log_dir_len:] for dir in dirs if os.listdir(os.path.join(root, dir)) == []])
            for filex in files:
                file_path = os.path.join(root,filex)
                zip_file_path = file_path[log_dir_len:]
                print "\tadding:%s => %s" %(os.path.split(file_path)[-1],zip_file_path)
                zip_obj.write(file_path,zip_file_path)
            for dir in empty_dirs:
                print "\tadding empty filefloder",dir
                zif = zipfile.ZipInfo(dir + os.sep)
                zip_obj.writestr(zif, "")
            empty_dirs =[]

if __name__ == '__main__':
    if not os.path.exists(zip_bk_dir):
        print u"create result Dir:" + zip_bk_dir
        os.makedirs(zip_bk_dir)
    elif not os.path.isdir(zip_bk_dir):
        print u"Permission denied!"
        os.sys.exit(1)
    zipfolder()
    print_info(zip_file)
