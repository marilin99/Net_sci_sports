import pandas as pd
import numpy as np
import networkx as nx


def drop_sentiment(df):
    return df.drop(columns=['sentiment'])


def core_to_file(G, target):
    df = nx.to_pandas_edgelist(G)
    df.to_csv('./Data/K_cores/'+target+'.csv', index=False)


def to_df(source):
    df = pd.read_csv(source)
    df = df.astype({'source': 'int64', 'target': 'int64'})
    return df


def switch_direction(df):
    return df.rename(columns={"source": "target", "target": "source"})


def collaps_to_wo_sentiment(df):
    df_collapsed = df.drop(columns=['sentiment'])
    df_collapsed = df_collapsed.groupby(['source', 'target']).agg({
        'weight': 'sum'}).reset_index()
    return df_collapsed


def graph_to_csv(df, name):
    df.to_csv('./Data/'+name+'.csv', index=False)


def collapsed_to_csv(df, name):
    df.to_csv('./Data/Collapsed/'+name+'.csv', index=False)
