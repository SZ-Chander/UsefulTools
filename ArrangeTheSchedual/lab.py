import time

NowTime = time.localtime()
filename = "{}-{}-{}-{}导出表".format(NowTime.tm_year,NowTime.tm_mon,NowTime.tm_mday,NowTime.tm_min)
print(filename)
