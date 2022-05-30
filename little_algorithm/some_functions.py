from collections import defaultdict


# 归并排序
def mergesort(seq):
    mid = len(seq) // 2
    lft, rgt = seq[:mid], seq[mid:]
    if len(lft) > 1:
        lft = mergesort(lft)
    if len(rgt) > 1:
        rgt = mergesort(rgt)
    res = []
    while lft and rgt:
        if lft[-1] >= rgt[-1]:
            res.append(lft.pop())
        else:
            res.append(rgt.pop())
    res.reverse()
    return (lft or rgt) + res


# 计数排序
def counting_sort(a, key=lambda x: x):
    b, c = [], defaultdict(list)
    for x in a:
        c[key(x)].append(x)
    for k in range(min(c), max(c) + 1):
        b.extend(c[k])
    return b


def walk(g, s, ss: set = ()):
    # 遍历一个表示为邻接集的图结构的连通分量
    p, q = dict(), set()
    p[s] = None
    q.add(s)
    while q:
        u = q.pop()
        for v in g[u].difference(p, ss):
            q.add(v)
            p[v] = u
    return p


def dfs_topsort(g):
    # 基于深度优先搜索的拓扑排序
    s, res = set(), []

    def recurse(u):
        if u in s:
            return
        s.add(u)
        for v in g[u]:
            recurse(v)
        res.append(u)

    for u in g:
        recurse(u)
    res.reverse()
    return res


def tr(g):
    # 有向边反向
    gt = {}
    for u in g:
        gt[u] = set()
    for u in g:
        for v in g[u]:
            gt[v].add(u)
    return gt


def scc(g):
    gt = tr(g)
    sccs, seen = [], set()
    dfs_result = dfs_topsort(g)
    for u in dfs_result:
        if u in seen:
            continue
        c = walk(gt, u, seen)
        seen.update(c)
        sccs.append(c)
    return sccs


if __name__ == '__main__':
    # test = mergesort([7, 5, 8,3,32,34,6,4636,6,4,3,646,])
    # test = counting_sort
    s_test = 'a'
    g_test = {'a': {'b', 'c'}, 'b': {'d', 'i'}, 'c': {'d'}, 'd': {'a', 'h'},
              'e': {'f'}, 'f': {'g'}, 'g': {'e', 'h'}, 'h': {'i'}, 'i': {'h'}}
    path = walk(g_test, s_test)
    top_sort = dfs_topsort(g_test)
    scc_result = scc(g_test)
