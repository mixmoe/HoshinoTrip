import nonebot
from nonebot.adapters.cqhttp import Bot

nonebot.init(debug=True)

nonebot.get_driver().register_adapter('cqhttp',Bot)

nonebot.load_plugin('nonetrip')

import hoshino

hoshino.init()
nonebot.run(port=2333)

