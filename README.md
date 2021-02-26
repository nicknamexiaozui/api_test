#质量保证部

##声明：

本项目适用于一键文件和哈希存证，仅用于测试和学习研究，

##运行环境

* python3
* pip install requests

##使用教程
###文件存证
1.修改数据文件userdata.py

2.运行cunzheng_main.py

>在userdata.py数据文件基础上做对应修改
>
>注意：修改证书cert数据时，注意换行。在什么情况下请查看证书文件内容
>
>修改file_path值，可以上传不同文件
>
>运行结果提示成功，则可登录企业端系统查看证据库。
###哈希存证
1.修改数据文件userdata.py，保持用户数据的一致性
>在userdata.py数据文件基础上做对应修改
>
>不用修改file_path，file_path在摘要存证时未被使用

2..修改cunzheng.py下file_hash和file_name的值，并保持file_hash为32位

3..运行cunzheng.py
>运行结果提示成功，则可登录企业端系统查看证据库。
