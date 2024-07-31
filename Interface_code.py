import numpy as np
import matplotlib.pyplot as plt 
import tkinter as tk
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

# Creamos la ventana de tkinter
root = tk.Tk()
root.geometry("800x600")
root.title("Vectorcardiogram App")
root.iconbitmap("favicon.ico")

# Configuramos un estilo de tema oscuro
root.configure(bg='#212121')
plt.style.use('bmh')

# Creamos el frame principal para la barra lateral y la figura
main_frame = tk.Frame(root)
main_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Creamos el frame de la barra lateral
sidebar_frame = tk.Frame(main_frame, bg="#f0ecec", width=100)
sidebar_frame.pack(side=tk.LEFT, fill=tk.Y)

# Agregamos el título con bordes al frame de la barra lateral
title_frame = tk.Frame(sidebar_frame, bg="#222222")
title_frame.pack(side=tk.TOP, fill=tk.X, padx=15, pady=15)

title_label = tk.Label(title_frame, text='VECTORCARDIOGRAM APP', font=('Roboto', 30, 'bold',), fg='#f0ecec', bg='#333333', padx=5, pady=25, bd=2, relief=tk.SOLID)
title_label.pack(fill=tk.X)

# Creamos la etiqueta de imagen para el logo
logo_frame = tk.Frame(sidebar_frame, bg="#f0ecec")
logo_frame.pack(side=tk.TOP, fill=tk.Y, padx=5, pady=10)

logo_image = Image.open("VECTO.png")
logo_photo = ImageTk.PhotoImage(logo_image)
logo_label = tk.Label(logo_frame, image=logo_photo, bg="#f0ecec", anchor="center")
logo_label.image = logo_photo  # Necesario para evitar que la imagen sea destruida por el recolector de basura
logo_label.pack(fill=tk.BOTH)

# Creamos el marco para el texto descriptivo
desc_frame = tk.Frame(sidebar_frame, bg="#333333", width=100)
desc_frame.pack(side=tk.TOP, fill=tk.X, padx=120, pady=5)

# Creamos el marco para el texto descriptivo
desc_frame1 = tk.Frame(sidebar_frame, bg="#333333", width=100)
desc_frame1.pack(side=tk.TOP, fill=tk.X, padx=120, pady=5)

# Creamos la etiqueta de imagen para el logo2
logo_frame1 = tk.Frame(sidebar_frame, bg="#f0ecec")
logo_frame1.pack(side=tk.TOP, fill=tk.Y, padx=65, pady=10)

logo_image1 = Image.open("FRANK.png")
logo_photo1 = ImageTk.PhotoImage(logo_image1)
logo_label1 = tk.Label(logo_frame1, image=logo_photo1, bg="#f0ecec", anchor="center")
logo_label1.image = logo_photo1  # Necesario para evitar que la imagen sea destruida por el recolector de basura
logo_label1.pack(fill=tk.BOTH)

# Creamos el marco para el texto descriptivo2
desc_frame2 = tk.Frame(sidebar_frame, bg="#333333", width=100)
desc_frame2.pack(side=tk.LEFT, fill=tk.X, padx=20, pady=5)

# Creamos la etiqueta para el texto descriptivo1
desc_label2 = tk.Label(desc_frame2, text='V. 1.0', font=('Roboto', 15), fg='#333333', padx=1, pady=1)
desc_label2.pack(side=tk.LEFT,fill=tk.X)

# Creamos el frame de la figura 3D
figure_frame = tk.Frame(main_frame, bg="#222222")
figure_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)

# Creamos la figura
fig = plt.Figure(figsize=(7, 5), dpi=100)
fig.patch.set_facecolor('#212121') # Fondo de la figura
fig.patch.set_alpha(0.9) # Transparencia de la figura

# Patrón para generar la interactividad
canvas = FigureCanvasTkAgg(fig, master=figure_frame)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Configuramos el borde de la figura para que se parezca al marco lateral
canvas.get_tk_widget().configure(borderwidth=2, relief="solid")

# Cambiamos el color de fondo de la figura
fig.patch.set_facecolor("#333333")

# Creamos el sub-plot de la gráfica en 3D
ax1 = fig.add_subplot(121, projection="3d")

