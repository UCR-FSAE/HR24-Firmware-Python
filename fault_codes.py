def check_for_fault_code(message, fault_code_dict):
    decoded_message = message.decode('utf-8')
    
    for byte, description in fault_code_dict.items():
        binary_code = format(byte, '08b')
        if binary_code in decoded_message:
            print(f"Fault code '{description}' detected in the message.")
            #while True:
                # Infinite loop to catch the fault code
            #    print("Catching the fault code...")

# Define Post_Faults_dictionary
Post_Faults_dictionary = {
    # Byte 0
    0: "Hardware Gate/Desaturation Fault",
    1: "HW Over-current Fault",
    2: "Accelerator Shorted",
    3: "Accelerator Open",
    4: "Current Sensor Low",
    5: "Current Sensor High",
    6: "Module Temperature Low",
    7: "Module Temperature High",

    # Byte 1
    8: "Control PCB Temperature Low",
    9: "Control PCB Temperature High",
    10: "Gate Drive PCB Temperature Low",
    11: "Gate Drive PCB Temperature High",
    12: "5V Sense Voltage Low",
    13: "5V Sense Voltage High",
    14: "12V Sense Voltage Low",
    15: "12V Sense Voltage High",

    # Byte 2
    16: "2.5V Sense Voltage Low",
    17: "2.5V Sense Voltage High",
    18: "1.5V Sense Voltage Low",
    19: "1.5V Sense Voltage High",
    20: "DC Bus Voltage High",
    21: "DC Bus Voltage Low",
    22: "Pre-charge Timeout",
    23: "Pre-charge Voltage Failure",

    # Byte 3
    24: "EEPROM Checksum Invalid",
    25: "EEPROM Data Out of Range",
    26: "EEPROM Update Required",
    27: "Hardware DC Bus Over-Voltage during initialization",
    28: "Gen 3: Reserved / Gen 5: Gate Driver Initialization",
    29: "Reserved",
    30: "Brake Shorted",
    31: "Brake Open",
}

#Ex 
message = b"00000001"
check_for_fault_code(message, Post_Faults_dictionary)

# Define Run_Faults_dictionary
Run_Faults_dictionary = {
    # Byte 4
    0: "Motor Over-speed Fault",
    1: "Over-current Fault",
    2: "Over-voltage Fault",
    3: "Inverter Over-temperature Fault",
    4: "Accelerator Input Shorted Fault",
    5: "Accelerator Input Open Fault",
    6: "Direction Command Fault",
    7: "Inverter Response Time-out Fault",

    # Byte 5 (
    8: "Hardware Gate/Desaturation Fault",
    9: "Hardware Over-current Fault",
    10: "Under-voltage Fault",
    11: "CAN Command Message Lost Fault",
    12: "Motor Over-temperature Fault",
    13: "Reserved",
    14: "Reserved",
    15: "Reserved",

    # Byte 6 
    16: "Brake Input Shorted Fault",
    17: "Brake Input Open Fault",
    18: "Module A Over-temperature Fault",
    19: "Module B Over-temperature Fault",
    20: "Module C Over-temperature Fault",
    21: "PCB Over-temperature Fault",
    22: "Gate Drive Board 1 Over-temperature Fault",
    23: "Gate Drive Board 2 Over-temperature Fault",

    # Byte 7 
    24: "Gate Drive Board 3 Over-temperature Fault",
    25: "Current Sensor Fault",
    26: "Gen 3: Reserved / Gen 5: Gate Driver Over-Voltage",
    27: "Gen 3: Hardware DC Bus Over-Voltage Fault / Gen 5: Reserved",
    28: "Gen 3: Reserved / Gen 5: Hardware DC Bus Over-voltage Fault",
    29: "Reserved",
    30: "Resolver Not Connected",
    31: "Reserved",
}

#test script
message = b"00000001"
for i in range(100):
    message += b"01"
    check_for_fault_code(message, Run_Faults_dictionary)