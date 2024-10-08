use std::collections::{HashMap, HashSet};
use lazy_static::lazy_static;
use regex::Regex;

lazy_static! {
    static ref route_regex: Regex = Regex::new(r"^(\w+) to (\w+) = (\d+)$").unwrap();
}
pub fn solve_part_1(data: String) -> i64 {
    let mut nodes: HashSet<&str> = HashSet::new();
    let mut adjacency_sets: HashMap<&str, HashSet<&str>> = HashMap::new();
    for (_, [source, destination, _ ]) in route_regex.captures_iter(data.as_str()).map(|c| c.extract()) {
        nodes.insert(source);
        nodes.insert(destination);
        if !adjacency_sets.contains_key(source) {
            adjacency_sets.insert(source, HashSet::new());
        }
        if !adjacency_sets.contains_key(destination) {
            adjacency_sets.insert(destination, HashSet::new());
        }
        adjacency_sets.get_mut(source).unwrap().insert(destination);
        adjacency_sets.get_mut(destination).unwrap().insert(source);
    };
    let mut node_to_key: HashMap<&str, usize> = HashMap::new();
    let mut key_to_node: HashMap<usize, &str> = HashMap::new();
    for (key, node) in nodes.iter().enumerate() {
        node_to_key.insert(node, key);
        key_to_node.insert(key, node);
    }
    let mut graph = vec![vec![u16::MAX; nodes.len()]; nodes.len()];
    for (_, [source, destination, distance_str ]) in route_regex.captures_iter(data.as_str()).map(|c| c.extract()) {
        let distance = distance_str.parse::<u16>().unwrap();
        let source_key = *node_to_key.get(source).unwrap();
        let distination_key = *node_to_key.get(destination).unwrap();
        graph[source_key][distination_key] = distance;
        graph[distination_key][source_key] = distance;
    }
    let mut shortest_path: HashSet<&str> = HashSet::new();
    let mut u = *nodes.iter().next().unwrap();
    loop {
        shortest_path.insert(u);
        if shortest_path.len() == nodes.len() {
            break
        }
    }
    0
}

pub fn solve_part_2(_: String) -> i64 {
    0
}

#[cfg(test)]
mod test_solver {
    use super::*;

    #[test]
    fn test_part_1() {
        assert_eq!(605, solve_part_1(r#"London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141"#.parse().unwrap()));
    }

    #[test]
    fn test_part_2() {
        assert_eq!(0, solve_part_2("".parse().unwrap()));
    }
}
