import random,os,copy,algorithm,socket
#发送给所有玩家
def remote_cls(sock:socket.socket):
    sock.sendall("cls".encode())
def remote_print(sock:socket.socket,msg):
    sock.sendall(msg.encode())
def remote_input(sock:socket.socket,hint):
    sock.sendall(hint.encode())
    return sock.recv(1024).decode()
def start_game(sock:socket.socket):
    remote_print(sock,"""欢迎来到简化版麻将。
      关于游戏规则的特别说明：
      1.如果有不少于2个人在结束阶段选择和牌，则让本结束阶段对应的回合阶段对应的id逆时针方向第一个选择和牌的人和牌
      2.请根据游戏提示，输入动作对应的编号，后面如果要接上需要操作的牌，请在动作编号之后加空格，并接上需要操作的牌
      3.本游戏配有查询其余玩家牌河和副露的功能，在游戏的任何暂停阶段，您可以输入Query可进入查询模式""")
    remote_print(sock,"timeout")
#服务器端
def cards_init():
    global cardlst
    cardlst=[]
    for k in ["S","M","P"]:
        for i in range(1,10):
            for j in range(4):
                cardlst.append(k+str(i))
class Player():
    def __init__(self,identity,conn="localhost") -> None:
        self.identity=identity
        self.conn=conn
        self.hand=[]
        self.subhand=[]#玩家的副露可作为二维列表方便查询
        self.discards=[]#一样是二维列表
    def get_cards(self):
        global cardlst
        ind=random.randint(0,len(cardlst)-1)
        a=cardlst.pop(ind)
        self.hand.append(a)
        return a
def createrole(lst:list[socket.socket]):
    global playerlst
    playerlst=[]
    while lst:
        playerlst.append(Player(identity="human",conn=lst.pop()))
    a=len(playerlst)
    for i in range(4-a):
        playerlst.insert(random.randint(0,len(playerlst)),Player(identity="ai"))
sort_parameter=lambda x:((0 if x[0]=="S" else( 9 if x[0]=="M" else 18))+int(x[1]))
def fenpai():
    global cardlst,playerlst
    for i in range(52):
        playerlst[i%4].get_cards()
    for i in range(4):
        playerlst[i%4].hand=sorted(playerlst[i%4].hand,key=sort_parameter)
#开始回合
def prtinfo(turnnum,sockseq:int,sock:socket.socket):
    global cardlst
    remote_print(sock,f"Your ID: {sockseq}\nCurrent ID: {turnnum}\nHand: {" ".join(playerlst[sockseq].hand)}\n")
    subout="".join(f"({" ".join(i)})"for i in playerlst[sockseq].subhand)
    remote_print(sock,f"Sub Hand: {subout}\nRemain card number:{len(cardlst)}")
def hu(msg):
    winnerid=int(msg[6])
    subout=""
    for i in playerlst[winnerid].subhand:
        subout+=("("+" ".join(i)+")")
    for i in playerlst:
        if i.identity=="human":
            remote_print(i.conn,msg+"\n"+" ".join(playerlst[winnerid].hand)+" + "+subout+" + "+msg[11:])
