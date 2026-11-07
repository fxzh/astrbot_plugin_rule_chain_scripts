# astrbot_plugin_rule_chain_scripts

[astrbot_plugin_rule_chain](https://github.com/fxzh/astrbot_plugin_rule_chain)（AstrBot 消息规则链插件）的**脚本规则集合**。插件本体的介绍、安装与配置请移步[主仓库](https://github.com/fxzh/astrbot_plugin_rule_chain)。

插件出于安全考虑默认不附带任何可直接运行的脚本，需要什么自己挑着装——本仓库就是我自用的脚本集。

## 脚本列表

| 脚本 | 挂链 | 效果 |
| --- | --- | --- |
| [`_example.py`](_example.py) | 任意 | 模板与契约说明（含全部 `ctx` 字段表），改造它写自己的脚本 |
| [`fermat_too_long.py`](fermat_too_long.py) | post | 费马式"写不下"：AI 回复越长，越可能被替换成"我确信已经发现了一种美妙的回答，但是对话框太小写不下（"；≤100 字原样、>190 字固定 90%、中间按长度线性概率 |
| [`leading_question_mark.py`](leading_question_mark.py) | post | 结尾问号搬到开头（"真的吗？"→"？真的吗"）：开头无问号、结尾恰好一个问号、其余全文无任何标点才触发，全半角（？/?）都认；连续问号（"??"）、带标点的正常疑问句不动 |
| [`strip_single_period.py`](strip_single_period.py) | post | 删掉结尾唯一的"。"（"好的。"→"好的"）；结尾 ≥2 个连续句号（"无语了。。"）视为语气保留不动 |

## 使用方法

1. 把想要的 `.py` 放进插件目录下的 `scripts/`（目录不存在时新建即可）：

   ```
   ~/.astrbot/data/plugins/astrbot_plugin_rule_chain/scripts/
   ```

2. 挂到规则链（也可在 WebUI 插件配置页添加）：

   ```
   /rule add <pre|post> script <规则名> <脚本.py>
   ```

3. 脚本契约（`apply(text, ctx)` 返回值语义、超时透传、mtime 热加载、`ctx` 字段表等）详见主仓库 README 的[「脚本规则」一节](https://github.com/fxzh/astrbot_plugin_rule_chain#脚本规则)。

## 安全提示

脚本以 AstrBot 同等权限执行。请只安装自己写的或审阅过的脚本。
