

from pywinauto.application import Application
import time

app = Application().Start(cmd_line=u'"C:\\Program Files (x86)\\MELSOFT\\MRC2\\MR2.exe" ')
#找到主界面的窗口
time.sleep(3)
afx = app[u'MELSOFT MR Configurator2 \u65b0\u5de5\u7a0b']
start_dlg = app.window_(title_re = 'MELSOFT MR Configurator2', class_name = '#32770')
start_dlg.SetFocus()
start_dlg.TypeKeys('{TAB}')
start_dlg.TypeKeys('{ENTER}')
#通过ALt进入“程序运行(R)”界面
afx.TypeKeys('%E',pause=0.5)
afx.TypeKeys('{DOWN 4}')
afx.TypeKeys('{ENTER}')

#找到确认的界面
start_dlg = app.window_(title_re = 'MELSOFT MR Configurator2', class_name = '#32770')
start_dlg.TypeKeys('{ENTER}')

#进入“程序运行”的命令窗口
#comm_window = app.window_(title_re = u'程序运行',class_name = 'AfxFrameOrView100u')
dlg = afx[u'\u7a0b\u5e8f\u8fd0\u884c']
#dlg.Minimize()         窗口成功最小化
#button.Click()

#dlg1 = dlg['nihao']        The control does not have a __getitem__ method for item access (i.e. ctrl[key]) so maybe you have requested this in erro

#编辑程序
dlg.SetFocus() #窗口置最前面，键盘可以对齐操作。原来这一步操作的话就嗯那个成功，快哭了。。。。
#dlg.TypeKeys('{TAB}')
#dlg.TypeKeys('{ENTER}')
time.sleep(0.5)#
dlg.TypeKeys('%F',pause=0.5)
dlg.TypeKeys('{ENTER}')
edit= app.window_(title_re = u'Open')
edit.TypeKeys('TestCode.prg2')
edit.TypeKeys('{ENTER 3}')
afxabd = app[u'Afx:00310000:8:00010003:00000000:07AB138D']
button = afxabd.Button2
button.Click()

time.sleep(20)
app.Kill_()






