from threading import Thread 
import sys,time,os
try:
    import tkinter as tk
except ImportError:
    import tkinter as tk
val, w, root,w_win="None"
try:
    from tkinter import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    # auto_messenger_final_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    # auto_messenger_final_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None


BOT_STARTTED=False 
BOTWORKCOMPLETED=False


from selenium import webdriver
import time,os,uuid,json,re,sched, timeit
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from auto_messenger import BOT_THREAD_STARTER

 
 



chrome_options = Options()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('log-level=3')
chrome_options.add_argument('disable-notifications')
driver=None


class MyThread(Thread):
     def __init__(self,thread,emailfield,passwordfield,fbidfield,maxcontactsfield,maxwaitfield):
          Thread.__init__(self)
          self.thread=thread
          self.emailfield=emailfield
          self.passwordfield=passwordfield
          self.fbidfield=fbidfield
          self.maxcontactsfield=maxcontactsfield
          self.maxwaitfield=maxwaitfield
        #   self.btnreplica=btnreplica
          
     def run(self):
        global BOTWORKCOMPLETED, driver,BOT_STARTTED
        BOTWORKCOMPLETED=True
        driver = webdriver.Chrome(executable_path=os.path.join(os.getcwd(),'chromedriver.exe'),options=chrome_options)
        bot_status = BOT_THREAD_STARTER(driver=driver,EMAILID=self.emailfield,PASSWORD=self.passwordfield,your_id=self.fbidfield,minimum_contacts=self.maxcontactsfield,max_wait_for_reply=self.maxwaitfield)  
        if bot_status is True or bot_status is False:
            # self.btnreplica.configure(background="#6bbb1c")
            # self.btnreplica.configure(text='''Start''') 
            BOT_STARTTED=False 
            BOTWORKCOMPLETED=False
            driver.quit()
        print("thread")
          
          
          
     def stop(self):
          self.thread_running = False
class QUITDRIVER(Thread):
     def __init__(self):
          Thread.__init__(self)
 
          
     def run(self):
        global BOTWORKCOMPLETED, driver,BOT_STARTTED

        BOT_STARTTED=True
        BOTWORKCOMPLETED=True
        try:driver.quit()
        except:pass
          
     def stop(self):
          self.thread_running = False











































