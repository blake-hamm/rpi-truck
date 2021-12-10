
import obd
import warnings

# Hide output

connection = obd.OBD()

for cmd in list(connection.supported_commands):
    print(cmd)
