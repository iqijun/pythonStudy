

import pandas

from Spider.FundDetail import writeToCSV
import time
if __name__ == '__main__':
    #writeToCSV 调用它 就可以写入csv文件
    pd=pandas.read_csv("./csvfiles/001112.csv",dtype={'fcode':pandas.np.str_},index_col="fdate"
                       ,parse_dates=['fdate'])


    result=pd[pd['DGR'].notnull()] #DGR一定有值
    result=result[result['DGR'].str.strip('%').astype(pandas.np.float)<0]#取出跌的数据
    grouped=result.groupby(lambda d:d.strftime('%Y-%m')).size()
    print(grouped.sort_values(ascending=False).head(3))

















