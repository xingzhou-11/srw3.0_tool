import socket
import crcmod
import time
from enum import Enum
from protobuf import zigbee_pb2
from google.protobuf.json_format import MessageToJson


class event_enum(Enum):
    ACK_EVENT = {'val': 0, 'analysis': 1}
    MOVE_EVENT = {'val': 1, 'analysis': 1}
    END_COMMAND_EVENT = {'val': 2, 'analysis': 1}
    ERROR_EVENT = {'val': 3, 'analysis': 1}
    HEALTH_EVENT = {'val': 4, 'analysis': 1}
    INFO_EVENT = {'val': 5, 'analysis': 1}
    STATUS_EVENT = {'val': 6, 'analysis': 1}
    CONFIG_EVENT = {'val': 7, 'analysis': 1}
    RESET_EVENT = {'val': 8, 'analysis': 1}
    HEART_BEAT_EVENT = {'val': 9, 'analysis': 1}

command_list = []

def append_crc(data: bytes) -> bytes:
    # 定义 CRC 校验参数
    crc16 = crcmod.predefined.Crc('kermit')
    return data + crc16.new(data).crcValue.to_bytes(2, byteorder='little')

def send(log, client_socket, command_list):
    while True:
        if command_list:
            command = command_list.pop(0)
            command_str = append_crc(command.SerializeToString())
            for v in devices.values():
                client_socket.sendto(command_str, (udp_addr, v))
                log.info(f"sent to {v}: {command_str.hex()}")
                log.info(MessageToJson(command))

def recv(log, client_socket, event_list, flag):
    event = zigbee_pb2.Event()
    while True:
        try:
            raw_data, addr = client_socket.recvfrom(1024)
            data = raw_data[:len(raw_data) - 2]
            if append_crc(data) != raw_data:
                log.warning(f"crc failed: {raw_data.hex()}")
                continue

            event.ParseFromString(data)
            json_obj = MessageToJson(event)
            log.info(f"recv from {addr}: {data.hex()}")
            log.info(json_obj)

            for i in event_list:
                if event.type == i.value['val']:
                    i.value['analysis']
        except:
            pass

if __name__ == "__main__":
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(2)

    tsend = Thread(target=send, args=[proto_logger.get_logger(), client_socket, command_list])
    trecv = Thread(target=recv, args=[proto_logger.get_logger(), client_socket, event_list, flag])
    tsend.daemon = True
    trecv.daemon = True
    tsend.start()
    trecv.start()


