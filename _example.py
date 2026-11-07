"""脚本规则模板（示例，未被任何规则引用，可直接复制改造）。

脚本规则契约：
  1. 文件内必须定义 apply(text, ctx)，同步或 async 均可；
  2. 返回 str  = 处理后的文本（不想处理就返回原 text）；
     返回 None = 拦截这条消息
                 pre 链：不送 AI、不回复（或回复插件配置的提示语）
                 post 链：不发送到群、不存入对话历史；
  3. 抛异常或超时：该条消息按原样透传，异常记入日志；
  4. 修改脚本文件后自动热加载（按修改时间），无需重启。

ctx 字段：
  ctx.chain           当前链 'pre'（群友消息→AI）或 'post'（AI回复→群）
  ctx.rule_name/id    本规则的名称/ID
  ctx.session_id      会话 ID（unified_msg_origin）
  ctx.platform        平台名，如 qq_official / aiocqhttp
  ctx.chat_type       'group' / 'private' / 'other'
  ctx.group_id        群号（私聊为空串）
  ctx.sender_id       发送者 ID；post 链里即触发这轮对话的用户
  ctx.sender_name     发送者昵称
  ctx.is_admin        是否 AstrBot 管理员（admins_id 名单）
  ctx.is_group_chat / ctx.is_private_chat
  ctx.event           AstrMessageEvent 本体（高级用法，字段参考 docs.astrbot.app）
"""


def apply(text, ctx):
    # 示例：去掉结尾的中文句号（未触发则原样返回）
    if ctx.chain == "post" and text.endswith("。"):
        return text[:-1]
    return text

    # 示例：拦截"忘掉人格"类话术（取消注释并把上面 if 块删掉即可启用）
    # if ctx.chain == "pre" and ("忘掉" in text or "忽略之前" in text):
    #     return None
    # return text
