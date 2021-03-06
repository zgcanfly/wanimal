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
    title=title + ".jpg"
    filename=os.path.basename(title)
    print("开始下载文件",downurl,title)
    try:
        request.urlretrieve(downurl, filename, callbackfunc)
    except IOError as e:
        print("exit code:7",e)
    except:
        print("exit code: 5 无法下载该文件:",title,"\ndownurl:")


if __name__=='__main__':
    mg = Mongodbconn()
    for i in mg.col2.find(no_cursor_timeout=True).batch_size(5):
        down_file(downurl=i['picturl'],title=str(i['_id']))