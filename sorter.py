
import sys

def coupUrl(ligne):
	url_activate=False
	url=""
	for i in ligne :
		if (i=="<") :
			url_activate=True
		if (url_activate==True and i!=">") :
			url=url+i
		if (url_activate==True and i==">") : 
			url_activate=False
			url=url+">"
	return url

def coupRank(ligne):
	pageRankCapture=False
	pageRank=""
	dom=ligne.split(" ")
	pageRank=dom[len(dom)-1]
	pageRank=pageRank[:-2]
	return pageRank


if __name__ == "__main__" :
	maxInstantUrl=""
	maxInstantPageRank=0.0
	with open(str(sys.argv[1]), "r") as file :
		for line in file : 
			print(line)
			if (line[0]=="<"):
				instantUrl=coupUrl(line)
				instantRank=coupRank(line)
				print(instantRank)
				print(float(instantRank))

				if (maxInstantPageRank<float(instantRank)):
					maxInstantUrl=instantUrl
					maxInstantPageRank=float(instantRank)

	print(maxInstantUrl)
	print(maxInstantPageRank)




