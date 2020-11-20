from pathlib import Path
base_dir=Path(__file__).resolve().parent
logfile=str(base_dir)+"/log.txt"

with open(logfile, 'r') as f:
        lines = f.readlines()
        for l in lines:
            if 'Open url' in l:
                ciganum = 0
                ganum = 0
                url=l.split('=: ',1)[1]
            if '- GA code' in l:
                ganum = ganum +1
                # print('ganum:'+str(ganum))
                if ganum > 1:
                    print('GA代码响应超过1,目前为'+str(ganum)+'=='+url)
            if '- CIGA code' in l:
                ciganum = ciganum +1
                # print('ciganum:'+str(ciganum))
                if ciganum > 1:
                    print('CIGA代码响应超过1,目前为'+str(ciganum)+'=='+url)