<div align="center">

# Crazy Thursday

_🍗 疯狂星期四 🍗_

</div>

<p align="center">

  <a href="https://github.com/MinatoAquaCrews/nonebot_plugin_crazy_thursday/blob/master/LICENSE">
    <img src="https://img.shields.io/github/license/MinatoAquaCrews/nonebot_plugin_crazy_thursday?color=blue">
  </a>

  <a href="https://github.com/nonebot/nonebot2">
    <img src="https://img.shields.io/badge/nonebot2-2.0.0rc1+-green">
  </a>

  <a href="https://github.com/MinatoAquaCrews/nonebot_plugin_crazy_thursday/releases/tag/v0.2.6.post2">
    <img src="https://img.shields.io/github/v/release/MinatoAquaCrews/nonebot_plugin_crazy_thursday?color=orange">
  </a>

  <a href="https://www.codefactor.io/repository/github/MinatoAquaCrews/nonebot_plugin_crazy_thursday">
    <img src="https://img.shields.io/codefactor/grade/github/MinatoAquaCrews/nonebot_plugin_crazy_thursday/master?color=red">
  </a>

  <a href="https://github.com/MinatoAquaCrews/nonebot_plugin_crazy_thursday">
    <img src="https://img.shields.io/pypi/dm/nonebot_plugin_crazy_thursday">
  </a>

  <a href="https://results.pre-commit.ci/latest/github/MinatoAquaCrews/nonebot_plugin_crazy_thursday/master">
	<img src="https://results.pre-commit.ci/badge/github/MinatoAquaCrews/nonebot_plugin_crazy_thursday/master.svg" alt="pre-commit.ci status">
  </a>

</p>

## 版本

[v0.2.6.post2](https://github.com/MinatoAquaCrews/nonebot_plugin_crazy_thursday/releases/tag/v0.2.6.post2)

⚠ 适配nonebot2-2.0.0rc1+

## 安装

1. 通过 `pip` 或 `nb` 安装；

2. 文案的默认路径位于**插件同级目录**下；也可放置在别处，在 `.env` 下设置即可；`CRAZY_AUTO_UPDATE` 默认关闭，开启则插件将在启动时自动检查资源更新。例如：

```python
CRAZY_PATH="your-path-to-post.json"
CRAZY_AUTO_UPDATE=false
```

## 功能

天天疯狂！随机输出KFC疯狂星期四文案。

⚠ 每次启动插件会自动尝试从repo中下载最新的文案资源！

## 命令

1. 天天疯狂，疯狂星期[一|二|三|四|五|六|日|天]，输入**疯狂星期八**等不合法时间将提示；

2. 支持日文触发：狂乱[月|火|水|木|金|土|日]曜日；

## 本插件改自

[HoshinoBot-fucking_crazy_thursday](https://github.com/Nicr0n/fucking_crazy_thursday)
