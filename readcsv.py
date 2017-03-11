import csv
import re

def read_csv(csv_path, d):
    with open(csv_path, newline='', encoding='utf-8') as f:
        txt=f.read()[0:]
    lines=txt.splitlines()[1:]
    csv_rows=list(csv.reader(lines, delimiter=d))
    return csv_rows

def gethead_csv(csv_path,d):
    with open(csv_path, newline='', encoding='utf-8') as f:
        txt=f.read()[0:]
    header=txt.splitlines()[0]
    re=header.split(d)
    return re

def filter(ad, f):
    w=[]
    for i in ad:
        if f(i):
            w.append(i)
    return w

def getbypostnumber(n):
    d=int(n[0])
    if d<2000:
        return False
    elif d>=2600 and d<2620:
        return False
    elif d>2900 and d<2920:
        return False
    elif d>=3000:
        return False
    else:
        return True

def provicefilter(p):
    if p[2]=='NSW':
        return True
    else:
        return False

def typefilter(p):
    if p[4].strip()=='Delivery Area':
        return True
    else:
        return False

if __name__=="__main__":
    data=read_csv('data.csv',',')
    header=gethead_csv('data.csv',',')
    sheader=[]
    for i in header:
        sheader.append(re.sub(r'^"|"$', '', i))
    print(sheader)
    w=filter(filter(data, provicefilter), typefilter)
    print(filter(data, provicefilter)[0])
    print("-----")
    with open('output.csv', 'w') as csvfile:
         writer = csv.DictWriter(csvfile, fieldnames=sheader)
         writer.writeheader()
         for di in w:
             writer.writerow({sheader[0]:di[0],sheader[1]:di[1], sheader[2]:di[2],
                sheader[3]:di[3],sheader[4]:di[4], sheader[5]:di[5], sheader[6]:di[6]})
