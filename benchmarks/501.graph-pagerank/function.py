import datetime
import igraph

def handler(event, iteration, run):

    size = event.get('size')
    graph_generating_begin = datetime.datetime.now()
    graph = igraph.Graph.Barabasi(size, 10)
    graph_generating_end = datetime.datetime.now()

    process_begin = datetime.datetime.now()
    result = graph.pagerank()
    process_end = datetime.datetime.now()

    graph_generating_time = (graph_generating_end - graph_generating_begin) / datetime.timedelta(microseconds=1)
    process_time = (process_end - process_begin) / datetime.timedelta(microseconds=1)
    with open(f'/vagrant/results/runs/501.graph-pagerank/501.graph-pagerank_result_{run}.csv', 'a') as f:
      f.writelines(f"{iteration},{process_time}\n")
    return {
            'result': result[0],
            'measurement': {
                'graph_generating_time': graph_generating_time,
                'compute_time': process_time
            }
    }
