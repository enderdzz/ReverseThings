import re
with open('node-equ.js', 'r') as f:
    code = f.read()
    
with open('plain_trace', 'r') as f:
    trace = f.read()

case_dict = {}
res = code.split('case ')[1:]
for i in res:
    case_num = i[:i.find(':')]
    ctx = i.replace('\n', '')
    bd = {}
    pattern = r"if \(.*\) \{(.*)\} else \{(.*)\}"
    branch = re.search(pattern, ctx)
    if branch == None:
        pass
        #print(case_num)
    else:
        bd['T'] = branch.group(1)
        bd['F'] = branch.group(2)
    case_dict[case_num] = bd


c = trace.split('##\n')
stat_l = []
for i in c:
    t = i.split('\n')[:-1]
    bd = case_dict[t[0]]
    if bd == {}:
        continue
    if 'T' in t:
        stat = bd['T']
    else:
        stat = bd['F']
    
    if 'cc()' in stat:
        stat = stat.replace('cc()', t[-1])
    stat = stat.replace(' ', '')
    if '+=' in stat:
        stat = stat.replace('+=', '-=')
    elif '-=' in stat:
        stat = stat.replace('-=', '+=')
    stat_l.append(stat)
    #print('===================')

for i in stat_l[::-1]:
    print(i)