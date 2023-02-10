import json
import argparse


def mainFunction(arg):
    try:
        path = arg.path
        keysStr = arg.keys
        dataKey = arg.d
        anserList = []

        with open(path) as txt_r:
            txt = txt_r.read()
        jsonData = json.loads(txt)
        dataList = jsonData[dataKey]
        if(keysStr == None):
            keys = list(dataList[0].keys())
        else:
            keys = keysStr.split(',')


        for line in dataList:
            lineData = []
            for key in keys:
                lineData.append(line[key])
            anserList.append("$".join(lineData))

        listRow = anserList
        listChecked = list(set(anserList))
        if (len(listRow) == len(listChecked)):
            retStr = "输入数据在唯一约束为\n{}\n的情况下，数据无重复".format(",".join(keys))

        else:
            times = len(listRow) - len(listChecked)
            retStr = "输入数据在唯一约束为\n{}\n的情况下，检查到重复数据 {} 条".format(",".join(keys),times)

        print(retStr)


    except:
        print("运行错误，请检查参数格式是否正确")



if __name__ == '__main__':
    print("欢迎使用重复查找器")

    parse = argparse.ArgumentParser()
    parse.add_argument('--path',default=None)
    parse.add_argument('--keys',default=None)
    parse.add_argument('--d',default='data')

    arg = parse.parse_args()

    mainFunction(arg)
