const DIGITS: [&[u8]; 9] = [b"1", b"2", b"3", b"4", b"5", b"6", b"7", b"8", b"9"];
const WORDS: [&[u8]; 9] = [b"one", b"two", b"three", b"four", b"five", b"six", b"seven", b"eight", b"nine"];

pub fn solve_part_1(data: String) -> i64 {
    let result: usize = data.lines().into_iter().map(|outer_line| {
        let mut line = outer_line.as_bytes();
        let first_digit = 'outer: loop {
            for (index, digit) in DIGITS.iter().enumerate() {
                if line.starts_with(digit) {
                    break 'outer 1 + index;
                }
            }
            line = &line[1..];
        };
        let second_digit = 'outer: loop {
            for (index, digit) in DIGITS.iter().enumerate() {
                if line.ends_with(digit) {
                    break 'outer 1 + index;
                }
            }
            line = &line[..line.len() - 1];
        };
        first_digit * 10 + second_digit
    }).sum();
    result as i64
}

pub fn solve_part_2(data: String) -> i64 {
    let result: usize = data.lines().into_iter().map(|outer_line| {
        let mut line = outer_line.as_bytes();
        let first_digit = 'outer: loop {
            for (index, digit) in DIGITS.iter().enumerate() {
                if line.starts_with(digit) {
                    break 'outer 1 + index;
                }
            }
            for (index, digit) in WORDS.iter().enumerate() {
                if line.starts_with(digit) {
                    break 'outer 1 + index;
                }
            }
            line = &line[1..];
        };
        let second_digit = 'outer: loop {
            for (index, digit) in DIGITS.iter().enumerate() {
                if line.ends_with(digit) {
                    break 'outer 1 + index;
                }
            }
            for (index, digit) in WORDS.iter().enumerate() {
                if line.ends_with(digit) {
                    break 'outer 1 + index;
                }
            }
            line = &line[..line.len() - 1];
        };
        let line_result = first_digit * 10 + second_digit;
        line_result
    }).sum();
    result as i64
}

#[cfg(test)]
mod test_solver_01 {
    use super::*;
    use ctor::ctor;

    #[ctor]
    static REAL_DATA: String = {
        let filename = "../data/2023/day_01.txt";
        std::fs::read_to_string(filename).expect("Unable to read file")
    };

    #[test]
    fn test_solve_day_01_part_1() {
        let data = r#"1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"#.to_string();
        let result = solve_part_1(data);
        assert_eq!(142, result);
    }

    #[test]
    fn test_solve_day_01_part_1_real() {
        let result = solve_part_1(REAL_DATA.clone());
        assert_eq!(55386, result);
    }

    #[test]
    fn test_solve_day_01_part_2() {
        let data = r#"two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"#.to_string();
        let result = solve_part_2(data);
        assert_eq!(281, result);
    }

    #[test]
    fn test_solve_day_01_part_2_real() {
        let result = solve_part_2(REAL_DATA.clone());
        assert_eq!(54824, result);
    }
}
