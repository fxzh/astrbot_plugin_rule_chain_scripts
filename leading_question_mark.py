"""结尾问号搬到开头：把"真的吗？"整成"？真的吗"。

挂 post 链（后处理）。三个条件同时满足才动：
  1. 开头不是问号（"？就这"本来就前置，不动）；
  2. 除结尾问号外全文没有任何标点（"你好，在吗？"是正常疑问句，不动——
     只处理"内容光秃秃、偏偏结尾挂个问号"的回复，那种才有疑惑语气）；
  3. 结尾恰好一个问号（"？?"“？?”连续问号、"??"“?!”结尾不是问号，都不动）。

满足则把结尾那个问号原样搬到开头，全半角保留：
  "真的吗？" → "？真的吗"      "就这?" → "?就这"

标点判定用 unicodedata 的 P* 类（中英文标点全覆盖），另把波浪号 ~／～
也算标点（语气符号）。换行不算标点，但带换行的多行回复不是一句话，
搬了会变成"？第一行\\n第二行"这种残废格式，直接跳过。结尾空白/换行
不参与判断。
"""

import unicodedata

QM = ("?", "？")
_EXTRA_PUNCT = {"~", "～"}


def _is_punct(ch):
    return ch in _EXTRA_PUNCT or unicodedata.category(ch).startswith("P")


def apply(text, ctx):
    if ctx.chain != "post":
        return text
    core = text.rstrip()  # 结尾空白/换行不参与判断
    if not core.endswith(QM):
        return text
    if len(core) >= 2 and core[-2] in QM:
        return text  # 结尾连续问号，不止一个
    if core[0] in QM:
        return text  # 开头已是问号
    body = core[:-1]
    if not body.strip():
        return text  # 整条回复就是一个问号，没内容可搬
    if "\n" in body or "\r" in body:
        return text  # 多行回复不是一句话
    if any(_is_punct(ch) for ch in body):
        return text  # 中间有其他标点，是正常句子
    return core[-1] + body.strip()
