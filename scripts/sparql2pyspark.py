import sys

if __name__ == "__main__" :

    nb_tp = 0
    tp_list = []
    nb_spo = 0
    next_spo_filter = False
    next_join = False
    nb_join = 0

    with open(str(sys.argv[1]),'r') as sparql_query:
        for line in sparql_query.readlines():
            tp = "tp"+str(nb_tp)+"=triples.filter(lambda x: x["
            for item in line.split(" "):
                if item and item not in ["SELECT","WHERE",")",",","}","*\n","{\n"]:
                    if "?" not in item and "\n" not in item and ".FILTER(" not in item:
                        if item != "strStarts(" and not next_spo_filter: 
                            tp = tp+str(nb_spo)+"]==\""+item+"\""+" and  x["
                        elif not next_spo_filter:
                            tp = tp+str(nb_spo)+"].startswith("
                            next_spo_filter = True
                        else:
                            tp = tp+str(item)+")"
                            next_spo_filter = False
                    nb_spo+=1
                    if "\n" in item:
                        if tp.endswith(" and  x["):
                            tp = tp[:len(tp)-8]
                        tp = tp+").keyBy(lambda x: x[0])\n"
                        tp_list.append(tp)
                        nb_tp+=1
                        nb_spo=0
                    if ".FILTER" in item:
                        nb_spo-=2
    
    with open(str(sys.argv[2]),'w') as pyspark_query:
        for tp in tp_list:
            pyspark_query.write(tp)
        for tp in tp_list:
            if not next_join:
                pyspark_query.write("joined"+str(nb_join)+"="+str(tp.split("=")[0])+".join(")
                next_join = True
            else:
                pyspark_query.write(str(tp.split("=")[0])+")\n")
                next_join = False
                nb_join+=1
        
            