def player_turn(id,round_draw,round_hu):
    #回合阶段
    global cardlst,playerlst
    #turnnum是全局的,id是本局回合阶段属于谁的变量
    for sockseq in range(4):
        if playerlst[sockseq].identity=="human":remote_cls(playerlst[sockseq].conn)
    if round_draw:
        d=playerlst[id].get_cards()
        if playerlst[id].identity=="human":remote_print(playerlst[id].conn,f"Draw: {d}")
        playerlst[id].hand=sorted(playerlst[id].hand,key=sort_parameter)
    for sockseq in range(4):
        if playerlst[sockseq].identity=="human":
            prtinfo(id,sockseq,playerlst[sockseq].conn)
    action_lst=["Cut"]
    if algorithm.card_hu(copy.deepcopy(playerlst[id].hand)) and round_hu:action_lst.insert(0,"Hu")
    gang0lst=algorithm.can_gang0(copy.deepcopy(playerlst[id].hand))
    if gang0lst:action_lst.append("Gang0")
    gang2lst=algorithm.can_gang2(copy.deepcopy(playerlst[id].hand),copy.deepcopy(playerlst[id].subhand))
    if gang2lst:action_lst.append("Gang2")
    while True:
        action=remote_input(playerlst[id].conn,f"\nChoose action: "+\
        ", ".join(f"{i}: {action_lst[i]}" for i in range(len(action_lst))))[:-1]\
             if playerlst[id].identity=="human" else random.randint(0,len(action_lst)-1)
        try:
            if playerlst[id].identity=="human" and action_lst[int(action[0])]=="Hu" or playerlst[id].identity=="ai" and action_lst[action]=="Hu":
                return f"Player{id} Hu {d}"
            elif (playerlst[id].identity=="human" and action_lst[int(action[0])]=="Cut" and action[2:] in playerlst[id].hand) or\
                 (playerlst[id].identity=="ai" and action_lst[action]=="Cut"):
                dis=action[2:] if playerlst[id].identity=="human" else random.choice(playerlst[id].hand)
                playerlst[id].discards.append(dis)
                playerlst[id].hand.remove(dis)
                bw=f"Player{id} Cut {dis}"
                return bw
            elif (playerlst[id].identity=="human" and action_lst[int(action[0])]=="Gang0" and action[2:] in gang0lst) or \
                (playerlst[id].identity=="ai" and action_lst[action]=="Gang0"):
                crd=action[2:] if playerlst[id].identity=="human" else random.choice(gang0lst)
                playerlst[id].hand=algorithm.multi_remove(playerlst[id].hand,crd,4)
                playerlst[id].subhand.append([crd for i in range(4)])
                bw=f"Player{id} Gang0 {crd}"
                return bw
            elif (playerlst[id].identity=="human" and action_lst[int(action[0])]=="Gang2" and action[2:] in gang2lst) or \
                (playerlst[id].identity=="ai" and action_lst[action]=="Gang2"):
                crd=random.choice(gang2lst) if playerlst[id].identity=="ai" else action[2:]
                for i in playerlst[id].subhand:
                    if i==3*[crd]:i.append(i[0])
                playerlst[id].hand.remove(crd)
                playerlst[id].discards.append(f"Gang2:{crd}")
                bw=f"Player{id} Gang2 {crd}"
                return bw
            else:remote_print(playerlst[id].conn,"请检查并重新输入指令")
        except Exception:remote_print(playerlst[id].conn,"请检查并重新输入指令")#目前只完成该地方的debug
def player_end(id,tagid,tagcard,is_gang2):
    #每一次切牌的结束动作
    global playerlst
    action_lst=["Ignore"]
    chilst=algorithm.can_chi(copy.deepcopy(playerlst[id].hand),tagcard) if (id-tagid)%4==1 else []
    if is_gang2==False:
        if chilst:action_lst.insert(0,"Chi")
        crdnum=copy.deepcopy(playerlst[id].hand).count(tagcard)
        if crdnum>=2:
            action_lst.insert(0,"Peng")
            if crdnum>=3:action_lst.insert(0,"Gang1")
    extended_list=copy.deepcopy(playerlst[id].hand)
    extended_list.append(tagcard)
    if algorithm.card_hu(extended_list):
        action_lst.insert(0,"Hu")
    #prtinfo(tagid)
    while True:
        if playerlst[id].identity=="human":action=remote_input(playerlst[id].conn,"\nChoose action: "+\
        ", ".join(f"{i}: {action_lst[i]}" for i in range(len(action_lst))))[:-1]
        try:
            actionnum=int(action[0])if playerlst[id].identity=="human" else random.randint(0,len(action_lst)-1)
            if action_lst[actionnum]=="Ignore":
                return f"Player{id} Ignore"
            if action_lst[actionnum]=="Hu":return f"Player{id} Hu {tagcard}"
            if (playerlst[id].identity=="human" and action_lst[actionnum]=="Chi" and action[2:].split() in chilst) or\
                playerlst[id].identity=="ai" and action_lst[actionnum]=="Chi":
                shunzi=action[2:].split() if playerlst[id].identity=="human" else random.choice(chilst)
                return f"Player{id} Chi Player{tagid} {tagcard}:{" ".join(shunzi)}"
            if action_lst[actionnum]=='Peng':
                return f"Player{id} Peng Player{tagid} {tagcard}"
            if action_lst[actionnum]=="Gang1":
                return f"Player{id} Gang1 Player{tagid} {tagcard}"
            remote_print(playerlst[id].conn,"请检查并重新输入指令")
        except Exception:remote_print(playerlst[id].conn,"请检查并重新输入指令")
