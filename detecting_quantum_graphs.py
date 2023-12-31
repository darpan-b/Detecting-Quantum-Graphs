from max_matching import Node, Match
import convert_g_to_mcg
import check_if_connected

''' Just an utility function for checking connectivity'''
def dfs(adjacency_list, visited, curnode, avoid1, avoid2, avoid3):
    if curnode == avoid1 or curnode == avoid2 or curnode == avoid3: return
    visited[curnode] += 1
    for e in adjacency_list[curnode]:
        if e == avoid1 or e == avoid2 or e == avoid3: continue
        if visited[e] > 0: continue
        dfs(adjacency_list, visited, e, avoid1, avoid2, avoid3)


''' Returns True if the graph is 2-edge-connected, otherwise returns False'''
def check_if_2_connected(adjacency_list, nv):
    # checking for 2-connectivity
    for i in range(nv):
        for j in range(i+1, nv):
            tdfs = 0
            while tdfs == i or tdfs == j: tdfs += 1
            visited = [0 for i in range(nv)]
            dfs(adjacency_list, visited, tdfs, i, j, -1)
            for k in range(nv):
                if k == i or k == j: continue
                if visited[k] == 0: return True
    return False

''' Returns True if the graph is 3-edge-connected, otherwise returns False'''
def check_if_3_connected(adjacency_list, nv):
    # checking for 3-connectivity
    for i in range(nv):
        for j in range(i+1, nv):
            for k in range(j+1, nv):
                tdfs = 0
                while tdfs == i or tdfs == j or tdfs == k: tdfs += 1
                visited = [0 for i in range(nv)]
                dfs(adjacency_list, visited, tdfs, i, j, k)
                for l in range(nv):
                    if l == i or l == j or l == k: continue
                    if visited[l] == 0: return True
    return False





