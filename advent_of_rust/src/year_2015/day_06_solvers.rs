use regex::Regex;

const WIDTH: usize = 1_000;
const HEIGHT: usize = 1_000;
const SIZE: usize = (WIDTH * HEIGHT) as usize;

pub fn solve_part_1(data: String) -> i64 {
    let regex = Regex::new("(turn on|turn off|toggle) (\\d+),(\\d+) through (\\d+),(\\d+)").unwrap();
    let mut array: [u8; SIZE] = [0u8; SIZE];
    for (_, [instruction, x0_str, y0_str, x1_str, y1_str]) in regex.captures_iter(data.as_str()).map(|c| c.extract()) {
        let x0 = x0_str.parse::<usize>().unwrap();
        let x1 = x1_str.parse::<usize>().unwrap();
        let y0 = y0_str.parse::<usize>().unwrap();
        let y1 = y1_str.parse::<usize>().unwrap();
        match instruction {
            "turn on" => {
                for i in x0..x1 + 1 {
                    for j in y0..y1 + 1 {
                        array[i + j * WIDTH] = 1u8;
                    }
                }
            },
            "turn off" => {
                for i in x0..x1 + 1 {
                    for j in y0..y1 + 1 {
                        array[i + j * WIDTH] = 0u8;
                    }
                }
            },
            "toggle" => {
                for i in x0..x1 + 1 {
                    for j in y0..y1 + 1 {
                        let element = i + j * WIDTH;
                        array[element] = 1u8 - array[element];
                    }
                }
            },
            _ => {},
        }
    }
    array.iter().fold(0, |a, &b| a + b as i64)
}

pub fn solve_part_2(data: String) -> i64 {
    let regex = Regex::new("(turn on|turn off|toggle) (\\d+),(\\d+) through (\\d+),(\\d+)").unwrap();
    let mut array: [u8; SIZE] = [0u8; SIZE];
    for (_, [instruction, x0_str, y0_str, x1_str, y1_str]) in regex.captures_iter(data.as_str()).map(|c| c.extract()) {
        let x0 = x0_str.parse::<usize>().unwrap();
        let x1 = x1_str.parse::<usize>().unwrap();
        let y0 = y0_str.parse::<usize>().unwrap();
        let y1 = y1_str.parse::<usize>().unwrap();
        match instruction {
            "turn on" => {
                for i in x0..x1 + 1 {
                    for j in y0..y1 + 1 {
                        array[i + j * WIDTH] += 1u8;
                    }
                }
            },
            "turn off" => {
                for i in x0..x1 + 1 {
                    for j in y0..y1 + 1 {
                        let current = array[i + j * WIDTH];
                        if current > 0 {
                            array[i + j * WIDTH] = current - 1u8;
                        }
                    }
                }
            },
            "toggle" => {
                for i in x0..x1 + 1 {
                    for j in y0..y1 + 1 {
                        array[i + j * WIDTH] += 2u8;
                    }
                }
            },
            _ => {},
        }
    }
    array.iter().fold(0, |a, &b| a + b as i64)
}

#[cfg(test)]
mod test_solver {
    use super::*;

    #[test]
    fn test_part_1() {
        assert_eq!(1_000_000, solve_part_1("turn on 0,0 through 999,999".parse().unwrap()));
        assert_eq!(1_000, solve_part_1("toggle 0,0 through 999,0".parse().unwrap()));
        assert_eq!(0, solve_part_1("turn off 499,499 through 500,500".parse().unwrap()));
    }

    #[test]
    fn test_part_2() {
        assert_eq!(1, solve_part_2("turn on 0,0 through 0,0".parse().unwrap()));
        assert_eq!(2000000, solve_part_2("toggle 0,0 through 999,999".parse().unwrap()));
    }
}
