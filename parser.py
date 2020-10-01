tokens=["struct ","};"]
idls=dict()
body=False
with open("bb.idl") as f:
    lines=f.read().splitlines()

for line in lines:
    if(line[:len(tokens[0])]==tokens[0]):
        st_name=line[len(tokens[0]):-1]
        filed=[]
        body=True
    elif(line[:len(tokens[1])]==tokens[1]):
        idls[st_name]=filed
        body=False
    else:
        if(body):
            if(line[0]=="\t" or line[0:4]=="    "):
                part=line.split()
                vType=" ".join(part[:-1])
                count=1
                vName=part[-1][:-1]
                if("[" in vName):
                    count=int(vName.split("[")[1].split("]")[0])
                    vName=vName.split("[")[0]
                filed.append((vType,vName,count))
print(idls)