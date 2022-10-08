<div align="center">

# Crazy Thursday

<!-- prettier-ignore-start -->
<!-- markdownlint-disable-next-line MD036 -->
_🍗 疯狂星期四 🍗_
<!-- prettier-ignore-end -->

</div>

<p align="center">
  
  <a href="https://github.com/MinatoAquaCrews/nonebot_plugin_crazy_thursday/blob/beta/LICENSE">
    <img src="https://img.shields.io/github/license/MinatoAquaCrews/nonebot_plugin_crazy_thursday?color=blue">
  </a>
  
  <a href="https://github.com/nonebot/nonebot2">
    <img src="https://img.shields.io/badge/nonebot2-2.0.0rc1+-green">
  </a>
  
  <a href="https://github.com/MinatoAquaCrews/nonebot_plugin_crazy_thursday/releases/tag/v0.2.6rc1">
    <img src="https://img.shields.io/github/v/release/MinatoAquaCrews/nonebot_plugin_crazy_thursday?color=orange">
  </a>

  <a href="https://www.codefactor.io/repository/github/MinatoAquaCrews/nonebot_plugin_crazy_thursday">
    <img src="https://img.shields.io/codefactor/grade/github/MinatoAquaCrews/nonebot_plugin_crazy_thursday/beta?color=red">
  </a>
  
</p>

## 版本

v0.2.6rc1

⚠ 适配nonebot2-2.0.0rc1+

[更新日志](https://github.com/MinatoAquaCrews/nonebot_plugin_crazy_thursday/releases/tag/v0.2.6rc1)

## 安装

1. 通过`pip`或`nb`安装；

2. 读取文案的默认路径位于**插件同级目录**下；可在`.env`下设置：

    ```python
    CRAZY_PATH="your-path-to-post.json"   # For example: "./my_data/crazy_thursday"，在此文件夹下放置"post.json"
    ```

## 功能

天天疯狂！随机输出KFC疯狂星期四文案。

⚠ 每次启动插件会自动尝试从repo中下载最新的文案资源！

## 命令

1. 天天疯狂，疯狂星期[一|二|三|四|五|六|日|天]，输入**疯狂星期八**等不合法时间将提示；

2. 支持日文触发：狂乱[月|火|水|木|金|土|日]曜日；

## 本插件改自

[HoshinoBot-fucking_crazy_thursday](https://github.com/Nicr0n/fucking_crazy_thursday)