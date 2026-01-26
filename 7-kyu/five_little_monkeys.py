def monkeys():
    l=["Five","Four","Three","Two","One"]
    r=""
    for i in l:
        r+=f"{i} little monkey{'s'*(i!='One')} jumping on the bed,\n"
        r+=f"{'One'if i!='One'else'He'} fell off and bumped his head.\n"
        r+="Mother called the doctor and the doctor said:\n"
        r+=f"{'No more monkeys jumping on the bed!'if i!='One'else'Put those monkeys right to bed!'}\n"
        if i!="One":r+="\n"
    return r.strip()
