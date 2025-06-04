import tkinter
import PIL
from PIL import ImageTk

root=tkinter.Tk()
root.title("my title")
width,height=640,800
width_max,height_max=root.maxsize()
s_center="%dx%d+%d+%d"%(width,height,(width_max-width)/2,(height_max-height)/2)
root.geometry(s_center)
root.resizable(width=False,height=True)

label1=tkinter.Label(root,text="我是一个可以显示文本内容的组件",width=60,height=4,bg='yellow',fg='blue',font=("微软雅黑",12),anchor=tkinter.W)
label1.pack()

var=tkinter.StringVar()
var.set("大家好，我是一个关于文本类型的变量")
label2=tkinter.Label(root,textvariable=var,width=60,height=4,bg='green',fg='white',font=("微软雅黑",12))
label2.pack()

def touch1():
    print("执行一次touch1函数")

def touch2():
    print("点我，按钮是图片")

def touch3():
    if var.get()=="大家好，我是一个关于文本类型的变量":
        var.set("字符已改变，点击复原")
    else:
        var.set("大家好，我是一个关于文本类型的变量")

button1=tkinter.Button(text='文本按钮',width=23,bg='Tan',command=touch1)
button1.pack()


button3=tkinter.Button(root,text="改变文本",command=touch3,width=34,height=2,bg='yellow')
button3.pack()


root.mainloop()