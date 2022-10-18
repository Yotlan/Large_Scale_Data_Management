import sys

if __name__ == "__main__" :

    max_entity_pagerank = "None"
    max_pagerank = 0.0

    second_max_entity_pagerank = "None"
    second_max_pagerank = 0.0

    third_max_entity_pagerank = "None"
    third_max_pagerank = 0.0

    with open(str(sys.argv[1]),'r') as data_file:
        for line in data_file.readlines():
            entity = line.split(",")[0].replace("(","")
            entity_pagerank = line.split(",")[1].replace(")","")
            if float(entity_pagerank) > max_pagerank :
                max_entity_pagerank = str(entity)
                max_pagerank = float(entity_pagerank)
            elif float(entity_pagerank) > second_max_pagerank:
                second_max_entity_pagerank = str(entity)
                second_max_pagerank = float(entity_pagerank)
            elif float(entity_pagerank) > third_max_pagerank:
                third_max_entity_pagerank = str(entity)
                third_max_pagerank = float(entity_pagerank)

    print("1. Entity " + str(max_entity_pagerank) + " have the best pagerank with " + str(max_pagerank))
    print("2. Entity " + str(second_max_entity_pagerank) + " have the best pagerank with " + str(second_max_pagerank))
    print("3. Entity " + str(third_max_entity_pagerank) + " have the best pagerank with " + str(third_max_pagerank))