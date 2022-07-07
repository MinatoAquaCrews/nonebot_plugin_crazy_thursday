import random
from pathlib import Path
from nonebot import on_regex
from nonebot.typing import T_State
from nonebot.matcher import Matcher
from nonebot.params import Depends, State, RegexMatched
from .config import crazy_config
try:
    import ujson as json
except ModuleNotFoundError:
    import json

__crazy_thursday_version__ = "v0.2.4"
__crazy_thursday_notes__ = f"""
KFC疯狂星期四 {__crazy_thursday_version__}
[疯狂星期X] 随机输出KFC疯狂星期四文案
[狂乱X曜日] 随机输出KFC疯狂星期四文案""".strip()

crazy = on_regex(pattern=r"疯狂星期\S", priority=15)
crazy_jp = on_regex(pattern=r"狂乱\S曜日", priority=15)

def get_weekday_cn(arg: str = RegexMatched(), state: T_State = State()):
    weekday = arg[-1].replace("天", "日")
    return {**state, "weekday": weekday}

def get_weekday_jp(arg: str = RegexMatched(), state: T_State = State()):
    weekday = arg[2]
    return {**state, "weekday": weekday}
        
@crazy.handle()
async def _(matcher: Matcher, state: T_State = Depends(get_weekday_cn)):
    weekday = state["weekday"]
    await matcher.finish(rndKfc(weekday))

@crazy_jp.handle()
async def _(matcher: Matcher, state: T_State = Depends(get_weekday_jp)):
    weekday = state["weekday"]
    await matcher.finish(rndKfc(weekday))

def rndKfc(day: str):
    # jp en cn
    tb = ["月", "Monday", "一", "火", "Tuesday", "二", "水", "Wednesday", "三", "木", "Thursday", "四", "金", "Friday", "五", "土", "Saturday""六", "日", "Sunday", "日"]
    if day not in tb:
        return "给个准确时间，OK?"
    
    # Get the weekday group index
    idx = int(tb.index(day)/3)*3
    
    # json数据存放路径
    path: Path = crazy_config.crazy_path / "post.json"
    
    # 将json对象加载到数组
    with open(path, "r", encoding="utf-8") as f:
        kfc = json.load(f).get("post")
        
    # 随机选取数组中的一个对象，替换关键字
    return random.choice(kfc).replace("木曜日", tb[idx] + "曜日").replace("Thursday", tb[idx+1]).replace("thursday", tb[idx+1]).replace("星期四", "星期" + tb[idx+2]).replace("周四", "周" + tb[idx+2]).replace("礼拜四", "礼拜" + tb[idx+2])