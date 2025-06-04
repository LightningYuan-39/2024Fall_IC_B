f=open("D:/File/Code/1.txt","w")
f.writelines(["I love Python!\n","I hate HP!\n"])
f.close()
f=open("1.txt","r+")
print(f.readable())
print(f.writable())
for each in f:
    print(each)
print(f.tell())
f.seek(0)
print(f.tell())
print(f.readline())
print(f.read())
f.write("I love WIFI.\n")
f.flush()
f.seek(0)
f.truncate(26)
f.close()
from pathlib import Path
p=Path.cwd()
print(p)
q=p/"py"
print(q)
r=q/"login.txt"
print(q.is_file(),q.is_dir())
print(r.is_file(),r.is_dir())
print((q/"1.txt").exists())
print(r.name,r.suffix,r.stem)
print(r.parent.parent.parent)
rs=r.parents
for each in rs:
    print(each)
print(rs[3])
print(r.parts)
print(r.stat())
print(r.stat().st_size)
a=Path("./py")
list1=list(each for each in q.iterdir() if each.is_file())
print(list1)
n=q/"untitled1/1/2/3"
m=q/"untitled"
n.mkdir(exist_ok=True,parents=True)
m.mkdir(exist_ok=True)
import shutil
for each in q.iterdir():
    if each.is_dir():shutil.rmtree(each)
del m,n,q,r,a,f
from pathlib import Path
a=Path.cwd()/"py/练习_代码行数统计.py"
a.rename("py/练习_代码行数统计.py")
a=Path("py/计概笔记.py")
a.replace(Path("py/计概笔记.py"))
a=Path.cwd()/"py/untitled/1/2/3"
a.mkdir(exist_ok=True,parents=True)
a=a/"1.txt"
a.open("a")
a.unlink()
a.parent.rmdir()
a.parent.parent.rmdir()
print(list(Path(".").glob("**/*.py")))