# legym-server
The Server Mode Legym automatically check-in Script | 服务版乐健自动打卡脚本（仅限UESTC）
--
## Requirements:
- 1.Need Python v3.9 or above
- 2.This project is based on justcyl/legym module.You must install it to support the script to run.
- 3.For Windows, the script needs Administrator Permission; For Linux, please run it with sudo permission.
## How To Deploy?
- 1.Clone this project to any position on your device
- 2.Install legym module.
To install legym module, you can directly install the fork version from the legym-master folder in the project, but we recommend you to install by using pip:
   `pip install -i https://test.pypi.org/simple/ legym==0.3`
- 3.Run the script by terminal:
Linux:
   `nohup python lejian.py YourAccount#YourPassword`
Windows:
   `python lejian.py YourAccount#YourPassword`
