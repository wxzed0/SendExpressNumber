from wxauto import *

# 获取当前微信客户端
wx = WeChat()

# 获取会话列表
wx.GetSessionList()

# wx.Search("wxzed-下单美瞳xxx-地址 xxx-电话 xxxx-运单号 100032")

EXPRESS_REGULAR_LIST = ['^[a-zA-Z0-9]{10}$|^(42|16)[0-9]{8}$|^A[0-9]{12}$|^ZJS[0-9]{12}$', '^[A-Za-z0-9]{4,35}$',
                        '^[A-Za-z0-9]{12,15}$', '^[0-9]{12,15}$', '^[A-Za-z0-9]{11,20}$',
                        '^[A-Za-z0-9]{11,20}$|^[0-9]{11,20}$', '^[A-Za-z0-9]{11,13}$|^[0-9]{11,13}$', '^[0-9]{12,15}$',
                        '^((A|B|D|E)[0-9]{12})$|^(BXA[0-9]{10})$|^(K8[0-9]{11})$|^(02[0-9]{11})$|^(000[0-9]{10})$|^(C0000[0-9]{8})$|^((21|22|23|24|25|26|27|28|29|30|31|32|33|34|35|36|37|38|39|61|63)[0-9]{10})$|^((50|51)[0-9]{12})$|^7[0-9]{13}$|^6[0-9]{13}$|^58[0-9]{14}$',
                        '^(YT)[0-9]{12,15}$|^[0-9]{10,15}$',
                        '(66|77|88|(5(5|6|8)))\\d{10}|(99(5|8))\\d{9}|TT(66|88|99|(5(6|7)))\\d{11}',
                        '^[0-6|9][0-9]{11}$|^[7][0-8][0-9]{10}$|^[0-9]{15}$|^[S][0-9]{9,11}(-|)P[0-9]{1,2}$|^[0-9]{13}$|^[8][0,2-9][0,2-9][0-9]{9}$|^[8][1][0,2-9][0-9]{9}$|^[8][0,2-9][0-9]{10}$|^[8][1][1][0][8][9][0-9]{6}$',
                        '^[A-Z]{2}[0-9]{9}[A-Z]{2}$|^(10|11)[0-9]{11}$|^(50|51)[0-9]{11}$|^(95|97)[0-9]{11}$',
                        '^VIP[0-9]{9}|V[0-9]{11}|[0-9]{12}$|^LBX[0-9]{15}-[2-9AZ]{1}-[1-9A-Z]{1}$|^(9001)[0-9]{8}$',
                        '^[0-9]{8,10}$|^\\d{15,}[-\\d]+$', '^(SUR)[0-9]{12}$|^[0-9]{12}$', '^[0-9]{12}$',
                        '^[A-Za-z0-9]*[0|2|4|6|8]$', '^\\d{12}|\\d{11}$', '^[A-Za-z0-9]{8,9}$', '^[0-9]{11,12}$',
                        '^[0-9]{12}$|^LBX[0-9]{15}-[2-9AZ]{1}-[1-9A-Z]{1}$|^[0-9]{15}$|^[0-9]{15}-[1-9A-Z]{1}-[1-9A-Z]{1}$',
                        '^[0-9]{8}$|^[0-9]{10}$', '^[0-9]{12}$|^[0-9]{14}$|^[0-9]{15}$',
                        '^(3(([0-6]|[8-9])\\d{8})|((2|4|5|6)\\d{9})|(7(?![0|1|2|3|4|5|7|8|9])\\d{9})|(8(?![2-9])\\d{9})|(2|4)\\d{11})$',
                        '^(?!440)(?!510)(?!520)(?!5231)([0-9]{9,13})$|^(P330[0-9]{8})$|^(D[0-9]{11})$|^(319)[0-9]{11}$|^(56)[0-9]{10}$|^(536)[0-9]{9}$',
                        '^((88|)[0-9]{10})$|^((1|2|3|5|)[0-9]{9})$|^(90000[0-9]{7})$', '^[\\x21-\\x7e]{1,100}$',
                        '^130[0-9]{9}|13[7-9]{1}[0-9]{9}|18[8-9]{1}[0-9]{9}$', '^[a-zA-Z]{2}[0-9]{9}[a-zA-Z]{2}$',
                        '^[A-Za-z0-9]{13}$|^[0-9]{11,13}$', '^[0-9]{8,10}$|^\\d{15,}[-\\d]+$', '^[0-9]{12}$',
                        '^[0-9]{9,12}$', '[0-9a-zA-Z-]{5,20}', '^[0-9]{12,13}$']


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
