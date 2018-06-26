#! -*- coding:utf-8 -*-

import sys
import time
import calendar
import math
import matplotlib.pyplot as plt

import tools

from matplotlib.font_manager import FontProperties  
mfont = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)  


def draw_pr(bdate):
    current = time.strftime("%Y.%m.%d")
    cyear = int(current.split(".")[0])
    cmonth = int(current.split(".")[1])

    monthRange = calendar.monthrange(cyear, cmonth)
    monthrange = monthRange[1]

    month_first_day = ".".join([str(cyear), str(cmonth), str(1)])
    month_first_day_delta = tools.cal_days_count(bdate, month_first_day)

    ax = plt.gca()

    xs = [x for x in range(1, monthrange + 1)]
    by = [math.sin(tools.get_body_point(month_first_day_delta + t)) for t in range(0, monthrange)]
    ey = [math.sin(tools.get_emotion_point(month_first_day_delta + t)) for t in range(0, monthrange)]
    iy = [math.sin(tools.get_iq_point(month_first_day_delta + t)) for t in range(0, monthrange)]

    ax.axes.set_xticks(xs)
    plt.plot(xs, by, color='green', label=u'body rhythm')
    plt.plot(xs, ey, color='red', label=u'emotion rhythm')
    plt.plot(xs, iy, color='skyblue', label=u'iq rhythm')

    plt.title(u'生日：{} 当前年月：{}.{} 生理节律'.format(bdate, cyear, cmonth), fontproperties=mfont)
    plt.xlabel(u'日期', fontproperties=mfont)
    plt.ylabel(u'节律指标', fontproperties=mfont)
    
    plt.legend()
    plt.show()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python draw_pr birthday")
    else:
        draw_pr(sys.argv[1])