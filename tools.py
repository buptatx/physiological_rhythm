#！ -*- coding:utf-8 -*-

import numpy as np
import datetime


def cal_days_count(bdate, cdate):
    bdate_list = bdate.split(".")
    cdate_list = cdate.split(".")

    total_days = 0

    cda = datetime.datetime(int(cdate_list[0]), int(cdate_list[1]), int(cdate_list[2]))
    bda = datetime.datetime(int(bdate_list[0]), int(bdate_list[1]), int(bdate_list[2]))

    res = (cda - bda)
    return int(str(res).split(" days")[0])


def get_body_point(cdays):
    body_cycle_days = 23
    #return float(cdays % (body_cycle_days + 1)) / body_cycle_days * 2 * np.pi
    return float(cdays % body_cycle_days) / body_cycle_days * 2 * np.pi

def get_emotion_point(cdays):
    emotion_cycle_days = 28
    return float(cdays % emotion_cycle_days) / emotion_cycle_days * 2 * np.pi

def get_iq_point(cdays):
    iq_cycle_days = 33
    return float(cdays % iq_cycle_days + 1) / iq_cycle_days * 2 * np.pi


if __name__ == "__main__":
    delta = cal_days_count("1989.06.20", "2018.06.01")
    print(get_iq_point(delta))
    print(get_iq_point(delta + 1))