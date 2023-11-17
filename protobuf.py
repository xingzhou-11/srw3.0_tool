import crcmod
import json
from enum import Enum
from srw import srw_pb2
from google.protobuf.json_format import MessageToJson


def status_analysis(data):
    json_obj = json.loads(data)
    state = json_obj["status"]["smlState"]
    print(f'机器人状态: {state}')

class event_enum(Enum):
    ACK_EVENT = {'val': 0, 'analysis': 1}
    MOVE_EVENT = {'val': 1, 'analysis': 1}
    END_COMMAND_EVENT = {'val': 2, 'analysis': 1}
    ERROR_EVENT = {'val': 3, 'analysis': 1}
    HEALTH_EVENT = {'val': 4, 'analysis': 1}
    INFO_EVENT = {'val': 5, 'analysis': 1}
    STATUS_EVENT = {'val': 6, 'analysis': status_analysis}
    CONFIG_EVENT = {'val': 7, 'analysis': 1}
    RESET_EVENT = {'val': 8, 'analysis': 1}
    HEART_BEAT_EVENT = {'val': 9, 'analysis': 1}

class zigbee_command:
    def __init__(self):
        self.command_list = []
        self.address = None

    def append_crc(self, data: bytes) -> bytes:
        # 定义 CRC 校验参数
        crc16 = crcmod.predefined.Crc('kermit')
        return data + crc16.new(data).crcValue.to_bytes(2, byteorder='little')

    def send(self, log, client_socket, command_list):
        while True:
            if command_list:
                command = command_list.pop(0)
                command_str = self.append_crc(command.SerializeToString())
                client_socket.sendto(command_str, self.address)
                log.info(f"sent to {self.address[1]}: {command_str.hex()}")
                log.info(MessageToJson(command))

    def recv(self, log, client_socket, event_list):
        event = srw_pb2.Event()
        while True:
            try:
                raw_data, addr = client_socket.recvfrom(1024)
                data = raw_data[:len(raw_data) - 2]
                if self.append_crc(data) != raw_data:
                    log.warning(f"crc failed: {raw_data.hex()}")
                    continue

                event.ParseFromString(data)
                json_obj = MessageToJson(event)
                log.info(f"recv from {addr}: {data.hex()}")
                log.info(json_obj)

                for i in event_list:
                    if event.type == i.value['val']:
                        return i.value['analysis'](json_obj)
            except:
                pass
