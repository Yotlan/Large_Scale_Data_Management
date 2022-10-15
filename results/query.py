tp0=triples.filter(lambda x: x[1]=="<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>" and  x[2]=="<https://schema.org/Mountain>").keyBy(lambda x: x[0])
tp1=triples.filter(lambda x: x[1]=="<https://schema.org/name>" and  x[2].startswith("\"P")).keyBy(lambda x: x[0])
joined0=tp0.join(tp1)
