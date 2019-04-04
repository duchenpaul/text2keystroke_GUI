# -*- mode: python -*-

block_cipher = None


a = Analysis(['text2keystroke_gui.py'],
             pathex=['C:\\Users\\chdu\\Desktop\\Portal\\Other\\text2keystroke_GUI'],
             binaries=[],
             datas=[("src\\wipe.svg", "src"), ("config_sample.ini", ".")],
             hiddenimports=['PyQt5.sip'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)


pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='text2keystroke_gui',
          debug=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='text2keystroke_gui')

