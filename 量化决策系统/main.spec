# -*- mode: python -*-

block_cipher = None


a = Analysis(['main.py', 'MainWindow.py', 'One_Prob_thread.py', 'Top_Eight_thread.py'],
             pathex=['/home/david/PycharmProjects/量化决策系统'],
             binaries=[],
             datas=[('/home/david/PycharmProjects/量化决策系统/softprob.model','DATA')],
             hiddenimports=[],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          name='main',
          debug=False,
          strip=False,
          upx=True,
          console=False )
