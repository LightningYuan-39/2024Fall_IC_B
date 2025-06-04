import socket,asyncio,threading,time,simplified
server_sockets=[]
client_sockets=[]
for i in range(4):
    server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.bind(("10.7.188.55",8888+i))
    server_socket.listen(4)
    print(f"server started,port={8888+i}")
    server_sockets.append(server_socket)
async def start_server():
    loop=asyncio.get_event_loop()
    #引导终端进入对应的端口
    server_presocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_presocket.bind(("10.7.188.55",7837))
    server_presocket.listen(4)
    presocket,preaddress=await loop.sock_accept(server_presocket)
    presocket.sendall("8888".encode())
    presocket.close()
    #接收终端进入端口
    client_socket,client_address=await loop.sock_accept(server_sockets[0])
    client_socket.sendall("您已进入游戏，正在为您匹配玩家".encode())
    client_sockets.append(client_socket)
async def wait_for_players():
    for i in range(3):
        loop=asyncio.get_event_loop()
        #引导终端进入端口
        server_presocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server_presocket.bind(("10.7.188.55",7837))
        server_presocket.listen(4)
        presocket,preaddress=await loop.sock_accept(server_presocket)
        presocket.send(f"{8888+i+1}".encode())
        presocket.close()
        #接收终端进入端口
        client_socket,client_address=await loop.sock_accept(server_sockets[i+1])
        client_socket.sendall("您已进入游戏，正在为您匹配玩家".encode())
        client_sockets.append(client_socket)
async def timelimit(func,t):
    try:
        await asyncio.wait_for(func(),timeout=t)
        return "program executed"
    except asyncio.TimeoutError:return "time limit exceeded"
def start():
    a=asyncio.run(timelimit(start_server,60))
    if a=="program executed":
        a=asyncio.run(timelimit(wait_for_players,30))#改回30
    else:return
    for i in range(3,len(client_sockets)-1,-1):
        server_sockets[i].close()
    simplified.main(client_sockets)
    time.sleep(10)
    for i in client_sockets:i.close()
    for i in server_sockets:i.close()
#在async的使用上面借助了ask.pku.edu.cn的ai
#开始的时候创建4个socket
start()
