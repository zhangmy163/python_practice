from pathlib import Path
base_dir=Path(__file__).resolve().parent
logfile=str(base_dir)+"/nissa-ciga-null.txt"
ciganum = 0
ganum = 0
url = ""
with open(logfile, 'r') as f:
        lines = f.readlines()
        for l in lines:
            # print(l)
            if 'Open url' in l:
                if (ganum != 1 or ciganum !=1) and url != "":
                    print('GA代码响应不为1,目前为'+str(ganum)+'=='+url)
                    print('CIGA代码响应不为1,目前为'+str(ciganum)+'=='+url)
                ciganum = 0
                ganum = 0
                url=l.split('=: ',1)[1]
                continue
            if '- GA code' in l:
                ganum = ganum +1
                # print('ganum:'+str(ganum))
                
            if '- CIGA code' in l:
                ciganum = ciganum +1
                # print('ciganum:'+str(ciganum))
                
            
            