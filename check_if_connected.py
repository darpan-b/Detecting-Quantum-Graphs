def dfs(curnode, adj_list, vis):
    vis.add(curnode)
    for e in adj_list[curnode]:
        if e not in vis:
            dfs(e, adj_list, vis)



def check_connected(adj_list, nv):
    vis=set()
    dfs(0, adj_list, vis)
    if len(vis)<nv: return False
    else: return True

