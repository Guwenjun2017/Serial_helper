import os
import os.path

# UI文件所在的路径
dir = './'

# 列出目录下的所有的UI文件
def listUiFile():
    list = []
    files = os.listdir(dir)
    for filename in files:
        if os.path.splitext(filename)[1] == '.ui':
            list.append(filename)

    return list

# 扩展名为.ui的文件改成扩展名为.py的文件
def transPyFile_to_UiFile(filename):
    return os.path.splitext(filename)[0] + '.py'

# 调用系统命令把.ui文件转换为python文件
def main():
    list = listUiFile()
    for uifile in list:
        pyfile = transPyFile_to_UiFile(uifile)
        cmd = 'pyuic5 -o {pyfile} {uifile}'.format(pyfile=pyfile, uifile=uifile)
        os.system(cmd)

if __name__=="__main__":
    main()

