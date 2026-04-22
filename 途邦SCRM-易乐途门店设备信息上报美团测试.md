---
date: 2026-04-02
tags:
  - 途邦
  - 易乐途
  - 美团
  - 测试
---
### 测试环境如何模拟易乐途门店设备信息上报流程？

>[!info]- 易乐途门店设备信息上报美团的完整流程
>- 易乐途门店设备**开机**、**关机**、**重启**时会上报数据到途邦
>- 途邦收到易乐途上报数据会先根据途邦SCRM管理平台中的**数据清洗规则**过滤数据
>- 途邦再将过滤后的数据上报美团
>>[!tip] 途邦不会主动给美团上报数据，美团调用接口查询门店下的设备信息时，数据才会同步给美团
>- 人工通过**编辑设备信息**修改设备数据后，同步数据给美团时，人工修改数据变为最新的上报数据

---
#### 1. [[易乐途测试环境安装]]
- 登录服务端后，即可调用设备上报接口模拟门店设备数据上报
- 打开客户端可模拟设备启动时上报数据，关闭客户端可模拟设备关闭时上报数据

#### 2. 易乐途门店绑定美团门店
- 在途邦管理平台通过**授权美团门店**绑定
>[!info] 测试环境美团门店账号
>账号：develop_tuangou304
>密码：m2QjWr

- 在tobang数据库middle_office：mt_shop_auths表中快速绑定、解绑门店
>[!info] is_auth=1为绑定，is_auth=0为解绑

#### 3. 调用易乐途设备上报接口

>[!example] 调用示例
>- url：http://192.168.58.149:52745/pms_PostDeviceInfo
>- query参数（shopid）：90007210
>- body参数（application/json）
>>[!example]- 
>>{
    "audio": [
        {
            "default": true,
            "device": "MEDIA",
            "device_id": "1022",
            "enumerator": "HDAUDIO",
            "firm": "NVIDIA",
            "name": "Digipass 905 SmartCard Reader false",
            "sn": "HDAUDIO\\FUNC_01&VEN_10DE&DEV_0093&SUBSYS_73770000&REV_1001",
            "vendor_id": "2c9c"
        },
        {
            "default": false,
            "device": "MEDIA",
            "device_id": "0001",
            "enumerator": "HDAUDIO",
            "firm": "Realtek",
            "name": "Digipass 905 SmartCard Reader true",
            "sn": "HDAUDIO\\FUNC_01&VEN_10EC&DEV_0897&SUBSYS_104387FB&REV_1004",
            "vendor_id": "1a44"
        }
    ],
    "baseboard": {
        "firm": "ASUSTeK COMPUTER INC.",
        "id": "230926617802880",
        "name": "B760M-T D4",
        "version": "Rev 1.xx"
    },
    "cpu": [
        {
            "core_count": 6,
            "family": 205,
            "firm": "Intel(R) Corporation",
            "id": "BFEBFBFF00090675",
            "interface": 0,
            "level2_cache_KB": 7680,
            "level3_cache_KB": 18432,
            "name": "12th Gen Intel(R) Core(TM) i5-12400F",
            "speed_MB": 3960,
            "thread_count": 12
        }
    ],
    "disks": [
        {
            "firm": "WDC",
            "id": "     WD-WXU2D53HDJ55",
            "interface": 0,
            "name": "WDC WD20EARZ-00C5XB0",
            "size": 1863,
            "size_MB": 1907729
        },
        {
            "firm": "WD",
            "id": "E823_8FA6_BF53_0001_001B_444A_48E6_813E.",
            "interface": 0,
            "name": "WD Blue SN570 500GB SSD",
            "size": 465,
            "size_MB": 476940
        }
    ],
    "display_resolution": "width:1920,height:1080",
    "gpu": [
        {
            "firm": "NVIDIA",
            "firmid": 4318,
            "id": "VEN_10DE&DEV_1F0A&REV_A1",
            "interface": 0,
            "name": "NVIDIA GeForce GTX 1650 6",
            "size_MB": 3072
        }
    ],
    "hids": [
        {
            "device_id": "013a",
            "device_type": 1,
            "firm": "(标准键盘)",
            "name": "Barcode Module - Virtual Keyboard111111",
            "sn": "HID\\VID_09DA&PID_2268&REV_0112&MI_00",
            "vendor_id": "0db5"
        },
        {
            "device_id": "024f",
            "device_type": 2,
            "firm": "Microsoft",
            "name": "RF Receiver and G6-20D Wireless Optical Mouse",
            "sn": "HID\\VID_09DA&PID_8736&REV_0101",
            "vendor_id": "09DA"
        }
    ],
    "ip": [
        "192.168.150.100"
    ],
    "mac": "E8-9C-25-37-9E-9A",
    "mac_addresses": [
        "E8-9C-25-37-9E-8A"
    ],
    "main_board": "PRIME B760M-F D4",
    "memories": [
        {
            "id": "BE5B0500",
            "interface": 0,
            "name": "A-DATA Technology-BE5B0500/32GB 101",
            "origin_name": "A-DATA Technology-BE5B0500",
            "size": 32,
            "size_MB": 32768,
            "speed_MHZ": 3200,
            "type": 29
        }
    ],
    "monitor": [
        {
            "diagonal_inches": 23.976991653442383,
            "firm": "DEL1415926",
            "frequency": 994,
            "height": 30,
            "name": "DELL P2422H test",
            "productCode": 41413,
            "resolution_height": 1920,
            "resolution_width": 3072,
            "width": 53
        },
        {
            "diagonal_inches": 23.976991653442383,
            "firm": "DEL",
            "frequency": 0,
            "height": 30,
            "name": "DELL P2422H",
            "productCode": 41412,
            "resolution_height": 1111,
            "resolution_width": 2222,
            "width": 53
        }
    ],
    "name": "机器1",
    "netcard": [
        {
            "firm": "Realtek",
            "name": "Realtek Gaming 2.5GbE Family Controller",
            "speed": 1000
        }
    ],
    "pc_ip": "192.168.150.230",
    "gid": 90007210,
    "shop_id": 90007210,
    "system_name": "Windows 11",
    "system_version": "10.0.19045",
    "uuid": "1df81cf07784fb3352dfe54d25e58f1341",
    "version": 2
}
- 调用该接口可将易乐途门店下设备的全量数据上报给途邦
- 易乐途门店没有绑定美团门店时，数据会展示在未授权列表
- 易乐途门店已绑定美团门店时，数据会展示在已授权列表

#### 4. 调用查询指定门店下全量设备信息接口

>[!example] 调用示例
>- url：https://tb-md-t.stnts.com/api/meituan/v1/callback/callback
>- 请求参数（body参数 x-www-form-urlencoded）：
>	- msgType：5810155
>	- developerid：117090
>	- sign：c339bc79e5cba76d71798b7bbb938edaebd140ee
>	- msgid：7668614585338609882
>	- message：{"opPoiId":"A13HE4SUAO93DVI01RJ1U9O9PKT4MOGM6K4A024BDOVFE4JS21L10","pageSize":50,"pageNo":1}
>	- timestamp：1778861127
>	- businessId：58
- 调用该接口可查询美团门店绑定的易乐途门店下的全量设备信息，易乐途上报给途邦的数据，此时会同步给美团
- 其中message中的opPoild是美团门店id
- 签名sign可找开发索要
---

>[!success] 完成以上步骤即可成功模拟易乐途门店设备数据上报美团