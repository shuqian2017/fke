
m tkinter import *
import tkinter.messagebox as messagebox

root = Tk()
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
	self.pack()
	self.createWidgets()
	self.root = root

   def createWidgets(self):
       self.nameInput = Entry(self)
       self.nameInput.pack()
       self.alertButton = Button(self, text='点击按钮', command=self.hello)
       self.alertButton.pack()

   def hello(self):	
       name = self.nameInput.get() or 'WORLD!'						             
       messagebox.showinfo("Message", 'hello, %s' % name)       


# 主程序
app = Application()
app.master.title("欢迎来到王者荣耀")							     
app.mainloop()    # 进入消息循环
