import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import math
import pygame
ventana_sec = False
def al_cerrar(instancia_a_cerrar):
    global ventana_sec
    ventana_sec = False  # 1. Liberamos el permiso primero
    instancia_a_cerrar.grab_release() # Por si acaso hubiera un bloqueo
    instancia_a_cerrar.destroy() # 2. Matamos la ventana



#----------------------------------------------------------------------------------------------------------------------------------
#Ventana de los nuemros
def Numeros():
    global ventana_sec
    ventana_numeros = tk.Toplevel(ventana)
    ventana_numeros.grab_set()
    ventana_numeros.title("Numeros enteros")
    ventana_numeros.geometry("800x600")
    ventana_numeros.resizable(width=False, height=False)
    
    btn_cerrar = tk.Button(ventana_numeros, text="Regresar", command=lambda: al_cerrar(ventana_numeros), bg="red", fg="white", font=("Arial", 10, "bold"))
    btn_cerrar.place(x=360, y=400)

    tk.Label(ventana_numeros, text="Porfavor, ingrese un numero entero", font=("Arial", 20, "bold"), fg="black", bg="pink").pack(pady=20)

    n_entero = tk.Entry(ventana_numeros)
    n_entero.pack(pady=5)

    resultado_pares = tk.Text(ventana_numeros, height=7, width=40)
    resultado_pares.pack(pady=10)
    
    boton_pares = tk.Button(ventana_numeros, text = 'Mostrat pares', command=lambda:ejecutar_calculo(), bg="green", fg="white", font=("Arial", 10, "bold"))
    boton_pares.place(x=350, y=300)

    def buscar_pares_recursivo(n, i, acumulador):
        num_abs = abs(n)
        pareja = num_abs // i
        
        # CASO BASE: Si el divisor supera a la pareja, detenemos para no repetir invertidos
        if i > pareja:
            return acumulador
        
        if num_abs % i == 0:
            par = f"({i}, {pareja})"
            # Concatenamos al acumulador
            nuevo_acumulador = par if acumulador == "" else acumulador + ", " + par
            return buscar_pares_recursivo(n, i + 1, nuevo_acumulador)
        else:
            # Si no es divisor, pasamos al siguiente número
            return buscar_pares_recursivo(n, i + 1, acumulador)

    # --- FUNCIÓN QUE SE EJECUTA AL TOCAR EL BOTÓN ---
    def ejecutar_calculo():
        try:
            # Ahora la función buscará estas variables en el nivel superior de Numeros()
            resultado_pares.delete('1.0', tk.END)
            valor_texto = n_entero.get().strip()
            
            if not valor_texto:
                messagebox.showwarning("Atención", "El campo está vacío.")
                return
                
            valor = int(valor_texto)
            
            if valor == 0:
                resultado_pares.insert(tk.END, "Infinitos pares: (0, x)")
                return

            # Llamada a la recursión
            resultado_final = buscar_pares_recursivo(valor, 1, "")
            
            if not resultado_final:
                resultado_pares.insert(tk.END, "No hay pares divisores.")
            else:
                resultado_pares.insert(tk.END, resultado_final)

        except ValueError:
            messagebox.showerror("Error", "Debe ingresar solo números enteros.")
        except RecursionError:
            messagebox.showerror("Error", "Número demasiado grande.")

#----------------------------------------------------------------------------------------------------------------------------------

