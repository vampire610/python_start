import os
import subprocess
os.system('start "" "D:\Program Files\Clash Verge\Clash Verge.exe"')
os.system('start "" "D:\Program Files\Proxifier\Proxifier.exe"')
# 指定要打开的浏览器路径
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# 要访问的网址
url = "https://poe.com/"

# 使用 subprocess 打开指定浏览器
subprocess.Popen([chrome_path, url])


# 生成带图标的exe:
# pyinstaller -Fw -i icon.ico main.py