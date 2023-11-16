from . import zigbee_pb2


class CommandData:
    seq = time = 0  # general properties
    move_position = move_speed = move_acc = move_dec = 0  # move
    direction = False  # load & unload & home
    reply_seq = 0  # ack

    def __init__(self, type=zigbee_pb2.ACK_COMMAND, seq=0, time=0):
        self.type = type
        self.seq = seq
        self.time = time

    def increment_seq(self):
        self.seq += 1

    def get_command(self) -> zigbee_pb2.Command:
        """command data to protobuf command converter

        Args:
            data (CommandData): command data

        Returns:
            zigbee_pb2.Command: protobuf command
        """
        command = zigbee_pb2.Command()
        command.type = self.type
        command.seq = self.seq
        command.time = self.time
        if command.type == zigbee_pb2.MOVE_COMMAND:
            command.move.position = self.move_position
            command.move.speed = self.move_speed
            command.move.acc = self.move_acc
            command.move.dec = self.move_dec
        elif command.type == zigbee_pb2.GO_LIFT_COMMAND:
            command.lift.position = self.move_position
            command.lift.speed = self.move_speed
            command.lift.acc = self.move_acc
            command.lift.dec = self.move_dec
        elif command.type == zigbee_pb2.ACK_COMMAND:
            command.ack.reply_seq = self.reply_seq
        elif command.type == zigbee_pb2.LOAD_COMMAND:
            command.load.direction = self.direction
        elif command.type == zigbee_pb2.UNLOAD_COMMAND:
            command.unload.direction = self.direction
        elif command.type == zigbee_pb2.HOME_COMMAND:
            command.home.direction = self.direction
            command.home.position = self.move_position
        elif command.type == zigbee_pb2.EMERGENCY_COMMAND:
            command.emergency.dec = self.emergency_dec
            command.emergency.into_emergency = self.emergency_into_emergency
        elif command.type == zigbee_pb2.RECOVER_COMMAND:
            command.recover.size = self.size
            command.recover.error_code_1 = self.error_code_1
            command.recover.error_code_2 = self.error_code_2
            command.recover.error_code_3 = self.error_code_3
            command.recover.error_code_4 = self.error_code_4
            command.recover.error_code_5 = self.error_code_5
        elif command.type == zigbee_pb2.SLEEP_COMMAND:
            command.sleep.type = (
                zigbee_pb2.EXIT_SLEEP
                if self.sleep_type == True
                else zigbee_pb2.ENTER_SLEEP
            )
        elif command.type == zigbee_pb2.FORCE_UNLOAD_COMMAND:
            command.forceunload.direction = self.direction
            command.forceunload.force_unload_duration = self.force_unload_duration
        return command

    def set_move_command(self, pos: float, vel: float, acc: float, dec: float):
        self.type = zigbee_pb2.MOVE_COMMAND
        self.move_position = pos
        self.move_speed = vel
        self.move_acc = acc
        self.move_dec = dec

    def set_golift_command(self, pos: float, vel: float, acc: float, dec: float):
        self.type = zigbee_pb2.GO_LIFT_COMMAND
        self.move_position = pos
        self.move_speed = vel
        self.move_acc = acc
        self.move_dec = dec

    def set_home_command(self, dir: bool, pos: float):
        self.type = zigbee_pb2.HOME_COMMAND
        self.direction = dir
        self.move_position = pos

    def set_load_command(self, dir):
        self.type = zigbee_pb2.LOAD_COMMAND
        self.direction = dir

    def set_unload_command(self, dir):
        self.type = zigbee_pb2.UNLOAD_COMMAND
        self.direction = dir

    def set_ack_command(self, r_seq: int):
        self.type = zigbee_pb2.ACK_COMMAND
        self.reply_seq = r_seq

    def set_reset_command(self):
        self.type = zigbee_pb2.RESET_COMMAND

    def set_emergency_command(self, dec: float, into_emergency: bool):
        self.type = zigbee_pb2.EMERGENCY_COMMAND
        self.emergency_dec = dec
        self.emergency_into_emergency = into_emergency

    def set_sleep_command(self, type: bool):
        self.type = zigbee_pb2.SLEEP_COMMAND
        self.sleep_type = type

    def set_info_command(self):
        self.type = zigbee_pb2.INFO_COMMAND

    def set_status_command(self):
        self.type = zigbee_pb2.STATUS_COMMAND

    def set_error_command(self):
        self.type = zigbee_pb2.ERROR_COMMAND

    def set_recover_command(
        self,
        error_size: int,
        error_code_1: int,
        error_code_2: int,
        error_code_3: int,
        error_code_4: int,
        error_code_5: int,
    ):
        self.type = zigbee_pb2.RECOVER_COMMAND
        self.size = error_size
        self.error_code_1 = error_code_1
        self.error_code_2 = error_code_2
        self.error_code_3 = error_code_3
        self.error_code_4 = error_code_4
        self.error_code_5 = error_code_5

    def set_upgrade_command(self):
        self.type = zigbee_pb2.UPGRADE_COMMAND

    def set_health_command(self):
        self.type = zigbee_pb2.HEALTH_COMMAND

    def set_forceunload_command(self, dir, time: int):
        self.type = zigbee_pb2.FORCE_UNLOAD_COMMAND
        self.direction = dir
        self.force_unload_duration = time
