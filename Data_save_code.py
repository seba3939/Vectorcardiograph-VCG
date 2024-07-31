import time
import serial
import numpy as np
import matplotlib.pyplot as plt

# Parámetros de función
numero_de_muestras = 800
periodo_muestreo = 0.0025

vector = np.arange(0, numero_de_muestras * periodo_muestreo, periodo_muestreo)

muestras = vector.size
numero_de_graficas = 1

P = np.zeros((numero_de_graficas, muestras))
fig = plt.figure()

# Función
try:
    arduino = serial.Serial('COM5', 115200)
    time.sleep(1)
    while (True):
        time_in=time.time()
        print("Muestreando")
        with arduino:
            for k in range(muestras):
                tic = time.time()
                for i in range(numero_de_graficas):
                    try:
                        line = arduino.readline().strip().decode('utf-8')
                        P[i, k] = float(line)
                    except (ValueError, UnicodeDecodeError):
                        # Handle invalid or incomplete data
                        P[i, k] = np.nan
                
                elapsed_time = time.time() - tic
                remaining_time = periodo_muestreo - elapsed_time
                if remaining_time > 0:
                    time.sleep(remaining_time)
        time_end=time.time()-time_in
        print(time_end)
        print("Muestreado finalizado...")
        
        data_string = ','.join(map(str, P[0, 400:]))
        
        # Guardar los datos en un archivo de texto
        with open('datosx.txt', 'a') as file:
            file.write(data_string + '\n')

except serial.SerialException as e:
    print(f"Error opening serial port: {e}")
except KeyboardInterrupt:
    print("Sampling interrupted by the user")
finally:
    if arduino and arduino.is_open:
        arduino.close()