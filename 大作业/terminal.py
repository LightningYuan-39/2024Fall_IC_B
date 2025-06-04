import socket,time,os
#接受服务器的引导
client_socket=socket.socket()
client_socket.connect(("10.7.188.55",7837))
port=int(client_socket.recv(1024).decode())
client_socket.close()
#主程序
client_socket=socket.socket()
client_socket.connect(("10.7.188.55",port))
client_socket.setblocking(False)
while True:
    try:
        msg=client_socket.recv(1024).decode()
        if "timeout" in msg:
            l=msg.split("timeout")
            print(l[0])
            os.system("timeout 10")
            msg=l[1]
        if "cls" in msg:
            os.system("cls")
            msg=msg.replace("cls","")
        print(msg)
        if "Choose action" in msg or "Press any key to continue..." in msg or "Query mode" in msg:
            client_socket.sendall((input()+"0").encode()) 
        if "Hu" in msg and "Choose action" not in msg or "No winner" in msg:
            time.sleep(10)
            client_socket.close()
            break
    except BlockingIOError:pass