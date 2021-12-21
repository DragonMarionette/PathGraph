"""
Written 12/20/2021 by Dan Strauss

This program represents 2-colored path graphs as strings in binary
A 1 represents a vertex included in a given set
A 0 represents a vertex not included in that set
e.g. 10010 represents the set containing only the first and fourth vertices of a 5-vertex path graph

This code has few safeguards but will usually throw an error if you give a function bad input
"""
import re


# returns a string of length size which is the binary representation of n
def to_bin(n: int, size: int):
    return format(n, 'b').zfill(size)


# returns the integer corresponding to a given 2-colored path graph
def to_int(g: str):
    return int(g, 2)


# returns a generator of all 2-colored path graphs of length size, represented as binary strings
def graphs_of_len(size):
    return (to_bin(n=i, size=size) for i in range(2**size))


# returns true iff path graph g has a dominating set colored with 1
def is_dominating(g: str):
    assert(re.match(r'^(0|1)*$', g))  # ensure g is a string of ones and zeros

    # forgive me for this regex. It matches strings where every character is either 1 or adjacent to a 1
    # ^     start of string. Redundant with .match() but included for cross-compatibility
    # 0?    optional leading zero
    # 1     digit one
    # (0{0,2}1)*    (0, 1, or 2 zeros followed by a one) repeated 0 or more times
    # 0?    optional lagging zero
    # $     end of string
    return re.match(r'^0?1(0{0,2}1)*0?$', g)


# example driver code to generate dominating sets for the path graph with 5 vertices
if __name__ == "__main__":
    for graph in graphs_of_len(5):
        if is_dominating(graph):
            print(graph)
