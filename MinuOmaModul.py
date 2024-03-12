def loe_ankeet(fail:str)->any:
    fail=open(fail,"r",encoding="utf-8")
    kus=[]
    vas=[]
    #kus_vas={}
    for line in fail:
        n=line.find(":") #-разделитель,разграничитель
        kus.append(line[0:n].strip())
        vas.append(line[0+1:len(line)].strip())
    
        #k,v=line.strip().split(":") 
        #kus_vas[k]=v #-работа со словорями

    fail.close()
    return kus,vas  #,kus_vas
def loe_failist(fail:str)->list:
    """
    """
    f=open(fail,"r",encoding="utf-8")
    oiged=[]
    for rida in f:
        oiged.append(rida.strip())
    f.close
    return oiged

