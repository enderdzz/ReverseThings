import re
from dlit_data import dlit
from binascii import unhexlify
def preprocess():
    def_str = "\$(\w+) = NUMBER \( \" (\d+) \" \)"
    #print(def_str)
    with open("extract.au3", 'r') as f:
        content = f.read()
    res = re.findall(def_str, content)
    var = {}
    if res:
        for i in res:
            var[i[0]] = i[1]
            #print(i[0], i[1])
    with open("prob.au3", 'r') as f:
        content = f.read()
    def_str = "\$(\w+)" # or "\$(?:\w+)" BUT still need to use finditer()
    res = re.finditer(def_str, content)
    
    # if res:
    #     for i in res:
    #         if i[1] in var.keys():
    #             content = re.sub('\\'+i[0], var[i[1]], content)
    # with open("p_prob.au3", 'w') as f:
    #     f.write(content)

    with open("p_prob.au3", 'r', encoding='utf-8') as f:
        content = f.read()
    Dlit = ''.join(dlit)
    Dlit = Dlit.split("4FD5$")
    for i in range(len(Dlit)):
        Dlit[i] = unhexlify(Dlit[i])
        print(i, Dlit[i])
    
    def_str = "ender_trans \( \$OS \[ (\d+) \] \)"
    res = re.finditer(def_str, content)
    # if res:
    #     for i in res:
    #         print(f"ender_trans \( \$OS \[ {i[1]} \] \)", Dlit[int(i[1])-1].decode())
    #         content = re.sub(f"ender_trans \( \$OS \[ {i[1]} \] \)", '"'+Dlit[int(i[1])-1].decode()+'"', content)
    # with open("pp_prob.au3", 'w', encoding='utf-8') as f:
    #     f.write(content)
        
if __name__ == "__main__":
    preprocess()