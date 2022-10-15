import sys

if __name__ == "__main__" :

    max_entity_pagerank = "None"
    max_pagerank = 0.0

    with open(str(sys.argv[1]),'r') as data_file:
        for line in data_file.readlines():
            entity = line.split(",")[0].replace("(","")
            entity_pagerank = line.split(",")[1].replace(")","")
            if float(entity_pagerank) > max_pagerank :
                max_entity_pagerank = str(entity)
                max_pagerank = float(entity_pagerank)

    print("Entity " + str(max_entity_pagerank) + " have the best pagerank with " + str(max_pagerank))