from xmlrpc.server import SimpleXMLRPCServer


def is_alive() -> bool:
    return True


server = SimpleXMLRPCServer(("localhost", 8000))

# 注册rpc服务状态检测函数
server.register_function(is_alive, 'is_alive')

# TODO 注册MediaCrawler函数



server.serve_forever()
