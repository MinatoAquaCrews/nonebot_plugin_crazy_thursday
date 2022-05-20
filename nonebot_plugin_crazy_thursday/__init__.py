from random import choice
from pathlib import Path
from re import match
from typing import Optional
from nonebot.matcher import Matcher
from nonebot import get_driver, on_regex
from nonebot.adapters.onebot.v11 import MessageEvent
try:
    import ujson as json
except ModuleNotFoundError:
    import json

global_config = get_driver().config
if not hasattr(global_config, 'crazy_path'):
    CRAZY_PATH = Path(__file__).parent / "resource"
else:
    CRAZY_PATH = global_config.crazy_path

# 插件用法简单，无需帮助
__crazy_thursday_vsrsion__ = 'v0.2.3'
__crazy_thursday_notes__ = f'''
KFC疯狂星期四 {__crazy_thursday_vsrsion__}
[疯狂星期X] 随机输出KFC疯狂星期四文案
[狂乱X曜日] 随机输出KFC疯狂星期四文案'''.strip()

crazy = on_regex(r'疯狂星期\S', priority=15)
crazy_jp = on_regex(r'狂乱\S曜日', priority=15)

@crazy.handle()
async def _(matcher: Matcher, event: MessageEvent):
    await matcher.finish(rndKfc(event.get_plaintext()))

@crazy_jp.handle()
async def _(matcher: Matcher, event: MessageEvent):
    await matcher.finish(rndKfc(event.get_plaintext(), True))

def rndKfc(msg: str, jp: Optional[bool] = False):
    day = (match(r'狂乱(\S)曜日', msg) if jp else match(r'疯狂星期(\S)', msg.replace('天', '日'))).group(1)
    tb = ['月', '一', '火', '二', '水', '三', '木', '四', '金', '五', '土', '六', '日', '日']
    if day not in tb:
        return '给个准确时间，OK?'
    idx = int(tb.index(day)/2)*2
    # json数据存放路径
    path = Path(CRAZY_PATH) / 'post.json'
    # 将json对象加载到数组
    with open(path, 'r', encoding='utf-8') as f:
        kfc = json.load(f).get('post')
    # 随机选取数组中的一个对象
    return choice(kfc).replace('星期四', '星期' + tb[idx+1]).replace('周四', '周' + tb[idx+1]).replace('木曜日', tb[idx] + '曜日')