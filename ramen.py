import os
import subprocess

# Stable Diffusionの実行ファイルへのパス
stable_diffusion_path = r'C:\path\to\your\stable_diffusion\stable_diffusion.exe'

# ショートカットを作成するためのパス
shortcut_path = r'C:\path\to\your\shortcut.lnk'

def create_shortcut(target, shortcut):
    shell = os.path.join(os.path.expandvars('%windir%'), 'System32', 'wscript.exe')
    vbs_script = f"""
    Set objShell = CreateObject("WScript.Shell")
    Set lnk = objShell.CreateShortcut("{shortcut}")
    lnk.TargetPath = "{target}")
    lnk.Save()
    """
    vbs_temp = os.path.join(os.path.expandvars('%temp%'), 'create_shortcut.vbs')
    with open(vbs_temp, 'w') as file:
        file.write(vbs_script)
    subprocess.run([shell, vbs_temp])
    os.remove(vbs_temp)

create_shortcut(stable_diffusion_path, shortcut_path)
