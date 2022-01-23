from nonebot.typing import T_State
import random
import json
import os
import re
import nonebot
from nonebot import on_regex
from nonebot.adapters.cqhttp import Bot, GroupMessageEvent, GROUP

_CRAZY_PATH = nonebot.get_driver().config.crazy_path
CRAZY_PATH = os.path.join(os.path.dirname(__file__), "resource") if not _CRAZY_PATH else _CRAZY_PATH
# crazy = on_command('疯狂星期四', aliases={"星期四", "KFC", "V我50"}, permission=GROUP, priority=15, block=True)
crazy = on_regex(r'疯狂星期.', permission=GROUP, priority=15, block=True)

@crazy.handle()
async def random_post(bot: Bot, event: GroupMessageEvent, state: T_State):
    iscrazy = re.search(r'(.*?)星期[一|二|三|四|五|六|日]', event.get_plaintext())
    crazy_day = iscrazy.group(0)[-3:] if iscrazy is not None else None
    if crazy_day is None:
        await crazy.finish("给个准确时间，OK?")
        
    # json数据存放路径
    filePath = os.path.join(CRAZY_PATH, "post.json")
    # 将json对象加载到数组
    kfc = json.load(open(filePath, 'r', encoding="UTF-8")).get('post')
    # 随机选取数组中的一个对象
    randomPost = random.choice(kfc)
    randomPost = randomPost.replace("星期四", crazy_day)
    await bot.send(event=event, message=randomPost)
