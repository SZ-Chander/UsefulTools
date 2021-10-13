import os
import shutil
from AnaData import Ana
def ReadPart(path):
    with open(path,encoding='utf-8') as txt_r:
        txt = txt_r.readlines()
    classes = []
    for line in txt:
        MessLine = line.replace('\n','').split(':')
        classes.append(MessLine)
    return classes

def GetMess(parts):
    PartTitle = parts[0]
    kinds = parts[1].split(',')
    print("现在输入{}部分成绩".format(PartTitle))
    print("="*30)
    ThisPart = {}
    for part in kinds:
        s_input = input("请输入{}部分成绩，格式为：正确数,总数  ".format(part))
        s = s_input.replace(',','/')
        ThisPart[part] = s
    return PartTitle,(ThisPart)

def WriteLog(Title,Mess):
    WritingPaper = []
    for kind in Mess:
        WritingPaper.append("{}: \n{}\n".format(kind,'+'*15))
        for part in Mess[kind]:
            line = "  {}:{}\n".format(part,Mess[kind][part])
            WritingPaper.append(line)
        WritingPaper.append("{}\n".format("="*30))
    save_dir = "{}/logs/{}".format(os.getcwd(),Title)
    os.mkdir(save_dir)
    TxtPath = "{}/logs/{}/{}.txt".format(os.getcwd(),Title,Title)
    txtw = open(TxtPath,'w')
    for wline in WritingPaper:
        txtw.write(wline)
    txtw.close()
    shutil.copy("{}/logs/parts.txt".format(os.getcwd()),save_dir)
    print("记录已完成")
    return TxtPath, save_dir+'/'

if __name__ == '__main__':
    title = input("请输入试卷时间：")
    TotalMess = {}
    for kind in (ReadPart("{}/logs/parts.txt".format(os.getcwd()))):
        part,mess = GetMess(kind)
        TotalMess[part] = mess
    txt_path, DirPath = WriteLog(title,TotalMess)
    with open(txt_path,encoding='utf-8') as txt_r:
        txt = txt_r.readlines()
    Ana(txt).draw(DirPath, ['r', 'g', 'b', 'y'])