import PySimpleGUI as sg

def check_robot_status():
    """Check if the robot is in an error state
    """
    pass

def robot_advance():
    """Move the robot forward
    """
    print('机器人前进')

def robot_retreat():
    """Move the robot backward
    """
    pass

def robot_stop():
    """Stop the robot
    """
    pass

def main():
    # 设置主题 Dark or Light
    sg.theme('Light Green')

    layout = [  [sg.Output(size=(100, 30))],
                [sg.Button('查看机器人状态'), sg.Button('机器人前进'), sg.Button('机器人后退'), sg.Button('机器人停止'), sg.Button('机器人传感器验证')]
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
            check_robot_status()
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