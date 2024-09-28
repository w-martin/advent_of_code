pub fn solve_part_1(data: String) -> i64 {
    data.chars().into_iter().map(|c| {
        match c {
            '(' => { 1 }
            ')' => { -1 }
            _ => { 0 }
        }
    }).sum()
}

pub fn solve_part_2(data: String) -> i64 {
    let mut sum = 0;
    let mut position = 0;
    for c in data.chars() {
        position += 1;
        sum += match c {
            '(' => { 1 }
            ')' => { -1 }
            _ => { 0 }
        };
        if sum < 0 {
            break;
        }
    }
    position
}

#[cfg(test)]
mod test_solver {
    use super::*;

    #[test]
    fn test_part_1() {
        assert_eq!(0, solve_part_1("(())".parse().unwrap()));
        assert_eq!(0, solve_part_1("()()".parse().unwrap()));
        assert_eq!(3, solve_part_1("(((".parse().unwrap()));
        assert_eq!(3, solve_part_1("(()(()(".parse().unwrap()));
        assert_eq!(3, solve_part_1("))(((((".parse().unwrap()));
        assert_eq!(-1, solve_part_1("())".parse().unwrap()));
        assert_eq!(-1, solve_part_1("))(".parse().unwrap()));
        assert_eq!(-3, solve_part_1(")))".parse().unwrap()));
        assert_eq!(-3, solve_part_1(")())())".parse().unwrap()));
    }

    #[test]
    fn test_part_2() {
        assert_eq!(1, solve_part_2(")".parse().unwrap()));
        assert_eq!(5, solve_part_2("()())".parse().unwrap()));
    }
}
