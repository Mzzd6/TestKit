netsh interface ip set address "以太网" static 10.87.225.178 255.255.255.224 10.87.225.190

netsh interface ip set dns "以太网" static 10.87.13.86 primary

netsh interface ip add dns "以太网" 10.87.13.87

::修改本地以太网地址，以太网也可以改为WLAN
::平时办公处于内网，网络环境时常变更，所以才有了这个脚本
::请使用管理员身份运行