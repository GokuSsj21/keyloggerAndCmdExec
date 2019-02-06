import win32api
import win32console
import win32gui
import pythoncom,pyHook
import os


 
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
    local()
    
def local():
    global data
    if "goodbye" in data:
        os.system('shutdown -s')
        data = ""
    if "notepad" in data:
        os.system('start notepad')
        data = ""
    if "internetexp" in data:
        os.system('start iexplore')
        data = ""
    return True


    


    
hm=pyHook.HookManager()
hm.KeyDown=OnKeyboardEvent                          
hm.HookKeyboard()                                
pythoncom.PumpMessages()