#Ventana de la ficha personal
def Ficha_Personal(): 
    global ventana_sec
   
    ventana_ficha = tk.Toplevel(ventana)
    ventana_ficha.grab_set()
    ventana_ficha.title("Ficha Personal")
    ventana_ficha.geometry("800x600")
    ventana_ficha.resizable(width=False, height=False)
    btn_cerrar = tk.Button(ventana_ficha, text="Regresar", command=lambda: al_cerrar(ventana_ficha), bg="red", fg="white", font=("Arial", 10, "bold"))
    btn_cerrar.place(x=600, y=500)
    

    label_ficha = tk.Label(ventana_ficha, text="Ficha personal del programador", font=("Arial", 20, "bold"), fg="black", bg="pink")
    label_ficha.pack(pady=10)
    
    label_info = tk.Label(ventana_ficha, text=" Nombre: Emanuel Gutiérrez Moreira\n Carnet: 2026091141\n Edad: 18 Años\n \n Biografía:\n Soy un estudiante de primer ingreso del TEC;\n Mis sagas de vieojuegos favoritas son: Red Dead Rdemtion,\n Grand Theft Auto y God of War;\n se armar distintos cubos de Rubik a pesar de no ser tan rápido en\n ello; Soy proveniente del Cantón de Abangares en Guanacaste;\n Mis géneros musicales favoritos son el reggae, dancehall, rap y\n rancheras. ",font=("Arial", 10, "bold"), justify= "left")
    label_ficha =tk.Label(ventana_ficha, font=("Arial", 20, "bold"))
    label_info.place(x=40, y=90)

    label_musica = tk.Label(ventana_ficha, text= "Interprete Favorito: Barrington Levy\nGenero musical: Reggae y Dancehall\n",justify= "left", font=("Arial", 10, "bold"))
    label_musica.place(x=40, y=330)


    foto_home = tk.PhotoImage(file="Departamento.png")
    foto_peq = foto_home.subsample(5, 5)
    label_foto_h = tk.Label(ventana_ficha, image=foto_peq)
    label_foto_h.image = foto_peq
    label_foto_h.place(x=600, y=80)

    foto_Ema = tk.PhotoImage(file="Imagen_Ema.png")
    foto_peq2 = foto_Ema.subsample(5, 5)
    label_foto_E = tk.Label(ventana_ficha, image=foto_peq2)
    label_foto_E.image = foto_peq2
    label_foto_E.place(x=600, y=250)

    foto_B_L = tk.PhotoImage(file="Cantante.png")
    foto_peq3 = foto_B_L.subsample(7, 7)
    label_foto_B_L= tk.Label(ventana_ficha, image=foto_peq3)
    label_foto_B_L.image = foto_peq3
    label_foto_B_L.place(x=300, y=300)

    pygame.mixer.init()
    cancion = pygame.mixer.Sound("Murderer.mp3")

    def play_cancion():
        cancion.stop()
        cancion.play()
        
    btn_cancion = tk.Button(ventana_ficha, text="Escuchar canción", command=play_cancion,bg="purple", fg="white")
    btn_cancion.place(x=60, y=400)