# Ingresa los datos 
x_data = np.loadtxt("datosx.txt",delimiter=',').astype(np.float64)
y_data = np.loadtxt("datosy.txt",delimiter=',').astype(np.float64)
z_data = np.loadtxt("datosz.txt",delimiter=',').astype(np.float64)

# Función que cuenta los picos R durante 1 segundo
contador = 0
for i in range(1, len(x_data)):
    if x_data[i] > 1.4 and x_data[i] > x_data[i-1]:
        contador += 1

heart_rate = (contador/1.5) * 60

# Función que determina la condición del paciente
if heart_rate > 120:
    disturbance = str("Tachycardia")
elif 120 >= heart_rate >= 60:
    disturbance = str("None")
elif heart_rate < 60:
    disturbance = str("Bradycardia")
elif heart_rate == 0:
    disturbance = str("Asystole")

heart = str(heart_rate)

# Creamos la etiqueta para el texto descriptivo
desc_label = tk.Label(desc_frame, text='The heart rate of the patient is: ' + heart + ' bpm', font=('Roboto', 15), fg='#f0ecec', bg='#333333', padx=1, pady=1)
desc_label.pack(fill=tk.X)

# Creamos la etiqueta para el texto descriptivo1
desc_label1 = tk.Label(desc_frame1, text='The cardiac disturbance is: ' + disturbance, font=('Roboto', 15), fg='#f0ecec', bg='#333333', padx=1, pady=1)
desc_label1.pack(fill=tk.X)

# Plot de la gráfica en 3D
ax1.plot(x_data, y_data, z_data, color='blue', linewidth=2)
ax1.set_xlabel('Vx (mV)', color='black')
ax1.set_ylabel('Vy (mV)', color='black')
ax1.set_zlabel('Vz (mV)', color='black')
ax1.tick_params(axis='x', colors='black')
ax1.tick_params(axis='y', colors='black')
ax1.tick_params(axis='z', colors='black')
ax1.w_xaxis.line.set_color("black")
ax1.w_yaxis.line.set_color("black")
ax1.w_zaxis.line.set_color("black")

# Recurso para el tiempo de las gráficas
inicio = 0
fin = 1
paso = 0.0025
numero_de_datos = int((fin - inicio) / paso) 

arreglo_tiempo = np.arange(inicio, fin + paso, paso)[:numero_de_datos]

# Crear subplots de 3 gráficas en 2D
ax2 = fig.add_subplot(3, 2, 2)
ax2.plot(arreglo_tiempo, x_data, color='blue', label='Vx', linewidth=2)
ax2.set_xlabel('T (s)', color='white')
ax2.set_ylabel('Vx (mV)', color='white')
ax2.spines['bottom'].set_color('white')
ax2.spines['left'].set_color('white')
ax2.tick_params(axis='x', colors='white')
ax2.tick_params(axis='y', colors='white')
ax2.legend(facecolor='#303030', edgecolor='#f9c784')

ax3 = fig.add_subplot(3, 2, 4)
ax3.plot(arreglo_tiempo, y_data, color='blue', label='Vy', linewidth=2)
ax3.set_xlabel('T (s)', color='white')
ax3.set_ylabel('Vy (mV)', color='white')
ax3.spines['bottom'].set_color('white')
ax3.spines['left'].set_color('white')
ax3.tick_params(axis='x', colors='white')
ax3.tick_params(axis='y', colors='white')
ax3.legend(facecolor='#303030', edgecolor='#f9c784')

ax4 = fig.add_subplot(3, 2, 6)
ax4.plot(arreglo_tiempo, z_data, color='blue', label='Vz', linewidth=2)
ax4.set_xlabel('T (s)', color='white')
ax4.set_ylabel('Vz (mV)', color='white')
ax4.spines['bottom'].set_color('white')
ax3.spines['left'].set_color('white')
ax4.tick_params(axis='x', colors='white')
ax4.tick_params(axis='y', colors='white')
ax4.legend(facecolor='#303030', edgecolor='#f9c784')

plt.tight_layout()

# Añadir Toolbar para los botones de interactividad
toolbar = NavigationToolbar2Tk(canvas, figure_frame)
toolbar.update()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Mostramos la ventana de tkinter
tk.mainloop()