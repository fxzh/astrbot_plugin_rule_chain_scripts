"""费马式"写不下"：AI 回复越长，越可能被判定为"对话框太小写不下"。

挂 post 链（后处理）。按原文字符长度决定是否替换：
  len ≤ 100        原样输出（不处理）
  100 < len < 200  概率替换，p = (len - 100) / 100，随长度线性增加
  len ≥ 200        必定替换

例：len=149 → 49%；len=150 → 50%；len=199 → 99%。
"""

import random

REPLACEMENT = "我确信已经发现了一种美妙的回答，但是对话框太小写不下（"
MIN_LEN = 100  # ≤ 此长度不处理
MAX_LEN = 200  # ≥ 此长度必替换，(MIN_LEN, MAX_LEN) 内线性过渡


def apply(text, ctx):
    if ctx.chain != "post":
        return text
    n = len(text)
    if n <= MIN_LEN:
        return text
    if n >= MAX_LEN or random.random() < (n - MIN_LEN) / (MAX_LEN - MIN_LEN):
        return REPLACEMENT
    return text
