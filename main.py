from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
import requests
@register("howToday", "今日热搜", "今日热搜插件", "1.0", "https://github.com/ECR4Z/astrbot_plugin_how_today")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
    
    # 注册指令的装饰器。指令名为 helloworld。注册成功后，发送 `/helloworld` 就会触发这个指令，并回复 `你好, {user_name}!`
    @filter.command("now")
    async def now(self, event: AstrMessageEvent):
        '''返回今日热搜''' # 这是 handler 的描述，将会被解析方便用户了解插件内容。建议填写。
        user_name = event.get_sender_name()
        message_str = event.message_str # 用户发的纯文本消息字符串
        message_chain = event.get_messages() # 用户所发的消息的消息链 # from astrbot.api.message_components import *
        logger.info(message_chain)
        hot = self.get_hot()
        yield event.plain_result(f'今日热搜：\n{self.get_hot()}')
    def get_hot(self):
        url = "https://momoyu.cc/api/hot/list"
        querystring = {"type":"1"}
        payload = ""
        headers = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "cache-control": "no-cache",
            "pragma": "no-cache",
            "priority": "u=1, i",
            "referer": "https://momoyu.cc/",
            "sec-ch-ua-mobile": "?0",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Cookie": "connect.sid=s%3A1COKm5rqaRHZkaqYh4V8m-ikeriO-Zzm.f0ofYW7ZL4E%2BLCoKBVXJAhVVIpA9EQJLFOgUs70gX%2Bw"
        }
        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
        return response.text