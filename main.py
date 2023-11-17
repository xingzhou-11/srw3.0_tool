import socket
import PySimpleGUI as sg

from LogTool import LogTool
from threading import Thread
from protobuf import zigbee_command, event_enum
from srw.CommandData import CommandData

def check_robot_status(action: zigbee_command, ip, port):
    """Check if the robot is in an error state
    """
    address = (ip, int(port))
    action.address = address

    test_command = CommandData(seq=0)
    test_command.set_status_command()
    action.command_list.append(test_command.get_command())

def robot_advance(client_socket):
    """Move the robot forward
    """
    print('机器人前进')

def robot_retreat(client_socket):
    """Move the robot backward
    """
    pass

def robot_stop(client_socket):
    """Stop the robot
    """
    pass

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(2)

    srw_action = zigbee_command()
    proto_logger = LogTool("proto", "proto.log")

    tsend = Thread(target=srw_action.send, args=[proto_logger.get_logger(), client_socket, srw_action.command_list])
    trecv = Thread(target=srw_action.recv, args=[proto_logger.get_logger(), client_socket, event_enum])
    tsend.daemon = True
    trecv.daemon = True
    tsend.start()
    trecv.start()
    
    # 设置主题 Dark or Light
    sg.theme('Light Green')

    Text_font = ('Consolas', 15)

    layout = [
        [sg.Output(size=(70, 20), font=Text_font)],
        [sg.Text('网关IP地址:', font=Text_font), 
         sg.Input(size=(20, 1), key='ip', default_text='10.0.64.14', font=Text_font), 
         sg.Text('端口号:', font=Text_font), 
         sg.Input(size=(20, 1), key='port', default_text='4008', font=Text_font)
         ],
        [sg.Button('查看机器人状态', font=Text_font), 
         sg.Button('机器人前进', font=Text_font), 
         sg.Button('机器人后退', font=Text_font), 
         sg.Button('机器人停止', font=Text_font), 
         sg.Button('机器人传感器验证', font=Text_font)
         ],
    ]

    # 创造窗口
    window = sg.Window('robot tool', layout)

    # 事件循环并获取输入值
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:     # If user closed window with X or if user clicked "Exit" button then exit
            break
        if event == '查看机器人状态':
            print('查看机器人状态')
            check_robot_status(srw_action, values['ip'], values['port'])
        if event == '机器人前进':
            robot_advance()
        if event == '机器人后退':
            print('机器人后退')
        if event == '机器人停止':
            print('机器人停止')
        if event == '机器人传感器验证':
            print('机器人传感器验证')

    window.close()

if __name__ == '__main__':
    
    
    main()