import json
import sys
import seaborn as sns
import pandas as pd
import re
import matplotlib.pyplot as plt

def plot_data(nt_data, json_load):
    df = pd.DataFrame(data={'implementation':[], 'node':[], 'execution_time':[]})
    for implementation in json_load:
        for execution_time in json_load[implementation]:
            for node in json_load[implementation][execution_time]:
                new_row = {'implementation':str(implementation),'node':str(node),'execution_time':int(json_load[implementation][execution_time][node])}
                df = df.append(new_row, ignore_index=True)
    sns_plot = sns.lineplot(x="node", y="execution_time", hue="implementation", data=df)
    plt.title("Page Rank execution time")
    sns_plot.figure.savefig(str(sys.argv[2])+nt_data.split("/")[3]+".png")
    plt.clf()

if __name__ == "__main__":

    with open(sys.argv[1], 'r') as json_file:
        json_load = json.load(json_file)

    for nt_data in json_load:
        plot_data(nt_data, json_load[nt_data])