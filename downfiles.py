from urllib import request
from mongodbconn import Mongodbconn
import sys,os


def callbackfunc(blocknum, blocksize, totalsize):
    '''回调函数
    @blocknum: 已经下载的数据块
    @blocksize: 数据块的大小
    @totalsize: 远程文件的大小
    '''
    percent = 100.0 * blocknum * blocksize / totalsize
    if percent > 100:
        percent = 100
    downsize=blocknum * blocksize
    if downsize >= totalsize:
       downsize=totalsize
    s ="%.2f%%"%(percent)+"====>"+"%.2f"%(downsize/1024/1024)+"M/"+"%.2f"%(totalsize/1024/1024)+"M \r"
    sys.stdout.write(s)
    sys.stdout.flush()
    if percent == 100:
        print('')


def down_file(downurl,title):
    title=title
    filename=os.path.basename(title)
    print("开始下载文件",title)
    try:
        request.urlretrieve(downurl, filename, callbackfunc)
    except IOError as e:
        print("exit code:7",e)
    except:
        print("exit code: 5 无法下载该文件:",title,"\ndownurl:")
    print("下载成功 开始记录到数据库")







if __name__=='__main__':
    mg = Mongodbconn()
    picturl = mg.Selectdb()
    for i in picturl:
    # 启动线程下载
        down_file(downurl=i,title=i)