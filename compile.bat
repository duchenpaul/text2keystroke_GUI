SET appName=text2keystroke_gui
pyinstaller .\%appName%.py  --hidden-import PyQt5.sip
rem move dist\%appName%.exe %cd%

rem del /s /f /q  text2keystroke.spec

rem REM walkaround RD bug
rem timeout 1
rem RD /S /Q   dist\ build\