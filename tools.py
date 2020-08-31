
import serial

def Func_Serial_Info():
    # print('串口初始化 Func_Serial_Info')
    #----------------------------
    global serial_port
    port = "COM37" #端口号
    baudrate = 9600

    #组装成串口初始信息
    serial_port = serial.Serial(port,baudrate,timeout=1)#端口控制

#发送数据
def Func_Send_Data(send_data):#send_data为16进制字符串 send_data = 0x1388
    # print('发送指令函数 Func_Send_Data')
    #-----------------------------
    # print('''
    #         ---- Info of Send Data Parameter ----
    #             Send data   : %s
    #             Serial Port : %s
    #             ''' % (send_data , serial_port.port ))
    serial_port.write(send_data)

#获取数据
def Func_Receive_Data():
    # print('获取数据 Function_Receive_Data:')
    #-----------------------------------
    global  recv_string #获取到的数据

    line = serial_port.readline() #读取全部内容
    # print("recv:",len(line),"Type:",type(line),"readline :%s "%line)

    types_transform_string = line.hex() #字节变成字符串,方便处理数据
    # print("Len: ",len(types_transform_string),type(types_transform_string),types_transform_string)
    #----------------------------------------
    #数据名称转换，目的是作为全局变量
    recv_string = types_transform_string
    return types_transform_string

#处理接收数据
def Func_Handle_Recv():
    # print('处理数据 Function_Handle_Recv:')

    #===================================

    handle_data = recv_string #存在全局变量中的从串口读取的数据

    effective_data = handle_data[6:10]
    return effective_data


#功能：2个字节16进制转换成10进制
def Func_HexString_Trans(data_trans):
    print("转换数据格式 Function_HexString_Trans:")
    temp = bin(int(data_trans,16))[2:] #16进制转换为二进制
    # print(temp)
    # print(type(temp))
    temp_d = int(temp,2) #二进制转为10进制
    # print(temp_d)
    return temp_d



# if __name__ == '__main__':
#     print("-----------------------------")
#     print('=\t\t欢迎进入 测试环境 \t\t\t=')
#     print('-----------------------------\n')
#
# #测试Func_HexString_Trans
#     # AT = '1388'
#     # SEND_AT = Func_HexString_Trans(AT)
#     # print(type(SEND_AT))
#     # print("%.3f" % (SEND_AT*0.001))
# #测试发送数据
#     # Func_Serial_Info()
#     # AT = '1388'
#     # SEND_DATA = bytes.fromhex(AT)
#     # Func_Send_Data(SEND_DATA)
#
# #测试接收数据

