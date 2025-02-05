from astrbot.api.all import *

@register("astrbot_plugin_myapp", "Your Name", "一个简单的消息回复插件", "1.0.0")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
    
    # 注册指令的装饰器。指令名为 hello。注册成功后，发送 `/hello` 就会触发这个指令
    @filter.command("hello")
    async def hello(self, event: AstrMessageEvent):
        yield event.plain_result("你好，收到消息") # 发送一条纯文本消息
