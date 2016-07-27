# -*- coding: utf-8 -*-
from nltk.tokenize import sent_tokenize
import networkx as nx
import json
from math import log
import nltk
BLOG_DATA = 'feed.json'

def sentences(text):

    return sent_tokenize(text)

def connect(nodes):
    """ Return a list of edges connecting the nodes,
    where the edges are given a weight based on their
    similarity.
    """
    return [(start, end, similarity(start, end))
                        for start in nodes
                        for end in nodes
                        if start is not end]

def similarity(c1, c2):
    """ Return the amount of similarity between two chunks"""
    return len(common_words(c1, c2)) / (log(len(words(c1))) + log(len(words(c2))))

def rank(nodes, edges):
    """ Return a dictionary containing the scores for each vertex"""
    graph = nx.DiGraph()
    graph.add_nodes_from(nodes)
    graph.add_weighted_edges_from(edges)
    return nx.pagerank(graph)

def summarize(text, num_summaries=5):
    """ Create a small summaries of a larger text."""
    nodes = sentences(text)
    edges = connect(nodes)
    scores = rank(nodes, edges)
    return sorted(scores)[:num_summaries]

def common_words(c1, c2):
    return list(set(c1) & set(c2))

def words(c):
    normalized_sentences = [s.lower() for s in c]
    words = [w.lower() for sentence in normalized_sentences for w in
            nltk.tokenize.word_tokenize(sentence)]
    return words
