import random
import os
from pathlib import Path
import re
import nonebot
from nonebot import on_command, on_regex
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent, GROUP
try:
    import ujson as json
except ModuleNotFoundError:
    import json

global_config = nonebot.get_driver().config
if not hasattr(global_config, "crazy_path"):
    CRAZY_PATH = os.path.join(os.path.dirname(__file__), "resource")
else:
    CRAZY_PATH = global_config.crazy_path

__crazy_vsrsion__ = "v0.2.1"
plugin_notes = f'''
KFC疯狂星期四 {__crazy_vsrsion__}
[疯狂星期X] 随机输出KFC疯狂星期四文案
[狂乱X曜日] 随机输出KFC疯狂星期四文案'''.strip()

plugin_help = on_command("疯狂星期四帮助", permission=GROUP, priority=15, block=True)
crazy = on_regex(r'疯狂星期.', permission=GROUP, priority=15, block=True)
crazy_jp = on_regex(r'狂乱.曜日', permission=GROUP, priority=15, block=True)

@plugin_help.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    await plugin_help.finish(plugin_notes)

@crazy.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    iscrazy = re.search(r'疯狂星期[一|二|三|四|五|六|日]', event.get_plaintext())
    crazy_day = iscrazy.group(0)[-1] if iscrazy is not None else None
    if crazy_day is None:
        await crazy.finish("给个准确时间，OK?")
        
    # json数据存放路径
    filePath = Path(CRAZY_PATH) / "post.json"
    # 将json对象加载到数组
    with open(filePath, "r", encoding="utf-8") as f:
        kfc = json.load(f).get("post")
    # 随机选取数组中的一个对象
    randomPost = random.choice(kfc).replace("星期四", "星期" + crazy_day).replace("周四", "周" + crazy_day)
    await crazy.finish(randomPost)

@crazy_jp.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    iscrazy = re.search(r'狂乱[月|火|水|木|金|土|日]曜日', event.get_plaintext())
    crazy_day = iscrazy.group(0)[-3] if iscrazy is not None else None
    
    if crazy_day is None:
        await crazy_jp.finish("给个准确时间，OK?")

    filePath = Path(CRAZY_PATH) / "post.json"
    with open(filePath, "r", encoding="utf-8") as f:
        kfc = json.load(f).get("post")
    
    randomPost = random.choice(kfc).replace("星期四", "星期" + weekday_table[crazy_day]).replace("周四", "周" + weekday_table[crazy_day])
    await crazy_jp.finish(randomPost)

weekday_table = {
    "月": "一",
    "火": "二",
    "水": "三",
    "木": "四",
    "金": "五",
    "土": "六",
    "日": "日"
}
