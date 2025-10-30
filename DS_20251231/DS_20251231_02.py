from tkinter import*
from PIL import Image
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def draw_image1():
    canvas.delete("all")
    canvas.create_rectangle(50, 50, 150, 150, fill="red")

def draw_image2():
    canvas.delete("all")  # 이전 그림 지우기
    canvas.create_oval(200, 80, 300, 180, fill="blue")

def draw_image3():
    global image
    image_path = os.path.join(BASE_DIR, image["image1.png"])
    image

    canvas.delete("all")
    canvas.create_image(20, 20, anchor=NW, image=img)

def draw_image4():
    canvas.delete("all")

root = Tk()
root.title("중간고사 7번")
root.geometry("420x440")

canvas = Canvas(root, width=400, height=320, bg="white")
canvas.pack()

frame = Frame(root)
frame.pack(pady=10)

bt1=Button(frame, text="사각형", command=draw_image1()).pack(side="left", padx=10)
bt2=Button(frame, text="원", command=draw_image2()).pack(side="left", padx=10)
bt3=Button(frame, text="그림",command=draw_image3()).pack(side="left",padx=10)
bt4=Button(frame, text="지우기", command=draw_image4()).pack(side="left",padx=10)

Label(root, text = "버튼을 눌러 도형을 선택하세요.")

root.mainloop()
