# -*- coding=utf-8 -*-
try:
	import json
except ImportError:
#利用import ... as ...，可以动态导入不同名称的模块
	import simplejson as jason