import urllib.parse

def train_info(trains_list):
    """
    解析列车信息列表, 返回列车信息列表
    """
    trains_infos_list = []

    if trains_list == []:
        return []

    for train_info in trains_list:
        train_info_list = train_info.split('|')
        train_info_dict = {}
        # 构造列车信息
        train_info_dict['secretStr'] = urllib.parse.unquote(train_info_list[0])  # secretStr ;为''时无法购买车票
        # train_info_list[1]  预定/列车停运
        train_info_dict['train_no'] = urllib.parse.unquote(train_info_list[2])  # train_no
        train_info_dict['stationTrainCode'] = urllib.parse.unquote(train_info_list[3])  # stationTrainCode 即车次 # 展示
        train_info_dict['start_station'] = urllib.parse.unquote(train_info_list[4])  # 始发站 # 展示
        train_info_dict['end_station'] = urllib.parse.unquote(train_info_list[5])  # 终点站 # 展示
        train_info_dict['from_station'] = urllib.parse.unquote(train_info_list[6])  # 出发站 # 展示
        train_info_dict['to_station'] = urllib.parse.unquote(train_info_list[7])  # 到达站 # 展示
        train_info_dict['from_time'] = urllib.parse.unquote(train_info_list[8])  # 出发时间 # 展示
        train_info_dict['to_time'] = urllib.parse.unquote(train_info_list[9])  # 到达时间 # 展示
        train_info_dict['use_time'] = urllib.parse.unquote(train_info_list[10])  # 时长 # 展示
        train_info_dict['buy_able'] = urllib.parse.unquote(train_info_list[11])  # 能否购买 Y 可以购买 N 不可以购买 IS_TIME_NOT_BUY 停运 # 展示
        train_info_dict['leftTicket'] = urllib.parse.unquote(train_info_list[12])  # leftTicket
        train_info_dict['start_time'] = urllib.parse.unquote(train_info_list[13])  # 车次始发日期 # 展示
        train_info_dict['train_location'] = urllib.parse.unquote(train_info_list[15])  # train_location 不知道是啥??
        train_info_dict['from_station_no'] = urllib.parse.unquote(train_info_list[16])  # 出发站编号
        train_info_dict['to_station_no'] = urllib.parse.unquote(train_info_list[17])  # 到达站编号
        # 14,18,19,20,27,34,35未知
        train_info_dict['gaojiruanwo'] = urllib.parse.unquote(train_info_list[21])  # 高级软卧 # 展示
        train_info_dict['qita'] = urllib.parse.unquote(train_info_list[22])  # 其他 # 展示
        train_info_dict['ruanwo'] = urllib.parse.unquote(train_info_list[23])  # 软卧 # 展示
        train_info_dict['ruanzuo'] = urllib.parse.unquote(train_info_list[24])  # 软座 # 展示
        train_info_dict['tedengzuo'] = urllib.parse.unquote(train_info_list[25])  # 特等座 # 展示
        train_info_dict['wuzuo'] = urllib.parse.unquote(train_info_list[26])  # 无座 # 展示
        train_info_dict['yingwo'] = urllib.parse.unquote(train_info_list[28])  # 硬卧 # 展示
        train_info_dict['yingzuo'] = urllib.parse.unquote(train_info_list[29])  # 硬座 # 展示
        train_info_dict['erdengzuo'] = urllib.parse.unquote(train_info_list[30])  # 二等座 # 展示
        train_info_dict['yidengzuo'] = urllib.parse.unquote(train_info_list[31])  # 一等座 # 展示
        train_info_dict['shangwuzuo'] = urllib.parse.unquote(train_info_list[32])  # 商务座 # 展示
        train_info_dict['dongwo'] = urllib.parse.unquote(train_info_list[33])  # 动卧 # 展示
        trains_infos_list.append(train_info_dict)

    return trains_infos_list
