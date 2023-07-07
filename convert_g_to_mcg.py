''' This program aims to convert a given graph to its corresponding matching covered graph. '''
''' This is supposed to be done by checking an edge and seeing if it is part of a perfect matching or not. '''

from max_matching import Node, Match

def convert(edges, nv):

    esz=len(edges)
    edges_copy=[]
    already_removed=set()
    for i in range(esz):
        v1, v2=edges[i][0], edges[i][1]
        edges_copy.clear()
        for j in range(esz):
            if j in already_removed: continue
            if edges[j][0]==v1 or edges[j][0]==v2 or edges[j][1]==v1 or edges[j][1]==v2:
                continue
            cv1, cv2=edges[j][0], edges[j][1]

            if v1==nv-2:
                pass
            elif v2==nv-2:
                if cv1==nv-1 and v1<nv-2: cv1=v1
                elif cv2==nv-1 and v1<nv-2: cv2=v1
            else:        
                if cv1==nv-2 and v1<nv-2: cv1=v1
                elif cv2==nv-2 and v1<nv-2: cv2=v1
                if cv1==nv-1 and v2<nv-2: cv1=v2
                elif cv2==nv-1 and v2<nv-2: cv2=v2
            edges_copy.append((cv1, cv2))
            edges_copy.append((cv2, cv1))


        match = Match.from_edges(nv-2, edges_copy)
        unmatched_nodes = match.unmatched_nodes()
        if unmatched_nodes>0:
            already_removed.add(i)

    edges_copy=[]
    for e in edges: edges_copy.append(e)
    for e in already_removed: edges_copy.remove(edges[e])
    return edges_copy


def convert_to_mcg(adj_list, nv):
    edges_here=[]
    for i in range(nv):
        for e in adj_list[i]:
            if e>i:
                edges_here.append([i, e])

    final_edges=convert(edges_here, nv)
    if final_edges:
        print('')
        print('--------------------------------------------------')
        print('Edges in the matching covered graph are:')
        for e in final_edges:
            print('(', e[0]+1, ',', e[1]+1, ')')
        print('--------------------------------------------------\n')

    for i in range(nv):
        for e in adj_list[i]:
            if e>i:
                if [i, e] not in final_edges:
                    adj_list[i].remove(e)
                    adj_list[e].remove(i)
    return adj_list