#发送给客户端
def query(sock:socket.socket):
    global playerlst
    while True:
        x=remote_input(sock,f"""Query mode:
          1: Discards 2: Subhand
          """)[:-1]
        if x=="Exit":return
        elif len(x)==3 and x[0] in "12" and x[2] in "0123" and x[1]==":":
            if x[0]=="1":
                disout=" ".join(i[len(i)-2:len(i):1] for i in playerlst[int(x[2])].discards)
                remote_print(sock,f"\nPlayer{int(x[2])}\'s discards: {disout}")
            elif x[0]=="2":
                subout="".join(f"({" ".join(i)})" for i in playerlst[int(x[2])].subhand)
                remote_print(sock,f"\nPlayer{int(x[2])}\'s subhand: {subout}")
        else:remote_print(sock,"输入格式不对，请重新输入，例如查询4号玩家的副露可以输入4:2")
#服务器端
def main(lst:list[socket.socket]):
    cards_init()
    createrole(lst)
    fenpai()
    for i in playerlst:
        if i.identity=="human":start_game(i.conn)
    state="turn"
    global cardlst,turnnum
    turnnum,round_draw,round_hu=0,True,True
    while cardlst:
        if state=="turn":
            msg=player_turn(turnnum,round_draw,round_hu)
            if "Hu" in msg:
                hu(msg)
                return
            else:
                for i in playerlst:
                    if i.identity=="human":
                        a=remote_input(i.conn,f"\n{msg}\nPress any key to continue...")[:-1]
                        if a=="Query":query(i.conn)
                if "Cut" in msg or "Gang2" in msg:state="end"
                elif "Gang0" in msg:pass
        elif state=="end":
            tagid,tagcard,is_gang2=int(msg[6]),msg.split()[2],"Gang2" in msg#这里msg是回合阶段传过来的报文
            msglst=[]
            for i in range(4):
                if i!=tagid:
                    msglst.append((i,player_end(i,tagid,tagcard,is_gang2)))
            priorlst=["Hu","Gang1","Peng","Chi","Ignore"]
            def msg_sort_param(x,y,cur):
                if priorlst.index(x[1].split()[1])<priorlst.index(y[1].split()[1]):return 0
                if priorlst.index(x[1].split()[1])>priorlst.index(y[1].split()[1]):return 1
                if (x[0]-cur)%4<(y[0]-cur)%4:return 0
                return 1
            #prtinfo(tagid)
            msg=sorted(msglst,key=lambda i:sum(msg_sort_param(i,j,tagid) for j in msglst if j!=i))[0][1]#非法的吃操作已经被输入端过滤,此时msg定义改变
            if "Hu" in msg:
                hu(msg)
                return
            elif "Gang1" in msg:#msg指示的玩家在操作
                turnnum=int(msg[6])
                playerlst[turnnum].hand=algorithm.multi_remove(playerlst[turnnum].hand,tagcard,3)
                playerlst[turnnum].subhand.append(4*[tagcard])
                round_draw,round_hu,playerlst[tagid].discards=True,True,algorithm.multi_remove(playerlst[tagid].discards,tagcard,1)
            elif "Peng" in msg:
                turnnum=int(msg[6])
                playerlst[turnnum].hand=algorithm.multi_remove(playerlst[turnnum].hand,tagcard,2)
                playerlst[turnnum].subhand.append(3*[tagcard])
                round_draw,round_hu,playerlst[tagid].discards=False,False,algorithm.multi_remove(playerlst[tagid].discards,tagcard,1)
            elif "Chi" in msg:
                turnnum=int(msg[6])
                for i in msg[23:].split():
                    if i!=tagcard:playerlst[turnnum].hand.remove(i)
                playerlst[turnnum].subhand.append(msg[23:].split())
                round_draw,round_hu,playerlst[tagid].discards=False,False,algorithm.multi_remove(playerlst[tagid].discards,tagcard,1)
            else:
                round_draw,round_hu=True,True
                turnnum=(turnnum+1)%4
            for i in playerlst:
                if i.identity=="human":
                    a=remote_input(i.conn,f"\n{msg}\nPress any key to continue...")[:-1]
                    if a=="Query":query(i.conn)
            state="turn"

    s0=''
    for i in range(4):
        s=""
        for j in playerlst[i].subhand:
            s+=("("+" ".join(j)+")")
        if s!="":s=" + "+s
        s=f"Player{i}: "+" ".join(playerlst[i].hand)+s+"\n"
        s0+=s
    for i in range(4):
        if playerlst[i].identity=="human":remote_print(playerlst[i].conn,f"No winner\n{s0}")
    return