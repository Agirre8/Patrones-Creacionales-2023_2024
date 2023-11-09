from PIL import Image, ImageTk

# ... tu código ...

# Ruta a la imagen en formato JPG
ruta_imagen_jpg = "ImagenesPizza/champi.jpg"

# Convierte la imagen JPG a formato GIF
imagen_pil = Image.open(ruta_imagen_jpg)
champi_gif = ImageTk.PhotoImage(imagen_pil)

# Usa la imagen en tu interfaz gráfica
tk.Label(self.frame, image=imagen_gif).pack()