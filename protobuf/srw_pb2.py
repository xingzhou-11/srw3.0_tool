# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: srw.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tsrw.proto\x12\x03SRW\"T\n\x10MoveEventPayload\x12\x10\n\x08position\x18\x01 \x01(\x02\x12\r\n\x05speed\x18\x02 \x01(\x02\x12\x0b\n\x03\x61\x63\x63\x18\x03 \x01(\x02\x12\x12\n\nevent_time\x18\x04 \x01(\x02\"$\n\x0f\x41\x63kEventPayload\x12\x11\n\treply_seq\x18\x01 \x01(\r\"K\n\x16\x45ndCommandEventPayload\x12\x11\n\treply_seq\x18\x01 \x01(\r\x12\x0e\n\x06result\x18\x02 \x01(\x08\x12\x0e\n\x06status\x18\x03 \x01(\t\"q\n\x05\x45rror\x12\"\n\nerror_code\x18\x01 \x01(\x0e\x32\x0e.SRW.ErrorCode\x12\"\n\nerror_type\x18\x02 \x01(\x0e\x32\x0e.SRW.ErrorType\x12\x0f\n\x07task_id\x18\x03 \x01(\r\x12\x0f\n\x07payload\x18\x04 \x01(\x0c\"\xd8\x01\n\x11\x45rrorEventPayload\x12\x11\n\treply_seq\x18\x01 \x01(\r\x12\x0c\n\x04size\x18\x02 \x01(\r\x12\x1b\n\x07\x65rror_1\x18\x03 \x01(\x0b\x32\n.SRW.Error\x12\x1b\n\x07\x65rror_2\x18\x04 \x01(\x0b\x32\n.SRW.Error\x12\x1b\n\x07\x65rror_3\x18\x05 \x01(\x0b\x32\n.SRW.Error\x12\x1b\n\x07\x65rror_4\x18\x06 \x01(\x0b\x32\n.SRW.Error\x12\x1b\n\x07\x65rror_5\x18\x07 \x01(\x0b\x32\n.SRW.Error\x12\x11\n\ttrue_size\x18\x08 \x01(\r\"I\n\x12HealthEventPayload\x12\x11\n\treply_seq\x18\x01 \x01(\r\x12\x0f\n\x07voltage\x18\x02 \x01(\x02\x12\x0f\n\x07\x63urrent\x18\x03 \x01(\x02\"\xc2\x01\n\x10InfoEventPayload\x12\x11\n\treply_seq\x18\x01 \x01(\r\x12\x18\n\x10hardware_version\x18\x02 \x01(\t\x12\x18\n\x10software_version\x18\x03 \x01(\t\x12\x15\n\rserial_number\x18\x04 \x01(\t\x12\x18\n\x10protocol_version\x18\x05 \x01(\t\x12\x16\n\x0e\x63ommit_version\x18\x06 \x01(\t\x12\x0e\n\x06\x61\x64\x64r64\x18\x07 \x01(\x0c\x12\x0e\n\x06\x61\x64\x64r16\x18\x08 \x01(\x0c\"\xdc\x02\n\x12StatusEventPayload\x12\x11\n\treply_seq\x18\x01 \x01(\r\x12%\n\tsml_state\x18\x02 \x01(\x0e\x32\x12.SRW.MainStateEnum\x12\x18\n\x10main_motor_state\x18\x03 \x01(\r\x12\x18\n\x10\x62\x65lt_motor_state\x18\x04 \x01(\r\x12$\n\x1c\x61voidance_front_sensor_state\x18\x05 \x01(\x08\x12#\n\x1b\x61voidance_rear_sensor_state\x18\x06 \x01(\x08\x12\x1b\n\x13side_A_sensor_state\x18\x07 \x01(\x08\x12\x1b\n\x13side_B_sensor_state\x18\x08 \x01(\x08\x12\x1b\n\x13marker_sensor_state\x18\t \x01(\x08\x12\x19\n\x11home_sensor_state\x18\n \x01(\x08\x12\x1b\n\x13robot_position_in_m\x18\x0b \x01(\x02\"\xa4\x01\n\x12\x43onfigEventPayload\x12\x11\n\treply_seq\x18\x01 \x01(\r\x12!\n\x06\x61\x63tion\x18\x02 \x01(\x0e\x32\x11.SRW.ConfigAction\x12\x1f\n\x05\x65ntry\x18\x03 \x01(\x0e\x32\x10.SRW.ConfigEntry\x12\x14\n\nuint_value\x18\x04 \x01(\rH\x00\x12\x13\n\tstr_value\x18\x05 \x01(\tH\x00\x42\x0c\n\nconfig_val\"f\n\x11ResetEventPayload\x12\x11\n\treply_seq\x18\x01 \x01(\r\x12\x1e\n\x16hardware_startup_count\x18\x02 \x01(\r\x12\x1e\n\x16software_startup_count\x18\x03 \x01(\r\"\xbd\x03\n\x05\x45vent\x12\x1c\n\x04type\x18\x01 \x01(\x0e\x32\x0e.SRW.EventType\x12\x0b\n\x03seq\x18\x02 \x01(\r\x12\x0c\n\x04time\x18\x03 \x01(\x04\x12#\n\x03\x61\x63k\x18\x04 \x01(\x0b\x32\x14.SRW.AckEventPayloadH\x00\x12%\n\x04move\x18\x05 \x01(\x0b\x32\x15.SRW.MoveEventPayloadH\x00\x12*\n\x03\x65nd\x18\x06 \x01(\x0b\x32\x1b.SRW.EndCommandEventPayloadH\x00\x12\'\n\x05\x65rror\x18\x07 \x01(\x0b\x32\x16.SRW.ErrorEventPayloadH\x00\x12)\n\x06health\x18\x08 \x01(\x0b\x32\x17.SRW.HealthEventPayloadH\x00\x12%\n\x04info\x18\t \x01(\x0b\x32\x15.SRW.InfoEventPayloadH\x00\x12)\n\x06status\x18\n \x01(\x0b\x32\x17.SRW.StatusEventPayloadH\x00\x12)\n\x06\x63onfig\x18\x0b \x01(\x0b\x32\x17.SRW.ConfigEventPayloadH\x00\x12\'\n\x05reset\x18\x0c \x01(\x0b\x32\x16.SRW.ResetEventPayloadH\x00\x42\t\n\x07payload\"&\n\x11\x41\x63kCommandPayload\x12\x11\n\treply_seq\x18\x01 \x01(\r\"o\n\x12MoveCommandPayload\x12\x10\n\x08position\x18\x01 \x01(\x02\x12\r\n\x05speed\x18\x02 \x01(\x02\x12\x0b\n\x03\x61\x63\x63\x18\x03 \x01(\x02\x12\x0b\n\x03\x64\x65\x63\x18\x04 \x01(\x02\x12\x1e\n\x16report_frequency_boost\x18\x05 \x01(\x08\"\'\n\x12LoadCommandPayload\x12\x11\n\tdirection\x18\x01 \x01(\x08\")\n\x14UnloadCommandPayload\x12\x11\n\tdirection\x18\x01 \x01(\x08\"M\n\x19\x46orceUnloadCommandPayload\x12\x11\n\tdirection\x18\x01 \x01(\x08\x12\x1d\n\x15\x66orce_unload_duration\x18\x02 \x01(\r\"9\n\x12HomeCommandPayload\x12\x11\n\tdirection\x18\x01 \x01(\x08\x12\x10\n\x08position\x18\x02 \x01(\x02\"q\n\x14GoLiftCommandPayload\x12\x10\n\x08position\x18\x01 \x01(\x02\x12\r\n\x05speed\x18\x02 \x01(\x02\x12\x0b\n\x03\x61\x63\x63\x18\x03 \x01(\x02\x12\x0b\n\x03\x64\x65\x63\x18\x04 \x01(\x02\x12\x1e\n\x16report_frequency_boost\x18\x05 \x01(\x08\"\x16\n\x14HealthCommandPayload\"\x14\n\x12InfoCommandPayload\"\x16\n\x14StatusCommandPayload\"\x93\x01\n\x14\x43onfigCommandPayload\x12!\n\x06\x61\x63tion\x18\x01 \x01(\x0e\x32\x11.SRW.ConfigAction\x12\x1f\n\x05\x65ntry\x18\x02 \x01(\x0e\x32\x10.SRW.ConfigEntry\x12\x14\n\nuint_value\x18\x03 \x01(\rH\x00\x12\x13\n\tstr_value\x18\x04 \x01(\tH\x00\x42\x0c\n\nconfig_val\"\x15\n\x13ResetCommandPayload\">\n\x17\x45mergencyCommandPayload\x12\x0b\n\x03\x64\x65\x63\x18\x01 \x01(\x02\x12\x16\n\x0einto_emergency\x18\x02 \x01(\x08\"\xe3\x01\n\x15RecoverCommandPayload\x12\x0c\n\x04size\x18\x01 \x01(\r\x12$\n\x0c\x65rror_code_1\x18\x02 \x01(\x0e\x32\x0e.SRW.ErrorCode\x12$\n\x0c\x65rror_code_2\x18\x03 \x01(\x0e\x32\x0e.SRW.ErrorCode\x12$\n\x0c\x65rror_code_3\x18\x04 \x01(\x0e\x32\x0e.SRW.ErrorCode\x12$\n\x0c\x65rror_code_4\x18\x05 \x01(\x0e\x32\x0e.SRW.ErrorCode\x12$\n\x0c\x65rror_code_5\x18\x06 \x01(\x0e\x32\x0e.SRW.ErrorCode\"3\n\x13SleepCommandPayload\x12\x1c\n\x04type\x18\x01 \x01(\x0e\x32\x0e.SRW.SleepType\"\x17\n\x15UpgradeCommandPayload\"\x15\n\x13\x45rrorCommandPayload\"\xc2\x06\n\x07\x43ommand\x12\x1e\n\x04type\x18\x01 \x01(\x0e\x32\x10.SRW.CommandType\x12\x0b\n\x03seq\x18\x02 \x01(\r\x12\x0c\n\x04time\x18\x03 \x01(\x04\x12%\n\x03\x61\x63k\x18\x04 \x01(\x0b\x32\x16.SRW.AckCommandPayloadH\x00\x12\'\n\x04move\x18\x05 \x01(\x0b\x32\x17.SRW.MoveCommandPayloadH\x00\x12\'\n\x04load\x18\x06 \x01(\x0b\x32\x17.SRW.LoadCommandPayloadH\x00\x12+\n\x06unload\x18\x07 \x01(\x0b\x32\x19.SRW.UnloadCommandPayloadH\x00\x12\'\n\x04home\x18\x08 \x01(\x0b\x32\x17.SRW.HomeCommandPayloadH\x00\x12)\n\x04lift\x18\t \x01(\x0b\x32\x19.SRW.GoLiftCommandPayloadH\x00\x12+\n\x06health\x18\n \x01(\x0b\x32\x19.SRW.HealthCommandPayloadH\x00\x12\'\n\x04info\x18\x0b \x01(\x0b\x32\x17.SRW.InfoCommandPayloadH\x00\x12+\n\x06status\x18\x0c \x01(\x0b\x32\x19.SRW.StatusCommandPayloadH\x00\x12+\n\x06\x63onfig\x18\r \x01(\x0b\x32\x19.SRW.ConfigCommandPayloadH\x00\x12)\n\x05reset\x18\x0e \x01(\x0b\x32\x18.SRW.ResetCommandPayloadH\x00\x12\x31\n\temergency\x18\x0f \x01(\x0b\x32\x1c.SRW.EmergencyCommandPayloadH\x00\x12-\n\x07recover\x18\x10 \x01(\x0b\x32\x1a.SRW.RecoverCommandPayloadH\x00\x12)\n\x05sleep\x18\x11 \x01(\x0b\x32\x18.SRW.SleepCommandPayloadH\x00\x12-\n\x07upgrade\x18\x12 \x01(\x0b\x32\x1a.SRW.UpgradeCommandPayloadH\x00\x12)\n\x05\x65rror\x18\x13 \x01(\x0b\x32\x18.SRW.ErrorCommandPayloadH\x00\x12\x35\n\x0b\x66orceunload\x18\x14 \x01(\x0b\x32\x1e.SRW.ForceUnloadCommandPayloadH\x00\x42\t\n\x07payload*\x97\x08\n\tErrorCode\x12\t\n\x05\x44ummy\x10\x00\x12\x11\n\rNODE402_ERROR\x10\x01\x12\x15\n\x11\x41LLCAN_NODE_ERROR\x10\x02\x12\x0c\n\x07MOVE_OK\x10\x80\x02\x12\x15\n\x10MOVE_MOTOR_ERROR\x10\x81\x02\x12\x17\n\x12MOVE_SAFETY_SENSOR\x10\x82\x02\x12\x16\n\x11MOVE_CANBUS_FAULT\x10\x83\x02\x12\x11\n\x0cMOVE_TIMEOUT\x10\x84\x02\x12\x16\n\x11MOVE_MARKER_ERROR\x10\x85\x02\x12\x0c\n\x07LOAD_OK\x10\x80\x04\x12\x15\n\x10LOAD_MOTOR_ERROR\x10\x81\x04\x12\x1a\n\x15LOAD_NO_ITEM_DETECTED\x10\x82\x04\x12\x16\n\x11LOAD_CANBUS_FAULT\x10\x83\x04\x12\x11\n\x0cLOAD_TIMEOUT\x10\x84\x04\x12\x16\n\x11LOAD_ITEM_STUCKED\x10\x85\x04\x12\x16\n\x11LOAD_SENSOR_ERROR\x10\x86\x04\x12\x14\n\x0fLOAD_OVERLENGTH\x10\x87\x04\x12\x0e\n\tUNLOAD_OK\x10\x80\x06\x12\x17\n\x12UNLOAD_MOTOR_ERROR\x10\x81\x06\x12\x1c\n\x17UNLOAD_NO_ITEM_DETECTED\x10\x82\x06\x12\x18\n\x13UNLOAD_CANBUS_FAULT\x10\x83\x06\x12\x13\n\x0eUNLOAD_TIMEOUT\x10\x84\x06\x12\x18\n\x13UNLOAD_ITEM_STUCKED\x10\x85\x06\x12\x18\n\x13UNLOAD_SENSOR_ERROR\x10\x86\x06\x12\x0e\n\tGOLIFT_OK\x10\x80\x08\x12\x17\n\x12GOLIFT_MOTOR_ERROR\x10\x81\x08\x12\x1e\n\x19GOLIFT_NO_MARKER_DETECTED\x10\x82\x08\x12\x18\n\x13GOLIFT_CANBUS_FAULT\x10\x83\x08\x12\x1a\n\x15GOLIFT_LIFT_POS_ERROR\x10\x84\x08\x12\x0c\n\x07HOME_OK\x10\x80\n\x12\x15\n\x10HOME_MOTOR_ERROR\x10\x81\n\x12\x1c\n\x17HOME_NO_MARKER_DETECTED\x10\x82\n\x12\x16\n\x11HOME_CANBUS_FAULT\x10\x83\n\x12\x0f\n\nRECOVER_OK\x10\x80\x0c\x12\x1b\n\x16RECOVER_SENSOR_TRIGGER\x10\x81\x0c\x12\x1d\n\x18RECOVER_MOTOR_INIT_FAULT\x10\x82\x0c\x12\x0b\n\x06\x41\x43K_OK\x10\x80\x0e\x12\x10\n\x0b\x41\x43K_TIMEOUT\x10\x81\x0e\x12\x14\n\x0f\x46ORCE_UNLOAD_OK\x10\x80\x10\x12\x1d\n\x18\x46ORCE_UNLOAD_MOTOR_ERROR\x10\x81\x10\x12\x1e\n\x19\x46ORCE_UNLOAD_CANBUS_FAULT\x10\x82\x10\x12\x1e\n\x19\x46ORCE_UNLOAD_SENSOR_ERROR\x10\x83\x10\x12\x16\n\x11\x45XIT_EMERGENCY_OK\x10\x80\x12\x12%\n EXIT_EMERGENCY_EMCY_BUTTON_PRESS\x10\x81\x12*\x8b\x02\n\tErrorType\x12\x12\n\x0eMOVEMENT_MOTOR\x10\x00\x12\x10\n\x0cHANDLE_MOTOR\x10\x01\x12\x07\n\x03\x41\x43K\x10\x02\x12\x08\n\x04MOVE\x10\x03\x12\x08\n\x04LOAD\x10\x04\x12\n\n\x06UNLOAD\x10\x05\x12\x08\n\x04HOME\x10\x06\x12\x0b\n\x07GO_LIFT\x10\x07\x12\n\n\x06HEALTH\x10\x08\x12\x08\n\x04INFO\x10\t\x12\n\n\x06STATUS\x10\n\x12\n\n\x06\x43ONFIG\x10\x0b\x12\t\n\x05RESET\x10\x0c\x12\r\n\tEMERGENCY\x10\r\x12\x0b\n\x07RECOVER\x10\x0e\x12\t\n\x05SLEEP\x10\x0f\x12\x0b\n\x07UPGRADE\x10\x10\x12\x10\n\x0c\x46ORCE_UNLOAD\x10\x11\x12\r\n\tEXIT_EMCY\x10\x12\x12\n\n\x06\x41LLCAN\x10\x13*\xa5\x03\n\rMainStateEnum\x12\x0e\n\nSTATE_INIT\x10\x00\x12\x17\n\x13STATE_HANDLE_ENABLE\x10\x01\x12\x0e\n\nSTATE_IDLE\x10\x02\x12\x0e\n\nSTATE_MOVE\x10\x03\x12\x0e\n\nSTATE_HOME\x10\x04\x12\x0e\n\nSTATE_LIFT\x10\x05\x12\x0e\n\nSTATE_LOAD\x10\x06\x12\x10\n\x0cSTATE_UNLOAD\x10\x07\x12\x18\n\x14STATE_INTO_EMERGENCY\x10\x08\x12\x13\n\x0fSTATE_EMERGENCY\x10\t\x12\x18\n\x14STATE_EXIT_EMERGENCY\x10\n\x12\r\n\tSTATE_ACK\x10\x0b\x12\x11\n\rSTATE_UPGRADE\x10\x0c\x12\x0f\n\x0bSTATE_FAULT\x10\r\x12\x0f\n\x0bSTATE_SLEEP\x10\x0e\x12\x14\n\x10STATE_EXIT_SLEEP\x10\x0f\x12\x13\n\x0fSTATE_RESET_PUB\x10\x10\x12\x16\n\x12STATE_FORCE_UNLOAD\x10\x11\x12\x16\n\x12STATE_INITPROGRESS\x10\x12\x12\x11\n\rSTATE_RECOVER\x10\x13\x12\x0e\n\nSTATE_TEST\x10\x14*\xce\x01\n\tEventType\x12\r\n\tACK_EVENT\x10\x00\x12\x0e\n\nMOVE_EVENT\x10\x01\x12\x15\n\x11\x45ND_COMMAND_EVENT\x10\x02\x12\x0f\n\x0b\x45RROR_EVENT\x10\x03\x12\x10\n\x0cHEALTH_EVENT\x10\x04\x12\x0e\n\nINFO_EVENT\x10\x05\x12\x10\n\x0cSTATUS_EVENT\x10\x06\x12\x10\n\x0c\x43ONFIG_EVENT\x10\x07\x12\x0f\n\x0bRESET_EVENT\x10\x08\x12\x14\n\x10HEART_BEAT_EVENT\x10\t\x12\r\n\tEVENT_NUM\x10\n*1\n\x0c\x43onfigAction\x12\x0f\n\x0bREAD_ACTION\x10\x00\x12\x10\n\x0cWIRTE_ACTION\x10\x01*\xc4\t\n\x0b\x43onfigEntry\x12\t\n\x05\x44UMMY\x10\x00\x12\x1a\n\x15MAIN_MOTOR_RESOLUTION\x10\x80@\x12\x1f\n\x1aMAIN_MOTOR_REDUCTION_RATIO\x10\x81@\x12\x1e\n\x19MAIN_MOTOR_WHEEL_DISTANCE\x10\x82@\x12 \n\x1bMAIN_MOTOR_GO_LIFT_DISTANCE\x10\x83@\x12\x18\n\x13MAIN_MOTOR_HOME_VEL\x10\x84@\x12\x14\n\x0f\x42\x45LT_LOAD_SPEED\x10\x85@\x12\x16\n\x11\x42\x45LT_UNLOAD_SPEED\x10\x86@\x12\x18\n\x13\x42\x45LT_UNLOAD_TIMEOUT\x10\x87@\x12\x1a\n\x15\x42\x45LT_MOTOR_RESOLUTION\x10\x88@\x12\x1f\n\x1a\x42\x45LT_MOTOR_REDUCTION_RATIO\x10\x89@\x12\x19\n\x14\x42\x45LT_MOTOR_WHEEL_DIA\x10\x8a@\x12\r\n\x08\x42\x45LT_LEN\x10\x8b@\x12\x13\n\x0e\x42\x45LT_MOTOR_ACC\x10\x8c@\x12\x1b\n\x16MOTOR_ERR_RECOVER_CONT\x10\x8d@\x12\x1c\n\x17MOTOR_REACHED_THRESHOLD\x10\x8e@\x12\x1d\n\x18MOTOR_VELOCITY_THRESHOLD\x10\x8f@\x12\x14\n\x0f\x45NCODER_FACTORS\x10\x90@\x12\x0f\n\nVERSION_HW\x10\x91@\x12\x12\n\rVERSION_PROTO\x10\x92@\x12\x0f\n\nSERIAL_NUM\x10\x93@\x12\x14\n\x0fMARKER_MARKER_1\x10\x94@\x12\x14\n\x0fMARKER_MARKER_2\x10\x95@\x12\x14\n\x0fMARKER_MARKER_3\x10\x96@\x12\x14\n\x0fMARKER_MARKER_4\x10\x97@\x12\x14\n\x0fMARKER_MARKER_5\x10\x98@\x12\x14\n\x0fMARKER_MARKER_6\x10\x99@\x12\x14\n\x0fMARKER_MARKER_7\x10\x9a@\x12\x14\n\x0fMARKER_MARKER_8\x10\x9b@\x12\x14\n\x0fMARKER_MARKER_9\x10\x9c@\x12\x15\n\x10MARKER_MARKER_10\x10\x9d@\x12\x15\n\x10MARKER_MARKER_11\x10\x9e@\x12\x15\n\x10MARKER_MARKER_12\x10\x9f@\x12\x15\n\x10MARKER_MARKER_13\x10\xa0@\x12\x15\n\x10MARKER_MARKER_14\x10\xa1@\x12\x15\n\x10MARKER_MARKER_15\x10\xa2@\x12\x15\n\x10MARKER_MARKER_16\x10\xa3@\x12\x15\n\x10MARKER_MARKER_17\x10\xa4@\x12\x15\n\x10MARKER_MARKER_18\x10\xa5@\x12\x15\n\x10MARKER_MARKER_19\x10\xa6@\x12\x15\n\x10MARKER_MARKER_20\x10\xa7@\x12\x15\n\x10MARKER_MARKER_21\x10\xa8@\x12\x15\n\x10MARKER_MARKER_22\x10\xa9@\x12\x15\n\x10MARKER_MARKER_23\x10\xaa@\x12\x15\n\x10MARKER_MARKER_24\x10\xab@\x12\x15\n\x10MARKER_MARKER_25\x10\xac@\x12\x15\n\x10MARKER_MARKER_26\x10\xad@\x12\x15\n\x10MARKER_MARKER_27\x10\xae@\x12\x15\n\x10MARKER_MARKER_28\x10\xaf@\x12\x15\n\x10MARKER_MARKER_29\x10\xb0@\x12\x15\n\x10MARKER_MARKER_30\x10\xb1@*,\n\tSleepType\x12\x0f\n\x0b\x45NTER_SLEEP\x10\x00\x12\x0e\n\nEXIT_SLEEP\x10\x01*\xf0\x02\n\x0b\x43ommandType\x12\x0f\n\x0b\x41\x43K_COMMAND\x10\x00\x12\x10\n\x0cMOVE_COMMAND\x10\x01\x12\x10\n\x0cLOAD_COMMAND\x10\x02\x12\x12\n\x0eUNLOAD_COMMAND\x10\x03\x12\x10\n\x0cHOME_COMMAND\x10\x04\x12\x13\n\x0fGO_LIFT_COMMAND\x10\x05\x12\x12\n\x0eHEALTH_COMMAND\x10\x06\x12\x10\n\x0cINFO_COMMAND\x10\x07\x12\x12\n\x0eSTATUS_COMMAND\x10\x08\x12\x12\n\x0e\x43ONFIG_COMMAND\x10\t\x12\x11\n\rRESET_COMMAND\x10\n\x12\x15\n\x11\x45MERGENCY_COMMAND\x10\x0b\x12\x13\n\x0fRECOVER_COMMAND\x10\x0c\x12\x11\n\rSLEEP_COMMAND\x10\r\x12\x13\n\x0fUPGRADE_COMMAND\x10\x0e\x12\x11\n\rERROR_COMMAND\x10\x0f\x12\x18\n\x14\x46ORCE_UNLOAD_COMMAND\x10\x10\x12\x0f\n\x0b\x43OMMAND_NUM\x10\x11\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'srw_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_ERRORCODE']._serialized_start=3861
  _globals['_ERRORCODE']._serialized_end=4908
  _globals['_ERRORTYPE']._serialized_start=4911
  _globals['_ERRORTYPE']._serialized_end=5178
  _globals['_MAINSTATEENUM']._serialized_start=5181
  _globals['_MAINSTATEENUM']._serialized_end=5602
  _globals['_EVENTTYPE']._serialized_start=5605
  _globals['_EVENTTYPE']._serialized_end=5811
  _globals['_CONFIGACTION']._serialized_start=5813
  _globals['_CONFIGACTION']._serialized_end=5862
  _globals['_CONFIGENTRY']._serialized_start=5865
  _globals['_CONFIGENTRY']._serialized_end=7085
  _globals['_SLEEPTYPE']._serialized_start=7087
  _globals['_SLEEPTYPE']._serialized_end=7131
  _globals['_COMMANDTYPE']._serialized_start=7134
  _globals['_COMMANDTYPE']._serialized_end=7502
  _globals['_MOVEEVENTPAYLOAD']._serialized_start=18
  _globals['_MOVEEVENTPAYLOAD']._serialized_end=102
  _globals['_ACKEVENTPAYLOAD']._serialized_start=104
  _globals['_ACKEVENTPAYLOAD']._serialized_end=140
  _globals['_ENDCOMMANDEVENTPAYLOAD']._serialized_start=142
  _globals['_ENDCOMMANDEVENTPAYLOAD']._serialized_end=217
  _globals['_ERROR']._serialized_start=219
  _globals['_ERROR']._serialized_end=332
  _globals['_ERROREVENTPAYLOAD']._serialized_start=335
  _globals['_ERROREVENTPAYLOAD']._serialized_end=551
  _globals['_HEALTHEVENTPAYLOAD']._serialized_start=553
  _globals['_HEALTHEVENTPAYLOAD']._serialized_end=626
  _globals['_INFOEVENTPAYLOAD']._serialized_start=629
  _globals['_INFOEVENTPAYLOAD']._serialized_end=823
  _globals['_STATUSEVENTPAYLOAD']._serialized_start=826
  _globals['_STATUSEVENTPAYLOAD']._serialized_end=1174
  _globals['_CONFIGEVENTPAYLOAD']._serialized_start=1177
  _globals['_CONFIGEVENTPAYLOAD']._serialized_end=1341
  _globals['_RESETEVENTPAYLOAD']._serialized_start=1343
  _globals['_RESETEVENTPAYLOAD']._serialized_end=1445
  _globals['_EVENT']._serialized_start=1448
  _globals['_EVENT']._serialized_end=1893
  _globals['_ACKCOMMANDPAYLOAD']._serialized_start=1895
  _globals['_ACKCOMMANDPAYLOAD']._serialized_end=1933
  _globals['_MOVECOMMANDPAYLOAD']._serialized_start=1935
  _globals['_MOVECOMMANDPAYLOAD']._serialized_end=2046
  _globals['_LOADCOMMANDPAYLOAD']._serialized_start=2048
  _globals['_LOADCOMMANDPAYLOAD']._serialized_end=2087
  _globals['_UNLOADCOMMANDPAYLOAD']._serialized_start=2089
  _globals['_UNLOADCOMMANDPAYLOAD']._serialized_end=2130
  _globals['_FORCEUNLOADCOMMANDPAYLOAD']._serialized_start=2132
  _globals['_FORCEUNLOADCOMMANDPAYLOAD']._serialized_end=2209
  _globals['_HOMECOMMANDPAYLOAD']._serialized_start=2211
  _globals['_HOMECOMMANDPAYLOAD']._serialized_end=2268
  _globals['_GOLIFTCOMMANDPAYLOAD']._serialized_start=2270
  _globals['_GOLIFTCOMMANDPAYLOAD']._serialized_end=2383
  _globals['_HEALTHCOMMANDPAYLOAD']._serialized_start=2385
  _globals['_HEALTHCOMMANDPAYLOAD']._serialized_end=2407
  _globals['_INFOCOMMANDPAYLOAD']._serialized_start=2409
  _globals['_INFOCOMMANDPAYLOAD']._serialized_end=2429
  _globals['_STATUSCOMMANDPAYLOAD']._serialized_start=2431
  _globals['_STATUSCOMMANDPAYLOAD']._serialized_end=2453
  _globals['_CONFIGCOMMANDPAYLOAD']._serialized_start=2456
  _globals['_CONFIGCOMMANDPAYLOAD']._serialized_end=2603
  _globals['_RESETCOMMANDPAYLOAD']._serialized_start=2605
  _globals['_RESETCOMMANDPAYLOAD']._serialized_end=2626
  _globals['_EMERGENCYCOMMANDPAYLOAD']._serialized_start=2628
  _globals['_EMERGENCYCOMMANDPAYLOAD']._serialized_end=2690
  _globals['_RECOVERCOMMANDPAYLOAD']._serialized_start=2693
  _globals['_RECOVERCOMMANDPAYLOAD']._serialized_end=2920
  _globals['_SLEEPCOMMANDPAYLOAD']._serialized_start=2922
  _globals['_SLEEPCOMMANDPAYLOAD']._serialized_end=2973
  _globals['_UPGRADECOMMANDPAYLOAD']._serialized_start=2975
  _globals['_UPGRADECOMMANDPAYLOAD']._serialized_end=2998
  _globals['_ERRORCOMMANDPAYLOAD']._serialized_start=3000
  _globals['_ERRORCOMMANDPAYLOAD']._serialized_end=3021
  _globals['_COMMAND']._serialized_start=3024
  _globals['_COMMAND']._serialized_end=3858
# @@protoc_insertion_point(module_scope)