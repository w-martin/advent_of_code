use lazy_static::lazy_static;
use priority_queue::PriorityQueue;
use regex::Regex;
use std::collections::{HashMap, HashSet};
use std::hash::{Hash, Hasher};

lazy_static! {
    static ref route_regex: Regex = Regex::new(r"(\w+) to (\w+) = (\d+)").unwrap();
}

struct Neighbour {
    node: String,
    distance: i64,
}

struct VisitOption {
    visited: HashSet<String>,
    head: String,
}

impl Hash for VisitOption {
    fn hash<H: Hasher>(&self, state: &mut H) {
        self.visited.iter().for_each(|v| v.hash(state));
        self.head.hash(state);
    }
}

impl PartialEq for VisitOption {
    fn eq(&self, other: &Self) -> bool {
        self.visited == other.visited && self.head == other.head
    }
}

impl Eq for VisitOption {}

pub fn solve_part_1(data: String) -> i64 {
    let graph = parse_graph(data);
    let mut q = PriorityQueue::new();
    for key in graph.keys().into_iter() {
        let mut visited = HashSet::new();
        let head = key.to_string();
        visited.insert(key.to_string());
        q.push(VisitOption { visited, head }, 0);
    }
    let mut total = i64::MAX;
    while q.len() > 0 {
        let (option, distance) = q.pop().unwrap();
        if option.visited.len() == graph.len() && distance < total {
            total = distance
        }
        for neighbour in graph.get(option.head.as_str()).unwrap().into_iter() {
            if !option.visited.contains(neighbour.node.as_str()) {
                let mut new_visited = option.visited.clone();
                new_visited.insert(neighbour.node.clone());
                let new_option = VisitOption {visited: new_visited, head: neighbour.node.clone() };
                q.push(new_option, neighbour.distance + distance);
            }
        }
    }
    total
}

fn parse_graph(data: String) -> HashMap<String, Vec<Neighbour>> {
    let mut graph: HashMap<String, Vec<Neighbour>> = HashMap::new();
    for (_, [source, destination, distance_str ]) in route_regex.captures_iter(data.as_str()).map(|c| c.extract()) {
        if !graph.contains_key(source) {
            graph.insert(source.to_string(), Vec::new());
        }
        if !graph.contains_key(destination) {
            graph.insert(destination.to_string(), Vec::new());
        }
        let distance = distance_str.parse::<i64>().unwrap();
        graph.get_mut(source).unwrap().push(Neighbour { node: destination.to_string(), distance });
        graph.get_mut(destination).unwrap().push(Neighbour { node: source.to_string(), distance });
    };
    graph
}

pub fn solve_part_2(data: String) -> i64 {
    let graph = parse_graph(data);
    let mut q = PriorityQueue::new();
    for key in graph.keys().into_iter() {
        let mut visited = HashSet::new();
        let head = key.to_string();
        visited.insert(key.to_string());
        q.push(VisitOption { visited, head }, 0);
    }
    let mut total = i64::MIN;
    while q.len() > 0 {
        let (option, distance) = q.pop().unwrap();
        if option.visited.len() == graph.len() && distance > total {
            total = distance
        }
        for neighbour in graph.get(option.head.as_str()).unwrap().into_iter() {
            if !option.visited.contains(neighbour.node.as_str()) {
                let mut new_visited = option.visited.clone();
                new_visited.insert(neighbour.node.clone());
                let new_option = VisitOption {visited: new_visited, head: neighbour.node.clone() };
                q.push(new_option, distance + neighbour.distance);
            }
        }
    }
    total
}

#[cfg(test)]
mod test_solver {
    use super::*;

    lazy_static! {
        static ref DATA: String = r#"London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141"#.parse().unwrap();
    }

    #[test]
    fn test_part_1() {
        assert_eq!(605, solve_part_1(DATA.clone()));
    }

    #[test]
    fn test_part_2() {
        assert_eq!(982, solve_part_2(DATA.clone()));
    }
}
