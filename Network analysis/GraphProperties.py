import pandas as pd
import numpy as np
import networkx as nx


def graph_info(G, name='Full'):
    lists = np.transpose([x.split(': ') for x in nx.info(G).split('\n')])
    df = pd.DataFrame(lists)
    df.iloc[1, 0] = name
    df.columns = df.iloc[0]
    df = df[1:]
    return df


def net_prop_dict(G, name):
    prop_dict = {}
    prop_dict['Name'] = name
    prop_dict['Reciprocity'] = nx.reciprocity(G)
    prop_dict['Transitivity'] = nx.transitivity(G)
    prop_dict['Average_clustering'] = nx.average_clustering(G)
    prop_dict['Edge_density'] = nx.classes.function.density(G)
    prop_dict['No_strongly_connected_components'] = nx.algorithms.components.number_strongly_connected_components(
        G)
    prop_dict['No_weakly_connected_components'] = nx.algorithms.components.number_weakly_connected_components(
        G)
    return prop_dict


def to_k_core(G, k=10):
    return nx.k_core(G, k)
