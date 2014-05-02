#!/usr/bin/env python
#encoding:utf-8

#server.py 配置
import datetime
import os,platform

s_time1=datetime.date.today()-datetime.timedelta(days=1)
s_time=datetime.date.strftime(s_time1,'%Y-%m-%d')
s_time2=datetime.date.strftime(s_time1,'%Y%m%d')


#抽取文件、目录列表
#def Judge_Patform():
system_version = platform.system()
if  system_version == 'Windows':
    zip_bk_dir = "D:\\wins\\data"
    zip_file="D:\\wins\\data\\"+s_time2+".zip"
        #服务端日志主目录
    log_dir="D:\\runserver\\"
elif system_version == 'Linux':
    user_home_path =os.path.expanduser('~')
    zip_bk_dir = user_home_path + 'zip_bk_dir/'
    zip_file=user_home_path + '/zip_bk_dir/'+s_time2+'.zip'
        #服务端日志主目录
    log_dir=user_home_path +'/runserver/'


