from tkinter import*

root = Tk()
root.title("중간고사 5번")

Label("")

entry = Entry(root)
entry.pack()

btn1= Button(root, text = "로그인", command = Label)
btn2 = Button(root, text = "취소", command = root.quit)