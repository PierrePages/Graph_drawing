import workalendar



def find_neighbour(data):
    vertex_list = []
    neighbour_list = []
    edge_list = get_edges_coord(data)
    node_list = data.get('nodes')
    for node in node_list:
        vertex_list.append(((node.get('x')), node.get('y')))
    
    for vertex in vertex_list:
        x = vertex[0]
        y = vertex[1]

        neighbour = []

        for edge in edge_list:
            for i in range(len(edge)):
                x_bend = edge[i][0]
                y_bend = edge[i][1]

                if x_bend == x and y_bend == y:
                    if i==0:
                        if (edge[i+1][0], edge[i+1][1]) in vertex_list:
                            neighbour.append((edge[i+1][0], edge[i+1][1]))
                        
                    if i==len(edge)-1:
                        if (edge[i-1][0], edge[i-1][1]) in vertex_list:
                            neighbour.append((edge[i-1][0], edge[i-1][1]))

                    if (i !=0) and (i != len(edge)-1):
                        if (edge[i-1][0], edge[i-1][1]) in vertex_list and (edge[i+1][0], edge[i+1][1]) in vertex_list:
                            neighbour.append((edge[i-1][0], edge[i-1][1]))
                            neighbour.append((edge[i+1][0], edge[i+1][1]))
        neighbour_list.append(neighbour)
    return neighbour_list

neighbour_list = find_neighbour(data)
vertex_list = get_point_coord(data)




def compute_all_centroid(data):
    neighbour_list = find_neighbour(data)
    centroids = []
    for cycle in neighbour_list:
        centroids.append(compute_centroid(cycle))
    return centroids
