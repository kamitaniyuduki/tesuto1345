import os
import subprocess

# 実行したい画像生成AIのファイルパス
file_path = r'C:\path\to\your\ai\software.exe'

# ショートカットを作成するためのパス
shortcut_path = r'C:\path\to\your\shortcut.lnk'

def create_shortcut(target, shortcut):
    shell = os.path.join(os.path.expandvars('%windir%'), 'System32', 'wscript.exe')
    vbs_script = f"""
    Set objShell = CreateObject("WScript.Shell")
    Set lnk = objShell.CreateShortcut("{shortcut}")
    lnk.TargetPath = "{target}"
    lnk.Save()
    """
    vbs_temp = os.path.join(os.path.expandvars('%temp%'), 'create_shortcut.vbs')
    with open(vbs_temp, 'w') as file:
        file.write(vbs_script)
    subprocess.run([shell, vbs_temp])
    os.remove(vbs_temp)

create_shortcut(file_path, shortcut_path)
