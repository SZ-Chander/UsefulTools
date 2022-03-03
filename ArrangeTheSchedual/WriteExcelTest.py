import pandas as pd
import openpyxl as opl

def OpenExcel():
    data = {
        "姓名": ["张三", "李四"],
        "性别": ["男", "女"],
        "年龄": [15, 25],
    }
    df = pd.DataFrame(data)
    print(df)


if __name__ == '__main__':
    path = "/Users/szchandler/Desktop/VScodePy/ForMUJI/TestFiles"
    result = pd.DataFrame({'序号': [1, 2, 3], '姓名': ['张三', '李四', '王五']})
    result.to_excel("{}/{}".format(path,'新建.xlsx'),index=False)
    # OpenExcel()
