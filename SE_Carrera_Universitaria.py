import json
import tkinter as tk
from tkinter import messagebox
import pygame
import time

class SistemaExperto:
    def __init__(self, base_conocimiento_path):
        # Cargar la base de conocimiento desde un archivo JSON
        with open(base_conocimiento_path, 'r') as archivo:
            self.reglas = json.load(archivo)

    def obtener_recomendacion(self, respuestas):
        # Evaluar las respuestas del usuario y aplicar las reglas
        recomendaciones = []
        for regla in self.reglas:
            # Permitir coincidencias parciales entre las respuestas y las condiciones
            if any(condicion in respuesta for condicion in regla["condiciones"] for respuesta in respuestas):
                recomendaciones.append(regla["carrera"])

        return recomendaciones if recomendaciones else ["No se encontró una carrera adecuada."]

class Interfaz:
    def __init__(self, sistema):
        self.sistema = sistema
        self.respuestas_usuario = []
        self.preguntas = [
            "¿Te interesa la tecnología?",
            "¿Te consideras creativo/a?",
            "¿Te gusta resolver problemas?",
            "¿Eres bueno/a en matemáticas?",
            "¿Te interesa ayudar a los demás?",
            "¿Te interesan las ciencias naturales?",
            "¿Te gustaría investigar?",
            "¿Prefieres trabajar en equipo?",
            "¿Te interesa la programación?",
            "¿Te gusta liderar proyectos?",
            "¿Eres bueno/a comunicando ideas?",
            "¿Te interesan las humanidades?",
            "¿Te interesa el diseño y la estética?",
            "¿Te gusta resolver problemas complejos?",
            "¿Eres bueno/a con las ciencias sociales?",
            "¿Te interesa la economía?",
            "¿Te gusta trabajar con datos?",
            "¿Te interesan los negocios?",
            "¿Te gusta explorar la naturaleza?",
            "¿Eres bueno/a en biología?",
            "¿Te interesan los deportes?",
            "¿Te gusta escribir y leer?",
            "¿Te interesan los temas de sostenibilidad?",
            "¿Te gustaría trabajar en robótica?",
            "¿Prefieres tareas prácticas a teóricas?",
            "¿Te interesa la psicología clínica?",
            "¿Te gustaría enseñar a otros?",
            "¿Te interesan los videojuegos?",
            "¿Te gusta trabajar en laboratorios?",
            "¿Eres bueno/a en estadística?",
            "¿Te interesan los proyectos industriales?",
            "¿Te gustaría trabajar en el ámbito forense?",
            "¿Te interesan los algoritmos y la inteligencia artificial?",
            "¿Prefieres trabajos creativos?",
            "¿Te interesa la química aplicada?",
            "¿Te gusta resolver problemas de física?",
            "¿Te interesan los temas de conservación ambiental?",
            "¿Te interesan los procesos empresariales?",
            "¿Te gustaría trabajar en campos médicos?",
            "¿Te interesa la biotecnología?",
            "¿Te interesan los sistemas automatizados?"
        ]
        self.indice_pregunta = 0

        self.ventana = tk.Tk()
        self.ventana.title("Sistema Experto")
        self.ventana.geometry("803x635")

        # Mostrar mensaje de bienvenida
        self.mostrar_bienvenida()

        # Fondo
        self.fondo = tk.PhotoImage(file="FondoSE.png")  # Cambia "fondo.png" por la ruta de tu imagen
        self.label_fondo = tk.Label(self.ventana, image=self.fondo)
        self.label_fondo.place(relwidth=1, relheight=1)

        # Pregunta
        self.label_pregunta = tk.Label(self.ventana, text="", font=("Arial", 16), bg="white", wraplength=600, justify="center")
        self.label_pregunta.pack(pady=30)

        # Contenedor de botones
        self.frame_botones = tk.Frame(self.ventana, bg="white")
        self.frame_botones.pack(pady=10)

        # Botones
        self.boton_si = tk.Button(self.frame_botones, text="Sí", font=("Arial", 14), bg="green", fg="white", command=self.responder_si)
        self.boton_si.pack(side="left", padx=20)

        self.boton_no = tk.Button(self.frame_botones, text="No", font=("Arial", 14), bg="red", fg="white", command=self.responder_no)
        self.boton_no.pack(side="right", padx=20)

        # Isla inferior para recomendaciones
        self.frame_recomendaciones = tk.Frame(self.ventana, bg="lightgray")
        self.frame_recomendaciones.pack(side="bottom", fill="x", pady=10)

        self.label_recomendaciones = tk.Label(self.frame_recomendaciones, text="", font=("Arial", 14), bg="lightgray", wraplength=750, justify="center")
        self.label_recomendaciones.pack(pady=5)

        # Iniciar música de fondo
        pygame.init()
        pygame.mixer.music.load("Music.mp3")  # Cambia "musica_fondo.mp3" por la ruta de tu archivo de música
        pygame.mixer.music.play(-1)  # Repetir indefinidamente

        self.mostrar_pregunta()
        self.ventana.mainloop()

    def mostrar_bienvenida(self):
        # Ventana emergente de bienvenida
        ventana_bienvenida = tk.Toplevel()
        ventana_bienvenida.title("Bienvenido")
        ventana_bienvenida.geometry("400x200")

        mensaje = tk.Label(ventana_bienvenida, text="¡Bienvenido al Sistema Experto Vocacional!\nEste programa te ayudará a encontrar una carrera adecuada basada en tus intereses y habilidades.\n\nHaz clic en 'Aceptar' para continuar.", font=("Arial", 12), wraplength=350, justify="center")
        mensaje.pack(pady=20)

        boton_aceptar = tk.Button(ventana_bienvenida, text="Aceptar", font=("Arial", 12), command=ventana_bienvenida.destroy)
        boton_aceptar.pack(pady=10)

        self.ventana.wait_window(ventana_bienvenida)

    def mostrar_pregunta(self):
        if self.indice_pregunta < len(self.preguntas):
            self.label_pregunta.config(text=self.preguntas[self.indice_pregunta])
        else:
            self.mostrar_recomendaciones()

    def responder_si(self):
        # Agregar toda la pregunta como respuesta para asegurar coincidencias con las condiciones del JSON
        pregunta = self.preguntas[self.indice_pregunta].strip('?').lower()
        self.respuestas_usuario.append(pregunta)
        self.indice_pregunta += 1
        self.mostrar_pregunta()

    def responder_no(self):
        self.indice_pregunta += 1
        self.mostrar_pregunta()

    def mostrar_recomendaciones(self):
        recomendaciones = self.sistema.obtener_recomendacion(self.respuestas_usuario)
        resultado = "\n".join(recomendaciones)
        self.label_recomendaciones.config(text=f"Carreras recomendadas:\n{resultado}")
        pygame.mixer.music.stop()  # Detener la música cuando termine

        # Mostrar mensaje de despedida
        self.mostrar_despedida()

    def mostrar_despedida(self):
        ventana_despedida = tk.Toplevel()
        ventana_despedida.title("Despedida")
        ventana_despedida.geometry("400x200")

        mensaje = tk.Label(ventana_despedida, text="¡Gracias por usar el Sistema Experto Vocacional!\n¿Deseas realizar otra encuesta o salir?", font=("Arial", 12), wraplength=350, justify="center")
        mensaje.pack(pady=20)

        boton_otra = tk.Button(ventana_despedida, text="Otra encuesta", font=("Arial", 12), command=lambda: self.reiniciar(ventana_despedida))
        boton_otra.pack(side="left", padx=20, pady=10)

        boton_salir = tk.Button(ventana_despedida, text="Salir", font=("Arial", 12), command=self.ventana.quit)
        boton_salir.pack(side="right", padx=20, pady=10)

        self.ventana.wait_window(ventana_despedida)

    def reiniciar(self, ventana_despedida):
        ventana_despedida.destroy()
        self.respuestas_usuario = []
        self.indice_pregunta = 0
        self.label_recomendaciones.config(text="")
        self.mostrar_pregunta()

# Crear el sistema experto cargando la base de conocimiento desde un archivo JSON
sistema = SistemaExperto('base_conocimiento.json')

# Iniciar la interfaz gráfica
Interfaz(sistema)