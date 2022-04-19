# legym-server
The Server Mode Legym automatically check-in Script | 服务版乐健自动打卡脚本（仅限UESTC）
--
## 🚀Updates
- 2022-04-19 Update to legym v0.5 support (because of the port change of legym-App)
--
## 🏗️Requirements:
- 1.Need Python v3.9 or above (Python3.9,3.10 tested)
- 2.This project is based on justcyl/legym module. You must install it to support the script to run.
- 3.This project uses `schedule` module to automatically run rasks. You must install it to support the script.
- 4.For Windows, the script needs Administrator Permission; For Linux, please run it with sudo permission.
## 🎚️How To Deploy?
- 1.Clone this project to any position on your device
- 2.Install legym module.
To install legym module, you can directly install the fork version from the legym-master folder in the project, but we recommend you to install by using pip:
   `pip install -i https://test.pypi.org/simple/ legym==0.5`
- 3.Run the script by terminal:

Linux:
   `nohup python lejian.py YourAccount#YourPassword`

Windows:
   `python lejian.py YourAccount#YourPassword`
## 📢Notice
- 1.The script must keep running to automantically sign up. Windows users may be difficult to keep the script working so we strongly suggest you to deploy a linux server.
- 2.The script doesn't support auto running. Although the module support this function and you can manually use it, we think this function is RISKY and we strongly NOT recommand you to use.
- 3.This project is an open-source project and use GPL3.0 License. We are irresponsible for ANY result of using this project!
## ❤️Thanks To
[legym / ©justcyl / GPL v3.0][1]  

Open sourced under the GPL v3.0 license.

  [1]: https://github.com/justcyl/legym
