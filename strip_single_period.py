"""去掉结尾唯一的句号：单个删，连续保留。

挂 post 链（后处理）。只看结尾连续句号的数量：
  结尾恰好 1 个 "。" → 删掉（"好的。" → "好的"）
  结尾 ≥ 2 个 "。"   → 原样返回（"无语了。。" 是语气，不动）
  删完只剩空白（整条回复就是一个"。"）→ 返回 None 拦截，不发空消息

半角句点/省略号（如 "..."）不在处理范围，结尾的空白/换行不参与判断。

为什么不用正则：`。$` 会把"。。"削成"。"，`。+$` 会连语气省略号一起全删，
"数量恰好为 1 才删"用数尾巴最直白。
"""


def apply(text, ctx):
    if ctx.chain != "post":
        return text
    core = text.rstrip()  # 结尾空白/换行不参与判断
    i = len(core)
    while i > 0 and core[i - 1] == "。":
        i -= 1
    n = len(core) - i  # 结尾连续句号个数
    if n == 0 or n >= 2:
        return text
    result = core[:i]
    return result if result.strip() else None
