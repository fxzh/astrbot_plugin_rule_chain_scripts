"""结尾不是标点就补个没闭合的左括号："其实我也这么觉得" → "其实我也这么觉得（"。

挂 post 链（后处理）。两个条件同时满足才动：
  1. 结尾（尾部空白/换行不算）不是标点——结尾有标点说明话说完了，不动；
  2. 90% 概率掷中（剩下 10% 原样放过，避免每条都被看出套路）。

追加的是全角左括号"（"，没有右半边，潜台词"话没说完，你自己品"。

标点判定与 leading_question_mark 一致：unicodedata 的 P* 类（中英文
标点全覆盖），另把波浪号 ~／～ 也算标点（语气符号）。含 Markdown
代码块（```）的回复直接跳过——括号落在代码围栏后面会破坏渲染。
"""

import random
import unicodedata

PROBABILITY = 0.9
_EXTRA_PUNCT = {"~", "～"}


def _is_punct(ch):
    return ch in _EXTRA_PUNCT or unicodedata.category(ch).startswith("P")


def apply(text, ctx):
    if ctx.chain != "post":
        return text
    if "```" in text:
        return text  # 代码块结尾，追加会破坏渲染
    core = text.rstrip()  # 尾部空白/换行不参与判断
    if not core or _is_punct(core[-1]):
        return text
    if random.random() >= PROBABILITY:
        return text
    return core + "（"
