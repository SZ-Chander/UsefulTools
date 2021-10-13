from AnaData import Ana
import os
from matplotlib import pyplot as plt
plt.rcParams['font.family']=['Songti SC']

def ReadTxt(path):
    with open(path,'r') as txt_r:
        return txt_r.readlines()

def MessPacket2Total(packet):
    totles = []
    nums = []
    for kind in packet:
        datas = packet[kind]
        NumC,NumT = [],[]
        for data in datas:
            m = data.split(':')[-1]
            NumC.append(m.split('/')[0])
            NumT.append(m.split('/')[1])
        NumC = [int(i) for i in NumC]
        NumT = [int(i) for i in NumT]
        nums.append(sum(NumC)/sum(NumT))
    totles.append(sum(nums)/4)
    return nums,totles

def DrawLineChart(Data,Titles):
    colors = ['r', 'g', 'b', 'y','m']
    plt.figure(dpi=1024)
    for n, name in enumerate(Data):
        plt.plot(Titles,Data[name],label=name,color=colors[n])
    plt.legend(loc='best')
    plt.savefig("{}/logs/{}-{}Changes.png".format(os.getcwd(),Titles[0],Titles[-1]))

if __name__ == '__main__':
    log_path = "{}/logs".format(os.getcwd())
    DataBase = {'文字':[], '文法':[], '读解':[], '听解':[],'总分':[]}
    WaitingLogs = ['201007','201307']#需要分析的试卷名
    Num = []
    for log in WaitingLogs:
        txt_path = ("{}/{}/{}.txt".format(log_path,log,log))
        txt = ReadTxt(txt_path)
        TxtMess = Ana(txt).TxT2Arr()
        datas, Totles = MessPacket2Total(TxtMess)
        for n,k in enumerate(DataBase):
            if(len(DataBase) - n < 2):
                DataBase[k].append(Totles)
            else:
                DataBase[k].append(datas[n])
    DrawLineChart(DataBase,WaitingLogs)
    print("折线图绘制完成")