''' The following function takes in the adjacency list of a graph G,
    an array containing the degree of each vertex in the graph,
    and the total number of vertices in the graph.

    It returns k, where k is the ** matching index of G (denoted by $\mu$) **.
    If $\mu(G) = 2$, then G is said to be a TYPE 2 graph.

    If $\mu(G) \ne 2$, then the function states the reason why it is not a TYPE 2 graph. 
'''
def find_mu(adjacency_list, degrees, nv):
    v = 0 # Selecting an arbitrary vertex

    if max(degrees) >= 5: return 1 # From Observation 3.9

    ''' In the algorithm, it states that for all pairs of edges {e_1, e_2} incident on v,
        pick arbitrary perfect matchings M_1, M_2 such that e_1 \in M_1 and e_2 \in M_2,
        and if M_1 U M_2 is a hamiltonian cycle, then add it to the list of hamiltonian
        cycles.

        In the implementation however, for simplification (and optimization) purposes
        we pick an arbitrary perfect matching M_i for any edge e_i adjacent to v. Now,
        we check if there exists any such M_i, M_j (i \ne j) such that M_i U M_j is a
        hamiltonian cycle. If we find such M_i and M_j, we stop looking for any other
        hamiltonian cycles (because later on we anyway utilize only a single hamiltonian
        cycle to check the satisfiability of Properties 1, 2 and 3) and then move on to 
        checking whether the hamiltonian cycle satisfies Properties 1, 2 and 3.
    '''

    all_matchings = []
    for u in adjacency_list[v]:
        nodes = [Node() for i in range(nv - 2)]
        prev_value = [i for i in range(nv)]
        imap = {}
        tval = 0
        for e in nodes:
            imap[e.index] = tval
            tval += 1
        for i in range(nv):
            if i == u or i == v: continue
            curno = i
            if i > u: curno -= 1
            if i > v: curno -= 1
            prev_value[curno] = i
        for i in range(nv):
            if i == u or i == v: continue
            curnode = i
            if i > u: curnode -= 1
            if i > v: curnode -= 1
            for e in adjacency_list[i]:
                neighnode = e
                if e == u or e == v: continue
                if e > u: neighnode -= 1
                if e > v: neighnode -= 1
                nodes[curnode].neighbors.append(nodes[neighnode])
        
        match = Match(nodes) # This contains the maximum matching of the graph G, EXCLUDING THE VERTICES u and v
                             # In this way, we can obtain the maximum matching of G such that it contains the edge (u, v)
        un = match.unmatched_nodes()

        already_present = set()
        current_matching = [[min(u,v), max(u,v)]] # supposed to contain the matching of the max graph containing the edge (u, v)
        for node in nodes:
            if node.mate != None:
                assert node.mate.mate == node
                num1 = imap.get(node.index)
                num2 = imap.get(node.mate.index)

                if prev_value[num1] in already_present: continue
                smaller, bigger = prev_value[num1], prev_value[num2]
                if smaller > bigger: smaller, bigger = bigger, smaller
                current_matching.append([smaller, bigger])
                already_present.add(prev_value[num1])
                already_present.add(prev_value[num2])

        all_matchings.append(current_matching) # add the current matching to the list of all matchings


    tot_matchings = len(all_matchings)

    hamiltonian_cycle = []
    w1, w2 = [-1 for i in range(nv)], [-1 for i in range(nv)]

    for i in range(tot_matchings):
        if hamiltonian_cycle: break
        for j in range(i+1, tot_matchings):
            m1, m2 = all_matchings[i], all_matchings[j]

            # check if m1 U m2 form a hamiltonian cycle

            assert(len(m1) == len(m2) and len(m1) == nv//2)
            is_hamiltonian = True

            for k in range(nv//2):
                if m2[k] in m1:
                    is_hamiltonian = False
                    break
            if not is_hamiltonian: continue

            # checking whether it is only 1 hamiltonian cycle or multiple hamiltonian cycles
            all_here = []
            for e in m1: all_here.append(e)
            for e in m2: all_here.append(e)
            all_here.sort()
            count_vertices = {}
            for k in range(nv):
                count_vertices[all_here[k][0]] = count_vertices.get(all_here[k][0], 0) + 1
                count_vertices[all_here[k][1]] = count_vertices.get(all_here[k][1], 0) + 1
                if max(count_vertices.values()) == 2 and min(count_vertices.values()) == 2 and k != nv-1:
                    is_hamiltonian = False
                    break
            if not is_hamiltonian: continue

            for e in m1:
                w1[e[0]], w1[e[1]] = e[1], e[0]
                hamiltonian_cycle.append(e)
            for e in m2:
                w2[e[0]], w2[e[1]] = e[1], e[0]
                hamiltonian_cycle.append(e)
            break
    
    if not hamiltonian_cycle:
        print('NOT TYPE 2 BECAUSE NO HAMILTONIAN CYCLES WERE FOUND')
        return 1
    

    # Re-numbering the vertices in the order that they are present in the hamiltonian cycle for convenience
    re_numbering = [-1 for i in range(nv)]
    re_numbering[0] = 0
    current_number = 1
    current_vertex = w1[0]
    while current_vertex != 0:
        re_numbering[current_vertex] = current_number
        current_number += 1
        if current_number % 2 == 0:
            current_vertex = w2[current_vertex]
        else:
            current_vertex = w1[current_vertex]



    print('=================================================')
    print('Re-numbering of vertices:')
    print('=================================================')
    for i in range(nv):
        print('Original numbering:', i+1, 'Re-numbering:', re_numbering[i])
    print('=================================================\n')

    edge_set = []
    '''checking property 1'''
    for i in range(nv):
        for u in adjacency_list[i]:
            if u > i: continue
            edge_set.append([u, i])
            found = False
            for e in hamiltonian_cycle:
                if (e[0] == i and e[1] == u) or (e[0] == u and e[1] == i):
                    found = True
                    break
            if not found:
                if re_numbering[u]%2 != re_numbering[i]%2:
                    print('NOT TYPE 2 BECAUSE ILLEGAL EDGE WAS FOUND')
                    return 1

    '''checking property 2'''
    n_es = len(edge_set)
    drum_no = [-1 for i in range(n_es)]
    drums = 0
    for i in range(n_es):
        if edge_set[i] in hamiltonian_cycle:
            drum_no[i] = -2
            continue
        if [edge_set[i][1],edge_set[i][0]] in hamiltonian_cycle:
            drum_no[i] = -2
            continue
        for j in range(i+1, n_es):
            if edge_set[i][0] == edge_set[j][1] and edge_set[i][1] == edge_set[j][0]:
                continue
            e1, e2 = edge_set[i], edge_set[j]
            if e2 in hamiltonian_cycle: continue
            if [edge_set[j][1],edge_set[j][0]] in hamiltonian_cycle: continue


            v1, v2, v3, v4 = re_numbering[e1[0]], re_numbering[e1[1]], re_numbering[e2[0]], re_numbering[e2[1]]

            # check if the edges e1 and e2, which, if legal and non-cyclic edges, form a valid drum or not

            lv = [v1, v2, v3, v4]
            lv.sort()
            if not((lv[0] == v1 and lv[2] == v2) or (lv[0] == v2 and lv[2] == v1) or (lv[1] == v1 and lv[3] == v2) or (lv[1] == v2 and lv[3] == v1)):
                continue
            
            dec = 0
            is_drum = True
            for k in range(4):
                if lv[k] < lv[k-1]: dec += 1
                if lv[k]%2 != lv[k-2]%2:
                    is_drum = False
                    break
            if not is_drum or dec != 1:
                print('NOT TYPE 2 BECAUSE CROSSING PAIR DOES NOT FORM A DRUM')
                return 1
            def is_adj_vertex(x,y): return abs(x-y) == 1 or abs(x-y) == nv-1
            if (is_adj_vertex(lv[0],lv[1]) and is_adj_vertex(lv[2],lv[3])) or (is_adj_vertex(lv[0],lv[3]) and is_adj_vertex(lv[1],lv[2])):
                if drum_no[i] != -1 or drum_no[j] != -1:
                    print('NOT TYPE 2 BECAUSE LEGAL EDGE IS PART OF MULTIPLE CROSSING PAIRS')
                    return 1
                drums += 1
                drum_no[i], drum_no[j] = drums, drums
            else:
                return 1

    '''checking property 3'''
    if -1 in drum_no:
        print('NOT TYPE 2 BECAUSE LEGAL EDGE IS NOT PART OF ANY DRUMS')
        return 1
    if max(drum_no) == -2 and min(drum_no) == -2: return 2
    d_count = [0 for i in range(drums)]
    for i in range(n_es):
        if drum_no[i] == -1:
            print('NOT TYPE 2 BECAUSE LEGAL EDGE IS NOT PART OF ANY DRUMS')            
            return 1
        if drum_no[i] == -2: continue
        d_count[drum_no[i]-1] += 1
    if max(d_count) == 2 and min(d_count) == 2: return 2
    else: return 1


''' returns True if G is Type 2, otherwise returns False '''
def chandran_gajjala_is_type2(adjacency_list, degrees, nv):
    return find_mu(adjacency_list, degrees, nv) == 2


def main():
    nv, ne = 0, 0
    print('Number of vertices in the graph:')
    nv = int(input())
    adj_list = [[] for i in range(nv)]
    degree = [0 for i in range(nv)]
    print('Number of edges in the graph:')
    ne = int(input())
    capacity = [[0 for i in range(nv)] for j in range(nv)]
    print('Edges of the graph (1-indexed):')
    for i in range(ne):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj_list[u].append(v)
        adj_list[v].append(u)   
        degree[u] += 1
        degree[v] += 1
        capacity[u][v] = 1
        capacity[v][u] = 1
    is_graph_connected = check_if_connected.check_connected(adj_list, nv)
    if not is_graph_connected:
        print('Graph is not connected')
        exit(0)

    # If the graph is not a matching-covered graph, convert it to a matching covered graph
    adj_list = convert_g_to_mcg.convert_to_mcg(adj_list, nv)

    # Check if the resulting matching-covered graph is connected or not
    is_graph_connected = check_if_connected.check_connected(adj_list, nv)
    
    
    if not is_graph_connected:
        print('Matching covered graph is not connected')
        exit(0)
    is_2_connected = check_if_2_connected(adj_list, nv)
    is_3_connected = check_if_3_connected(adj_list, nv)


    print('---------------------------------------------------------')
    print('Is 2-connected:', 'Yes' if is_2_connected else 'No')
    print('Is 3-connected:', 'Yes' if is_3_connected else 'No')
    print('---------------------------------------------------------')
    print('')
    print('')


    is_type2 = chandran_gajjala_is_type2(adj_list, degree, nv) # Is it a type-2 graph or not
    
    
    print('===========================================')
    print('Is type 2:', 'Yes' if is_type2 else 'No')
    print('===========================================')

main()
