
import cv2
from PIL import ImageTk, Image
import tkinter as tk

# Read image with OpenCV
image = cv2.imread("starry_night.jpg")

# Convert image from BGR to RGB
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Create tkinter window
window = tk.Tk()

# Convert image to PIL format
image_pil = Image.fromarray(image)

# Create tkinter compatible image
image_tk = ImageTk.PhotoImage(image_pil)

# Create label widget to display the image
label = tk.Label(window, image=image_tk)
label.pack()

# Run tkinter event loop
window.mainloop()