class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.thread = None
        self.thread2 = None
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont ")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("928x542")
        # top.geometry("928x542+-1131+87")
        top.minsize(120, 1)
        top.maxsize(2650, 1005)
        top.resizable(0,  0)
        top.title("Auto Messenger")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#f0f0f0f0f0f0")
        top.configure(highlightcolor="black")

        self.Labelframe1 = tk.LabelFrame(top)
        self.Labelframe1.place(relx=0.017, rely=0.022, relheight=0.945
                , relwidth=0.962)
        self.Labelframe1.configure(relief='groove')
        self.Labelframe1.configure(font="-family {Segoe UI} -size 10")
        self.Labelframe1.configure(foreground="#001705")
        self.Labelframe1.configure(text='''Auto Messenger''')
        self.Labelframe1.configure(background="#d9d9d9")
        self.Labelframe1.configure(highlightbackground="#d9d9d9")
        self.Labelframe1.configure(highlightcolor="#000000")

        self.Labelframe2 = tk.LabelFrame(self.Labelframe1)
        self.Labelframe2.place(relx=0.011, rely=0.047, relheight=0.141
                , relwidth=0.973, bordermode='ignore')
        self.Labelframe2.configure(relief='groove')
        self.Labelframe2.configure(foreground="black")
        self.Labelframe2.configure(text='''Enter Email''')
        self.Labelframe2.configure(background="#d9d9d9")
        self.Labelframe2.configure(highlightbackground="#d9d9d9")
        self.Labelframe2.configure(highlightcolor="black")

        self.emailfield = ttk.Entry(self.Labelframe2,font=("-family {Segoe UI} -size 13"))
        self.emailfield.place(relx=0.013, rely=0.292, relheight=0.569
                , relwidth=0.974, bordermode='ignore')
        self.emailfield.configure(takefocus="")
        self.emailfield.configure(cursor="ibeam")

        self.Labelframe2_1 = tk.LabelFrame(self.Labelframe1)
        self.Labelframe2_1.place(relx=0.011, rely=0.219, relheight=0.141
                , relwidth=0.973, bordermode='ignore')
        self.Labelframe2_1.configure(relief='groove')
        self.Labelframe2_1.configure(foreground="black")
        self.Labelframe2_1.configure(text='''Enter Password''')
        self.Labelframe2_1.configure(background="#d9d9d9")
        self.Labelframe2_1.configure(highlightbackground="#d9d9d9")
        self.Labelframe2_1.configure(highlightcolor="black")

        self.passwordfield = ttk.Entry(self.Labelframe2_1,show="*",font=("-family {Segoe UI} -size 13"))
        # self.passwordfield = ttk.Entry(self.Labelframe2_1,font=("-family {Segoe UI} -size 13"))
        self.passwordfield.place(relx=0.013, rely=0.292, relheight=0.569
                , relwidth=0.974, bordermode='ignore')
        self.passwordfield.configure(takefocus="")
        self.passwordfield.configure(cursor="ibeam")

        self.Labelframe2_2 = tk.LabelFrame(self.Labelframe1)
        self.Labelframe2_2.place(relx=0.011, rely=0.391, relheight=0.141
                , relwidth=0.973, bordermode='ignore')
        self.Labelframe2_2.configure(relief='groove')
        self.Labelframe2_2.configure(foreground="black")
        self.Labelframe2_2.configure(text='''Enter Facebook ID''')
        self.Labelframe2_2.configure(background="#d9d9d9")
        self.Labelframe2_2.configure(highlightbackground="#d9d9d9")
        self.Labelframe2_2.configure(highlightcolor="black")

        self.fbidfield = ttk.Entry(self.Labelframe2_2,font=("-family {Segoe UI} -size 13"))
        self.fbidfield.place(relx=0.013, rely=0.292, relheight=0.569
                , relwidth=0.974, bordermode='ignore')
        self.fbidfield.configure(takefocus="")
        self.fbidfield.configure(cursor="ibeam")

        self.Labelframe2_3 = tk.LabelFrame(self.Labelframe1)
        self.Labelframe2_3.place(relx=0.011, rely=0.564, relheight=0.246
                , relwidth=0.973, bordermode='ignore')
        self.Labelframe2_3.configure(relief='groove')
        self.Labelframe2_3.configure(foreground="black")
        self.Labelframe2_3.configure(text='''Set Configurations''')
        self.Labelframe2_3.configure(background="#d9d9d9")
        self.Labelframe2_3.configure(highlightbackground="#d9d9d9")
        self.Labelframe2_3.configure(highlightcolor="black")

        self.Labelframe2_1_1 = tk.LabelFrame(self.Labelframe2_3)
        self.Labelframe2_1_1.place(relx=0.012, rely=0.214, relheight=0.651
                , relwidth=0.473, bordermode='ignore')
        self.Labelframe2_1_1.configure(relief='groove')
        self.Labelframe2_1_1.configure(foreground="black")
        self.Labelframe2_1_1.configure(text='''Enter number of Contacts to be Targetted''')
        self.Labelframe2_1_1.configure(background="#d9d9d9")
        self.Labelframe2_1_1.configure(highlightbackground="#d9d9d9")
        self.Labelframe2_1_1.configure(highlightcolor="black")

        self.maxcontactsfield = ttk.Entry(self.Labelframe2_1_1,font=("-family {Segoe UI} -size 13"))
        self.maxcontactsfield.place(relx=0.024, rely=0.293, relheight=0.512
                , relwidth=0.949, bordermode='ignore')
        self.maxcontactsfield.configure(takefocus="")
        self.maxcontactsfield.configure(cursor="ibeam")

        self.Labelframe2_1_1_1 = tk.LabelFrame(self.Labelframe2_3)
        self.Labelframe2_1_1_1.place(relx=0.517, rely=0.214, relheight=0.651
                , relwidth=0.471, bordermode='ignore')
        self.Labelframe2_1_1_1.configure(relief='groove')
        self.Labelframe2_1_1_1.configure(foreground="black")
        self.Labelframe2_1_1_1.configure(text='''Maximum wait for User Reply ( seconds )''')
        self.Labelframe2_1_1_1.configure(background="#d9d9d9")
        self.Labelframe2_1_1_1.configure(highlightbackground="#d9d9d9")
        self.Labelframe2_1_1_1.configure(highlightcolor="black")

        self.maxwaitfield = ttk.Entry(self.Labelframe2_1_1_1,font=("-family {Segoe UI} -size 13"))
        self.maxwaitfield.place(relx=0.024, rely=0.293, relheight=0.512
                , relwidth=0.954, bordermode='ignore')
        self.maxwaitfield.configure(takefocus="")
        self.maxwaitfield.configure(cursor="ibeam")
        self.maxwaitfield.delete(0,tk.END)
        self.maxwaitfield.insert(0,"30")

        cred_path=os.path.join(os.getcwd(),'credentials.txt')
        creds=[]
        if os.path.exists(cred_path):
            with open(cred_path, 'r') as file:
                for line in file.readlines():
                    creds.append(str(line).strip())
            
            self.emailfield.delete(0,tk.END)
            self.emailfield.insert(0,str(creds[0]))
            self.passwordfield.delete(0,tk.END)
            self.passwordfield.insert(0,str(creds[1]))
            self.fbidfield.delete(0,tk.END)
            self.fbidfield.insert(0,str(creds[2]))
            self.maxcontactsfield.delete(0,tk.END)
            self.maxcontactsfield.insert(0,str(creds[3]))
            self.maxwaitfield.delete(0,tk.END)
            self.maxwaitfield.insert(0,str(creds[-1]))
            
          
            
            
            print(creds)
        else: 
            pass
        # ContactFetcher(driver,int(your_id),int(minimum_contacts))

        def Validation():
            if self.emailfield.get()=='':
                self.emailfield.delete(0,tk.END)
                self.emailfield.insert(0,"Invalid Input")
                return False
            # else:return True
            elif self.passwordfield.get()=='' :
                self.passwordfield.delete(0,tk.END)
                self.passwordfield.insert(0,"Invalid Input")
                return False
            # else:return True
            elif self.fbidfield.get()=='' or not str(self.fbidfield.get()).isnumeric():
                self.fbidfield.delete(0,tk.END)
                self.fbidfield.insert(0,"Invalid Input")
                return False
            # else:return True
            elif self.maxcontactsfield.get()=='' or not str(self.maxcontactsfield.get()).isnumeric():
                self.maxcontactsfield.delete(0,tk.END)
                self.maxcontactsfield.insert(0,"Invalid Input")
                return False
            # else:return True
            elif self.maxwaitfield.get()=='' or not str(self.maxwaitfield.get()).isnumeric():
                self.maxwaitfield.delete(0,tk.END)
                self.maxwaitfield.insert(0,"Invalid Input")
                return False
            else:return True
  





        # self.btnreplica=""
            
        def launch_thread(self):
            if self.thread:
                print("thread already launched")
            else:
                print("thread launched")
                self.thread = MyThread(thread=self.thread,emailfield=self.emailfield.get(),passwordfield=self.passwordfield.get(),fbidfield=self.fbidfield.get(),maxcontactsfield=self.maxcontactsfield.get(),maxwaitfield=self.maxwaitfield.get())
                self.thread.start()

        def stop_thread(self):
            if self.thread:
                self.thread.stop()
                self.thread = None
            else:
                print("no thread running")


            
        def launch_thread2(self):
            if self.thread2:
                print("thread already launched")
            else:
                print("thread launched")
                self.thread2 = QUITDRIVER()
                self.thread2.start()

        def stop_thread2(self):
            if self.thread2:
                self.thread2.stop()
                self.thread2 = None
            else:
                print("no thread running")



        def Controller():
            global BOT_STARTTED,driver
            if Validation() is True and BOT_STARTTED is False:
                cred_path=os.path.join(os.getcwd(),'credentials.txt')
                with open(cred_path, 'w') as file:
                    file.seek(0)
                    file.truncate()
                    file.write(str(self.emailfield.get())+'\n')
                    file.write(str(self.passwordfield.get())+'\n')
                    file.write(str(self.fbidfield.get())+'\n')
                    file.write(str(self.maxcontactsfield.get())+'\n')
                    file.write(str(self.maxwaitfield.get())+'\n')


                BOT_STARTTED=True
                print(BOT_STARTTED)
                self.Button1.configure(background="red")
                self.Button1.configure(text='''Stop''')
                if not self.thread:
                    launch_thread(self)
                else:
                    # root.destroy()
                    # os.startfile("gui.py")
                    launch_thread2(self)
                    stop_thread(self)
                    stop_thread2(self)
                print(self.emailfield.get())
                print(self.passwordfield.get())
                print(self.fbidfield.get())
                print(self.maxcontactsfield.get())
                print(self.maxwaitfield.get())
                # BOT_STARTTED=False
            
            elif BOT_STARTTED is True:

                self.Button1.configure(background="#6bbb1c")
                self.Button1.configure(text='''Start''')
                launch_thread2(self)
                stop_thread(self)
                stop_thread2(self)
                BOT_STARTTED=False
                print("_____") 
                # print(driver.quit()) 
                print("_____")
                stop_thread(self)
            






            
            

        self.Button1 = tk.Button(self.Labelframe1,command=Controller)
        self.Button1.place(relx=0.403, rely=0.861, height=44, width=177
                , bordermode='ignore')
        self.Button1.configure(activebackground="#8a8a8a")
        self.Button1.configure(activeforeground="black")
        self.Button1.configure(background="#6bbb1c")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Segoe UI Light} -size 15 -weight bold")
        self.Button1.configure(foreground="#333333")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(relief="flat")
        self.Button1.configure(text='''Start''') 

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

if __name__ == '__main__':
    vp_start_gui()





