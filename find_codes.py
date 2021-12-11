
import obd

obd.logger.setLevel(obd.logging.DEBUG) # Show log

connection = obd.OBD() # USB connect

print('PROTOCOL: ',connection.protocol_name()) # Print protocal name

for cmd in list(connection.supported_commands): # Print supported commands
    print(cmd)

###

# Get supported PID A's
cmd = obd.commands.PIDS_A # select an OBD command (sensor)
response = connection.query(cmd, force=True) # send the command, and parse the response
print('PID A: ', response.value) # returns unit-bearing values thanks to Pint

# Get supported PID B's
cmd = obd.commands.PIDS_B # select an OBD command (sensor)
response = connection.query(cmd, force=True) # send the command, and parse the response
print('PID B: ', response.value) # returns unit-bearing values thanks to Pint

# Get supported PID C's
cmd = obd.commands.PIDS_C # select an OBD command (sensor)
response = connection.query(cmd, force=True) # send the command, and parse the response
print('PID C: ', response.value) # returns unit-bearing values thanks to Pint

###

# Get supported MID A's
# cmd = obd.commands.PIDS_9A # select an OBD command (sensor)
# response = connection.query(cmd) # send the command, and parse the response
# print('PIDS 9A: ', response.value) # returns unit-bearing values thanks to Pint

###

# Get supported MID A's
cmd = obd.commands.MIDS_A # select an OBD command (sensor)
response = connection.query(cmd, force=True) # send the command, and parse the response
print('MIDS A: ', response.value) # returns unit-bearing values thanks to Pint

# Get supported MID B's
cmd = obd.commands.MIDS_B # select an OBD command (sensor)
response = connection.query(cmd, force=True) # send the command, and parse the response
print('MIDS B: ', response.value) # returns unit-bearing values thanks to Pint

# Get supported MID C's
cmd = obd.commands.MIDS_C # select an OBD command (sensor)
response = connection.query(cmd, force=True) # send the command, and parse the response
print('MIDS C: ', response.value) # returns unit-bearing values thanks to Pint

# Get supported MID D's
cmd = obd.commands.MIDS_D # select an OBD command (sensor)
response = connection.query(cmd, force=True) # send the command, and parse the response
print('MIDS D: ', response.value) # returns unit-bearing values thanks to Pint

# Get supported MID E's
cmd = obd.commands.MIDS_E # select an OBD command (sensor)
response = connection.query(cmd, force=True) # send the command, and parse the response
print('MIDS E: ', response.value) # returns unit-bearing values thanks to Pint

# Get supported MID F's
cmd = obd.commands.MIDS_F # select an OBD command (sensor)
response = connection.query(cmd, force=True) # send the command, and parse the response
print('MIDS F: ', response.value) # returns unit-bearing values thanks to Pint