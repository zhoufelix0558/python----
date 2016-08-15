from pywinauto import Application
import  time
app = Application()
app.start('notepad.exe')
#app.UntitledNotepad.MenuItem('Edit -> Paste').Select()
app.Notepad.MenuItem('Edit -> Paste').Select()
app.notepad.TypeKeys('Hello World')

time.sleep(1)
app.notepad.TypeKeys('^+{ENTER}')

time.sleep(1)
app.Notepad.MenuItem('File -> Exit').Select()
#OK = 'Cancel'
#about_dlg[OK].Click()
app['Notepad']['Cancel'].Click()


