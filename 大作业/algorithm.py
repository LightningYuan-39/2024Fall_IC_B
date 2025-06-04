import copy
def multi_remove(lst,i,n):
    tmp=lst
    for j in range(n):tmp.remove(i)
    return tmp
def tri_hu(lst):
    if lst==[]:return True
    lst=sorted(lst,key=lambda x:int(x[1]))
    if lst.count(lst[0])>=3:return tri_hu(multi_remove(lst,lst[0],3))
    else:
        sz1=lst[0][0]+str(int(lst[0][1])+1)
        sz2=lst[0][0]+str(int(lst[0][1])+2)
        if sz1 in lst and sz2 in lst:
            a=multi_remove(lst,lst[0],1)
            a=multi_remove(a,sz1,1)
            a=multi_remove(a,sz2,1)
            return tri_hu(a)
        else:return False
def card_hu(lst):
    '''
    判断玩家的牌型能否和牌
    '''
    slst,mlst,plst=[],[],[]
    while lst:
        c=lst.pop()
        if c[0]=="S":slst.append(c)
        elif c[0]=="M":mlst.append(c)
        elif c[0]=="P":plst.append(c)
    cnt=[]
    for i in [slst,mlst,plst]:
        if len(i)%3==1:return False
        elif len(i)%3==2:cnt.append(i)
    if len(cnt)!=1:return False
    cnt=cnt[0]
    oncelst=[]
    st=set()
    for i in cnt:
        if i not in oncelst:oncelst.append(i)
        else:st.add(i)
    return any(tri_hu(multi_remove(copy.deepcopy(cnt),i,2)) for i in st) and \
        all(tri_hu(copy.deepcopy(i)) for i in [slst,mlst,plst] if i!=cnt)
def can_gang0(lst):
    '''
    输入为玩家手牌,
    判断玩家是否可以暗杠，如果可以，则输出玩家所有可以暗杠的牌
    '''
    dic=dict()
    for i in lst:
        if i not in dic.keys():dic[i]=1
        else:dic[i]+=1
    for i in dic.keys():
        lst=[]
        if dic[i]==4:lst.append(i)
    return lst if lst else False
def can_gang2(hnd,sub):
    '''
    输入的hnd表示玩家的手牌，sub表示玩家的副露
    判断玩家能否补杠，若能，输出玩家所有可以补杠的牌
    '''
    lst=[]
    for i in sub:
        if len(i)==3 and i[0]==i[1]==i[2] and i[0] in hnd:
            lst.append(i[0])
    return lst if lst else False
def can_chi(hnd,crd):
    lst=[]
    a=crd[0]+str(int(crd[1])-2)
    b=crd[0]+str(int(crd[1])-1)
    if a in hnd and b in hnd:lst.append([a,b,crd])
    a=crd[0]+str(int(crd[1])+1)
    if a in hnd and b in hnd:lst.append([b,crd,a])
    b=crd[0]+str(int(crd[1])+2)
    if a in hnd and b in hnd:lst.append([crd,a,b])
    return lst if lst else False
