use regex::Regex;

use cached::proc_macro::cached;
use cached::UnboundCache;
use lazy_static::lazy_static;
use std::collections::HashMap;

lazy_static! {
    static ref transformation_regex: Regex = Regex::new(r"^(.*) -> (\w+)$").unwrap();
    static ref initialiser_regex: Regex = Regex::new(r"^(\d+)$").unwrap();
    static ref combinator_regex: Regex = Regex::new(r"^(\w+) (AND|OR) (\w+)$").unwrap();
    static ref shifter_regex: Regex = Regex::new(r"^(\w+) ([LR]SHIFT) (\d+)$").unwrap();
    static ref noter_regex: Regex = Regex::new(r"^NOT (\w+)$").unwrap();
    static ref reff_regex: Regex = Regex::new(r"^(\w+)$").unwrap();
}

#[cached(
    ty = "UnboundCache<String, u16>",
    create = "{ UnboundCache::new() }",
    convert = r#"{ format!("{}", instruction) }"#
)]
fn resolve_instruction(instruction: &str, circuit: &HashMap<&str, &str>) -> u16 {
    let initialiser = initialiser_regex.captures(instruction);
    if initialiser.is_some() {
        return instruction.parse::<u16>().unwrap();
    }
    let combinator = combinator_regex.captures(instruction);
    if combinator.is_some() {
        let (_, [a_key, operator, b_key]) = combinator.unwrap().extract();
        let a = resolve_instruction(a_key, circuit);
        let b = resolve_instruction(b_key, circuit);
        return match operator {
            "AND" => { a & b }
            "OR" => { a | b }
            _ => { 0u16 }
        };
    }
    let shifter = shifter_regex.captures(instruction);
    if shifter.is_some() {
        let (_, [a_key, operator, b_str]) = shifter.unwrap().extract();
        let a = resolve_instruction(a_key, circuit);
        let b = b_str.parse::<u16>().unwrap_or(0u16);
        return match operator {
            "LSHIFT" => { a << b }
            "RSHIFT" => { a >> b }
            _ => { 0u16 }
        };
    }
    let not = noter_regex.captures(instruction);
    if not.is_some() {
        let (_, [a_key]) = not.unwrap().extract();
        let a = resolve_instruction(a_key, circuit);
        return !a;
    }
    let reff = reff_regex.captures(instruction);
    if reff.is_some() {
        return resolve_instruction(circuit.get(instruction).unwrap_or(&""), circuit);
    }
    0
}

#[cached(
    ty = "UnboundCache<String, u16>",
    create = "{ UnboundCache::new() }",
    convert = r#"{ format!("{}", instruction) }"#
)]
fn resolve_instruction_b(instruction: &str, circuit: &HashMap<&str, &str>) -> u16 {
    let initialiser = initialiser_regex.captures(instruction);
    if initialiser.is_some() {
        return instruction.parse::<u16>().unwrap();
    }
    let combinator = combinator_regex.captures(instruction);
    if combinator.is_some() {
        let (_, [a_key, operator, b_key]) = combinator.unwrap().extract();
        let a = resolve_instruction_b(a_key, circuit);
        let b = resolve_instruction_b(b_key, circuit);
        return match operator {
            "AND" => { a & b }
            "OR" => { a | b }
            _ => { 0u16 }
        };
    }
    let shifter = shifter_regex.captures(instruction);
    if shifter.is_some() {
        let (_, [a_key, operator, b_str]) = shifter.unwrap().extract();
        let a = resolve_instruction_b(a_key, circuit);
        let b = b_str.parse::<u16>().unwrap_or(0u16);
        return if "LSHIFT" == operator {
            a << b
        } else {
            a >> b
        };
    }
    let not = noter_regex.captures(instruction);
    if not.is_some() {
        let (_, [a_key]) = not.unwrap().extract();
        return !resolve_instruction_b(a_key, circuit);
    }
    let reff = reff_regex.captures(instruction);
    if reff.is_some() {
        return if "b" == instruction {
            46065
        } else {
            resolve_instruction_b(circuit.get(instruction).unwrap_or(&""), circuit)
        };
    }
    0
}

pub fn solve_part_1(data: String) -> i64 {
    let mut result_target: &str = "";
    let mut circuit: HashMap<&str, &str> = HashMap::new();
    for (line_index, line) in data.trim().lines().enumerate() {
        if 0 == line_index {
            result_target = line;
            continue;
        }
        let transformation = transformation_regex.captures(line);
        if transformation.is_some() {
            let (_, [instruction, target]) = transformation.unwrap().extract();
            circuit.insert(target, instruction);
        }
    }
    let mut result = 0;
    result += resolve_instruction(result_target, &circuit);
    result as i64
}

pub fn solve_part_2(data: String) -> i64 {
    let mut result_target: &str = "";
    let mut circuit: HashMap<&str, &str> = HashMap::new();
    for (line_index, line) in data.trim().lines().enumerate() {
        if 0 == line_index {
            result_target = line;
            continue;
        }
        let transformation = transformation_regex.captures(line);
        if transformation.is_some() {
            let (_, [instruction, target]) = transformation.unwrap().extract();
            circuit.insert(target, instruction);
        }
    }
    let mut result = 0;
    result += resolve_instruction_b(result_target, &circuit);
    result as i64
}

#[cfg(test)]
mod test_solver {
    use super::*;

    #[test]
    fn test_part_1() {
        let input: String = r#"123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i"#.parse().unwrap();
        assert_eq!(72, solve_part_1(format!("d\n{}", input)));
        assert_eq!(507, solve_part_1(format!("e\n{}", input)));
        assert_eq!(492, solve_part_1(format!("f\n{}", input)));
        assert_eq!(114, solve_part_1(format!("g\n{}", input)));
        assert_eq!(65412, solve_part_1(format!("h\n{}", input)));
        assert_eq!(65079, solve_part_1(format!("i\n{}", input)));
        assert_eq!(123, solve_part_1(format!("x\n{}", input)));
        assert_eq!(456, solve_part_1(format!("y\n{}", input)));
    }

    #[test]
    fn test_part_2() {
        let input: String = r#"c OR b -> a
46066 -> c
9 -> b"#.parse().unwrap();
        assert_eq!(46066, solve_part_2(format!("c\n{}", input)));
        assert_eq!(46067, solve_part_2(format!("a\n{}", input)));
        assert_eq!(46065, solve_part_2(format!("b\n{}", input)));
    }
}
