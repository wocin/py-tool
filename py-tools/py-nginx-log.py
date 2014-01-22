#!/usr/bin/env python
#By wocin
#Email ---
#analys nginx log
#-------------------I am boring line------------------------------------
import sys
def analog():
    iplist={}
    codelist={}
    flowlist={}
    reslist={}
    final={}
    logs=open(sys.argv[1],'r').readlines()
    for line in logs:
        code=line.split()[8]
        ipadd=line.split()[0]
        flow=line.split()[9]
        res=line.split()[6]
        iplist[ipadd]=iplist.get(ipadd,0)+1
        codelist[code]=codelist.get(code,0)+1
        reslist[res]=reslist.get(res,0)+1
        final[code]=res 
        for code in codelist.keys():
            final[code]=[]
            for res in reslist.keys():
                final[code].append(res)
    for item in final.items():
        print '%s --->%s ' %(item[0],codelist[item[0]])
        print 'list here:\n\n%s\n' %item[1]
    for item in  iplist.items():
        print '%s  --->%s ' %(item[0] ,item[1])
def main():
    analog()
    
if __name__ == '__main__':
    main()