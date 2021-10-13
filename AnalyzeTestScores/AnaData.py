#-*- coding : utf-8-*-
# coding:unicode_escape
import os
import matplotlib.pyplot as plt
plt.rcParams['font.family']=['Songti SC']

class Ana:
    def __init__(self,txt):
        self.txt = txt
    def TxT2Arr(self):
        paper = ""
        data = {}
        for line in self.txt:
            paper += line
        Pmess = paper.split("="*30)
        del Pmess[-1]
        for part in Pmess:
            mess = part.split('+'*15)
            Ptitle = mess[0].replace(' ','').replace("""\r""","").replace(':','')
            sorce = mess[1].replace(' ','').split('''\n''')
            del sorce[0]
            del sorce[-1]
            data[Ptitle] = sorce
        return data

    def draw(self,path,colors):
        data = self.TxT2Arr()
        x_lines = []
        y_lines = []
        titles = []
        kinds = []
        for kind in data:
            kinds.append(kind)
            topices = data[kind]
            x_line = []
            y_line = []
            title = []
            for topic in topices:
                mess = topic.split(':')
                name = ""
                time = 0
                for w in mess[0]:
                    time+=1
                    name+=w
                    if(time>=2):
                        time = 0
                        name += '''\n'''
                x_line.append(name)
                title.append(mess[1])
                score = int(mess[1].split('/')[0])/int(mess[1].split('/')[1])
                y_line.append(score)
            x_lines.append(x_line)
            y_lines.append(y_line)
            titles.append(title)
        assert (len(x_lines) == len(y_lines))
        plt.figure(dpi=1024)
        for n in range(len(x_lines)):
            x = x_lines[n]
            y = y_lines[n]
            title = titles[n]
            plt.bar(x,y,fc=colors[n],align='center',label=kinds[n].replace('''\n''',''))
            time = 0
            for a, b in zip(x, y):
                plt.text(a, b + 0.005, "{}".format(title[time]), ha='center', va='bottom', fontsize=10)
                time += 1
        plt.legend(loc = 'best')
        plt.title("Question type correct rate")
        plt.xticks(fontsize=6)
        # for a, b in zip(x_line, y_line):
        #     plt.text(a, b + 0.005, "{}".format(titles[time]), ha='center', va='bottom', fontsize=10)
        #     time += 1
        plt.savefig("{}Question type correct rate.png".format(path))

        # plt.show()


if __name__ == "__main__":
    with open("{}/logs/201007/201007.txt".format(os.getcwd()),encoding='utf-8') as txt_r:
        txt = txt_r.readlines()
    Ana(txt).draw("{}/logs/201007".format(os.getcwd()),['r','g','b','y'])