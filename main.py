from wxauto import *

# 获取当前微信客户端
wx = WeChat()

# 获取会话列表
wx.GetSessionList()

# wx.Search("wxzed-下单美瞳xxx-地址 xxx-电话 xxxx-运单号 100032")

print("====程序开始====")

###############################
# 1、获取默认窗口聊天信息
###############################
# def get_default_window_messages():
#     # 默认是微信窗口当前选中的窗口
#     # 输出当前聊天窗口聊天消息
#     msgs = wx.GetAllMessage
#     for msg in msgs:
#         print('%s : %s' % (msg[0], msg[1]))
#
#     # 获取更多聊天记录
#     wx.LoadMoreMessage()
#     msgs = wx.GetAllMessage
#     for msg in msgs:
#         print('%s : %s' % (msg[0], msg[1]))

GROUP_NAME = "测试群"
DEFAULT_MSG = "售后的话是签收后十五天内 一副售后一只 拿到手记得核对一下有没有发错再拆封哦"
SUDI_KEY_WORDS = "速递"
ORDER_KEY_WORDS = "下单信息"
sudi_msg_list = []
order_msg_list = []
info_dict = {}


###############################
# 1、获取默认窗口聊天信息
###############################
def search_group():
    try:
        wx.ChatWith(GROUP_NAME)
        print("111")

        msgs = wx.GetAllMessage
        print("222")

        while msgs[0][0] == '查看更多消息':
            print("111")
            wx.LoadMoreMessage(1)

            print("111")
        msgs = wx.GetAllMessage
        for msg in msgs:
            if SUDI_KEY_WORDS in msg[1]:
                sudi_msg_list.append(msg[1])
                print("%s", msg[1])

            if ORDER_KEY_WORDS in msg[1]:
                order_msg_list.append(msg[1])


    except Exception as e:
        print("", e)


###############################
# 1、获取默认窗口聊天信息
###############################
def parse_customer(sudi_list=[]):
    try:

        print("333")

        for sudi in sudi_list:
            print("iis %s", sudi)

            sudi_info = sudi.split(' ')

            print("ifis %s", sudi_info)

            name = sudi_info[len(sudi_info) - 1]

            info = Info(name, sudi)
            if info not in info_dict:
                info_dict[info] = False

        return info_dict

    except Exception as e:
        print("", e)

###############################
# 1、获取默认窗口聊天信息
###############################
def parse_information(sudi_list=[]):
    try:

        print("333")

        for sudi in sudi_list:
            print("iis %s", sudi)

            sudi_info = sudi.split(' ')

            print("ifis %s", sudi_info)

            name = sudi_info[len(sudi_info) - 1]

            info = Info(name, sudi)
            if info not in info_dict:
                info_dict[info] = False

        return info_dict

    except Exception as e:
        print("", e)


###############################
# 1、获取默认窗口聊天信息
###############################
def send_sudi(customer_name, sudi_msg):
    try:
        wx.ChatWith(customer_name)
        wx.SendMsg(sudi_msg)
        wx.SendMsg(DEFAULT_MSG)

    except Exception as e:
        print("", e)


class Info():

    def __init__(self, customer_name, sudi_info):
        self.customer_name = customer_name
        self.sudi_info = sudi_info


if __name__ == '__main__':

    search_group()

    send_info_dict = parse_information(sudi_msg_list)

    for info in send_info_dict.keys():

        if not send_info_dict[info]:
            send_sudi(info.customer_name, info.sudi_info)
            send_sudi(info.customer_name, DEFAULT_MSG)
            info_dict[info] = True