def get_detail():
    AT_dic={
        "AT1":'0104001A0001100D',  #获取A相电流值报文
        "AT2":'01040014000171CE',  #获取A相电压值
        "AT3":'0104010000013036',  #获取A相电压总谐波含量
        "AT4":'010401030001C036',  #获取A相电压奇次谐波含量
        "AT5":'010401090001E034',  #获取A相电流总谐波含量
        "AT6":'0104011200019033',  #获取A相电流奇次谐波含量
    }
    Func_Serial_Info()   #初始化串口
    while True:
        for key in AT_dic:
            Flag = True  # 标志位，超时为False
            SEND_DATA = bytes.fromhex(AT_dic[key])
            Func_Send_Data(SEND_DATA)
            # start_time = time.time()
            # while Flag:
            recv = Func_Receive_Data()
            print("recv:", recv)
                # cost_time = time.time() - start_time
                # print(time)
                # if cost_time>2.0:
                #     Flag = False
                #     print("获取数据超时！")
            # if len:
            #     continue
            e_recv = Func_Handle_Recv()
            print("e_recv:", e_recv)
            print("hello")
            if key=="AT1":
                result = Func_HexString_Trans(e_recv) * 0.001
                print("A相电流值：%.3f A" % result)
            elif key =="AT2":
                result = Func_HexString_Trans(e_recv) * 0.1
                print("A相电压值：%.1f V" % result)
            elif key == "AT3":
                result = Func_HexString_Trans(e_recv) * 0.01
                print("A相电压总谐波含量：%.2f %%" %result)
            elif key == "AT4":
                result = Func_HexString_Trans(e_recv) * 0.01
                print("A相电压奇次谐波含量：%.2f %%" % result)
            elif key == "AT5":
                result = Func_HexString_Trans(e_recv) * 0.01
                print("A相电流总谐波含量：%.2f %%" % result)
            elif key == "AT6":
                result = Func_HexString_Trans(e_recv) * 0.01
                print("A相电流奇次谐波含量：%.2f %%" % result)







    # AT_dic={
    #     "AT1":'0104001A0001100D',  #获取A相电流值报文
    #     "AT2":'01040014000171CE',  #获取A相电压值
    #     "AT3":'0104010000013036',  #获取A相电压总谐波含量
    #     "AT4":'010401030001C036',  #获取A相电压奇次谐波含量
    #     "AT5":'010401090001E034',  #获取A相电流总谐波含量
    #     "AT6":'0104011200019033',  #获取A相电流奇次谐波含量
    # }
    # Func_Serial_Info()   #初始化串口
    # while True:
    #     for key in AT_dic:
    #         Flag = True  # 标志位，超时为False
    #         SEND_DATA = bytes.fromhex(AT_dic[key])
    #         Func_Send_Data(SEND_DATA)
    #         # start_time = time.time()
    #         # while Flag:
    #         recv = Func_Receive_Data()
    #         print("recv:", recv)
    #             # cost_time = time.time() - start_time
    #             # print(time)
    #             # if cost_time>2.0:
    #             #     Flag = False
    #             #     print("获取数据超时！")
    #         # if len:
    #         #     continue
    #         e_recv = Func_Handle_Recv()
    #         print("e_recv:", e_recv)
    #         print("hello")
    #         if key=="AT1":
    #             result = Func_HexString_Trans(e_recv) * 0.001
    #             print("A相电流值：%.3f A" % result)
    #         elif key =="AT2":
    #             result = Func_HexString_Trans(e_recv) * 0.1
    #             print("A相电压值：%.1f V" % result)
    #         elif key == "AT3":
    #             result = Func_HexString_Trans(e_recv) * 0.01
    #             print("A相电压总谐波含量：%.2f %%" %result)
    #         elif key == "AT4":
    #             result = Func_HexString_Trans(e_recv) * 0.01
    #             print("A相电压奇次谐波含量：%.2f %%" % result)
    #         elif key == "AT5":
    #             result = Func_HexString_Trans(e_recv) * 0.01
    #             print("A相电流总谐波含量：%.2f %%" % result)
    #         elif key == "AT6":
    #             result = Func_HexString_Trans(e_recv) * 0.01
    #             print("A相电流奇次谐波含量：%.2f %%" % result)



    AT_dic={
        "AT1":'0104001A0001100D',  #获取A相电流值报文
        "AT2":'01040014000171CE',  #获取A相电压值
        "AT3":'0104010000013036',  #获取A相电压总谐波含量
        "AT4":'010401030001C036',  #获取A相电压奇次谐波含量
        "AT5":'010401090001E034',  #获取A相电流总谐波含量
        "AT6":'0104011200019033',  #获取A相电流奇次谐波含量
    }
    # Func_Serial_Info()   #初始化串口
    while True:
        for key in AT_dic:
            # Flag = True  # 标志位，超时为False
            # SEND_DATA = bytes.fromhex(AT_dic[key])
            # Func_Send_Data(SEND_DATA)
            # # start_time = time.time()
            # # while Flag:
            # recv = Func_Receive_Data()
            # print("recv:", recv)
            #     # cost_time = time.time() - start_time
            #     # print(time)
            #     # if cost_time>2.0:
            #     #     Flag = False
            #     #     print("获取数据超时！")
            # # if len:
            # #     continue
            # e_recv = Func_Handle_Recv()
            # print("e_recv:", e_recv)
            print("hello")
            if key=="AT1":

                print("A相电流值")
            elif key =="AT2":

                print("A相电压值")
            elif key == "AT3":

                print("A相电压总谐波含量")
            elif key == "AT4":

                print("A相电压奇次谐波含量" )
            elif key == "AT5":

                print("A相电流总谐波含量" )
            elif key == "AT6":

                print("A相电流奇次谐波含量" )