#----------------------------------------------------------------------------------------------------------------------------------
#Ventana de las pelotas que rebotan
def Pelotas():
    global ventana_sec
    ventana_sec = True
    ventana_pelotas= tk.Toplevel(ventana)
    ventana_pelotas.grab_set()
    ventana_pelotas.title("Pelotas que rebotan")
    ventana_pelotas.geometry("800x600")
    ventana_pelotas.resizable(width=False, height=False)

    label_pelotas = tk.Label(ventana_pelotas, text="Pelotas que rebotan contra todo", font=("Arial", 20, "bold"), fg="black", bg="pink")
    label_pelotas.pack(pady=20)
    # Regulador de Velocidad
    velocidad_var = tk.DoubleVar(value=1.0)
    tk.Scale(ventana_pelotas, from_=0.1, to=3.0, resolution=0.1, 
             orient=tk.HORIZONTAL, label="Velocidad de Simulación",
             variable=velocidad_var, length=300).pack(pady=5)

    # Canvas
    ancho_c, alto_c = 750, 400 
    canvas = tk.Canvas(ventana_pelotas, width=ancho_c, height=alto_c, 
                       bg="#fdfdfd", highlightthickness=2, highlightbackground="purple")
    canvas.pack(pady=5)

    # Lista de pelotas idénticas
    bolas = [
        {'x': 200, 'y': 200, 'r': 30, 'vx': 4, 'vy': 2, 'color': '#ff5555', 'm': 30},
        {'x': 550, 'y': 200, 'r': 30, 'vx': -4, 'vy': -2, 'color': '#5555ff', 'm': 30}
    ]

    def resolver_colision(b1, b2):
        dx = b2['x'] - b1['x']
        dy = b2['y'] - b1['y']
        distancia = math.hypot(dx, dy)

        if distancia < (b1['r'] + b2['r']):
            nx, ny = dx / distancia, dy / distancia
            v_rel_x, v_rel_y = b1['vx'] - b2['vx'], b1['vy'] - b2['vy']
            vel_normal = v_rel_x * nx + v_rel_y * ny

            if vel_normal > 0: return

            impulso = (2 * vel_normal) / (b1['m'] + b2['m'])
            b1['vx'] -= impulso * b2['m'] * nx
            b1['vy'] -= impulso * b2['m'] * ny
            b2['vx'] += impulso * b1['m'] * nx
            b2['vy'] += impulso * b1['m'] * ny

            # Separación para evitar pegado
            traslape = (b1['r'] + b2['r']) - distancia + 0.5
            b1['x'] -= (traslape / 2) * nx
            b1['y'] -= (traslape / 2) * ny
            b2['x'] += (traslape / 2) * nx
            b2['y'] += (traslape / 2) * ny

    # --- FUNCIÓN RECURSIVA PARA PROCESAR LAS PELOTAS ---
    def procesar_pelotas_recursivo(indice):
        # Caso base: Si el índice llega al tamaño de la lista, terminamos la recursión
        if indice >= len(bolas):
            return

        b = bolas[indice]
        factor = velocidad_var.get()

        # Actualizar posición física
        b['x'] += b['vx'] * factor
        b['y'] += b['vy'] * factor

        # Rebotes en bordes
        if b['x'] - b['r'] <= 0 or b['x'] + b['r'] >= ancho_c:
            b['vx'] *= -1
        if b['y'] - b['r'] <= 0 or b['y'] + b['r'] >= alto_c:
            b['vy'] *= -1

        # Dibujar en el canvas
        canvas.create_oval(b['x']-b['r'], b['y']-b['r'], 
                           b['x']+b['r'], b['y']+b['r'], 
                           fill=b['color'], tags="pelota", outline="black", width=2)

        # Llamada recursiva para la siguiente pelota
        procesar_pelotas_recursivo(indice + 1)

    def animar():
        if not ventana_sec: return 
        
        canvas.delete("pelota")
        
        # Primero resolvemos la colisión entre las dos (Lógica física)
        resolver_colision(bolas[0], bolas[1])

        # Luego procesamos el movimiento y dibujo usando RECURSIVIDAD
        procesar_pelotas_recursivo(0)

        ventana_pelotas.after(16, animar)

    # Botón de cierre
    tk.Button(ventana_pelotas, text="Regresar", command=lambda: al_cerrar(ventana_pelotas), 
              bg="red", fg="white", font=("Arial", 10, "bold")).pack(pady=10)

    animar()
#----------------------------------------------------------------------------------------------------------------------------------
#Ventana principal
ventana = tk.Tk()
ventana.title('Tarea GUI')
ventana.geometry("1100x400")
ventana.resizable(width=False, height=False)

label = tk.Label(ventana, text= 'HOLA!, ESCOJA QUE QUIERE HACER: ', font=("Arial",20, "bold"), fg="black", bg="pink")
label.pack(pady=20)

canva1 = tk.Canvas(ventana, bg="light blue", width=2100, height=2000)
canva1.pack()
#Botones ventna principal
boton1 = tk.Button(ventana, text ='Pares ordenados', command=lambda:Numeros(), bg="white", width=15, height=1, font=("Arial", 10, "bold"))
boton1.place(x=100, y=200)

boton2 = tk.Button(ventana, text ='Ficha personal', command=lambda:Ficha_Personal(), bg="white", width=15, height=1, font=("Arial", 10, "bold"))
boton2.place(x=450, y=200)

boton3 = tk.Button(ventana, text = 'Animación', command=lambda:Pelotas(), bg="white", width=15, height=1, font=("Arial", 10, "bold"))
boton3.place(x=800, y=200)

boton4 = tk.Button(ventana, text = 'Cerrar', command=lambda:cerrar_ventana(), bg="red", fg="white", width=5, height=1,font=("Arial", 10, "bold"))
boton4.place(x=490, y=260)

def cerrar_ventana():
    print("Cerrando ventana")
    ventana.destroy()
#----------------------------------------------------------------------------------------------------------------------------------



ventana.mainloop()

