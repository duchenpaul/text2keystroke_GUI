SET appName=text2keystroke_gui
pyinstaller --noconfirm text2keystroke_gui.spec
rem pyinstaller --noconfirm .\%appName%.py --windowed --hidden-import PyQt5.sip  
rem move dist\%appName%.exe %cd%

rem del /s /f /q  text2keystroke.spec

REM walkaround RD bug
rem timeout 1
rem RD /S /Q   dist\ build\