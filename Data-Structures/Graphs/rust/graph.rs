use std::fs;

#[derive(Debug)]
struct Node {
    data: i32,
    neighbors: Vec<usize>,
}

struct Graph {
    nodes: Vec<Node>,
}

impl Graph {
    fn add_node(&mut self, data: i32) -> usize {
        let index = self.nodes.len();
        self.nodes.push(Node {
            data,
            neighbors: Vec::new(),
        });
        index
    }

    fn add_edge(&mut self, node_a: usize, node_b: usize) {
        self.nodes[node_a].neighbors.push(node_b);
        // self.nodes[node_b].neighbors.push(node_a); // For undirected graphs
    }

    fn print_nodes(&mut self) {
        for node in self.nodes.iter() {
            println!("{:?}", node);
        }
    }
}

fn main() {
    let mut graph = Graph { nodes: Vec::new() };

    let node1 = graph.add_node(14);
    let node2 = graph.add_node(30);
    let node3 = graph.add_node(865);
    let node4 = graph.add_node(578);

    graph.add_edge(node1, node2);
    graph.add_edge(node3, node4);
    graph.add_edge(node1, node3);

    let contents = fs::read_to_string("../test.txt").expect("Error reading file");
    println!("File contents: {}", contents);

    graph.print_nodes();

    println!("Test.");

    // Implement your logic to traverse or work with the graph structure
}
