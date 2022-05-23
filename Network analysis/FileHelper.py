import pandas as pd
import numpy as np
import networkx as nx


def drop_sentiment(df):
    return df.drop(columns=['sentiment'])


def core_to_file(G, target):
    df = nx.to_pandas_edgelist(G)
    df.to_csv('./Data/K_cores/'+target+'.csv', index=False)
