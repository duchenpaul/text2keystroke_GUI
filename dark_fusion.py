from PyQt5 import QtCore, QtGui
'''
Add to framework.py:
app.setStyle('Fusion')
import dark_fusion
app.setPalette(dark_fusion.paletteDark)
'''

palette = QtGui.QPalette()

paletteDark = QtGui.QPalette()
paletteDark.setColor(QtGui.QPalette.Window, QtGui.QColor(53,53,53))
paletteDark.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)
paletteDark.setColor(QtGui.QPalette.Base, QtGui.QColor(15,15,15))
paletteDark.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53,53,53))
paletteDark.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.white)
paletteDark.setColor(QtGui.QPalette.ToolTipText, QtCore.Qt.white)
paletteDark.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
paletteDark.setColor(QtGui.QPalette.Button, QtGui.QColor(53,53,53))
paletteDark.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.white)
paletteDark.setColor(QtGui.QPalette.BrightText, QtCore.Qt.red)
paletteDark.setColor(QtGui.QPalette.Highlight, QtGui.QColor(142,45,197).lighter())
paletteDark.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.black)