use lazy_static::lazy_static;
use regex::Regex;

lazy_static! {
    static ref special_character_regex1: Regex = Regex::new("(\\\\x.{2}|\\\\.)").unwrap();
    static ref special_character_regex2: Regex = Regex::new("(\"|\\\\)").unwrap();
}

pub fn solve_part_1(data: String) -> i64 {
    data.trim().lines().map(|mut line| {
        line = line.trim();
        let starting_length = line.len();
        line = &line[1..starting_length - 1];
        let num_characters = special_character_regex1.replace_all(line, "1").len();
        let result = starting_length - num_characters;
        result as i64
    }).sum()
}

pub fn solve_part_2(data: String) -> i64 {
    data.trim().lines().map(|mut line| {
        line = line.trim();
        let starting_length = line.len();
        let num_characters = 2 + special_character_regex2.replace_all(line, "12").len();
        let result = num_characters - starting_length;
        result as i64
    }).sum()
}

#[cfg(test)]
mod test_solver {
    use super::*;

    #[test]
    fn test_part_1() {
        assert_eq!(12, solve_part_1(r#"
""
"abc"
"aaa\"aaa"
"\x27"
        "#.parse().unwrap()));
    }

    #[test]
    fn test_part_2() {
        assert_eq!(19, solve_part_2(r#"
""
"abc"
"aaa\"aaa"
"\x27"
        "#.parse().unwrap()));
    }
}
