from Tkinter import *
import ScrolledText as tkst

def create_app(sock):
  root = Tk()
  main = Application(master=root, sock=sock)
  root.bind('<Return>', main.enter_text)
  return root, main

def start_app(root, main):
  main.mainloop()
  root.destroy()

class Application(Frame):
    def enter_text(self, event=None):
        message = self.entry.get()
        if len(message) > 0:
          try:
            self.socket.send(message)
          except:
            print 'Server disconnected.'
        self.entry.delete(0, END)
    
    def get_text(self, message):
      if len(message) > 0:
        self.scrolltext.configure(state='normal')
        self.scrolltext.insert(END, message + '\n')
        self.scrolltext.configure(state='disable')
        self.scrolltext.see("end")

    def createWidgets(self):
        self.scrolltext = tkst.ScrolledText(self, wrap='word')
        self.scrolltext["height"] = 10
        self.scrolltext["width"] = 50
        self.scrolltext.configure(state='disable')
        self.scrolltext.pack()
        
        self.entry = Entry(self)
        self.entry.pack({"side": "left"})
        
        self.enter_button = Button(self)
        self.enter_button["text"] = "Enter",
        self.enter_button["command"] = self.enter_text
        self.enter_button.pack({"side": "left"})
        
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["command"] =  self.quit   
        self.QUIT.pack({"side": "left"})
        
    def test(self, event, arg):
      print arg

    def __init__(self, master=None, sock=None):
        Frame.__init__(self, master)
        self.socket = sock
        self.pack()
        self.createWidgets()

