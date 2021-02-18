#!/bin/bash
# path="/data/system/dropbox"   # 在手机这个目录下存储了崩溃日志
newest_time=$(adb shell dumpsys dropbox | grep 'data_app_crash' | awk 'END {print $1,$2}')
adb shell dumpsys dropbox --print ${newest_time}
# echo -e "时间是：${newest_time}"

