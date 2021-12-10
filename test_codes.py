
import obd

connection = obd.OBD()

for i in range(1,3):
    print('')
    print(f'====================Mode 0{i}====================')
    for j in range(len(obd.commands[i])):
        print('')
        cmd = obd.commands[i][j]

        if (response := connection.query(cmd).value) is None:
            continue
        else:
            print('~~~~~~~~~~~~~~~~~~SUCCESS~~~~~~~~~~~~~~~~~~')
            print(cmd.name)
            print(response)
