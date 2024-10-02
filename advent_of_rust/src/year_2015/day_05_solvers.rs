use counter::Counter;

const VOWELS: [char; 5] = ['a', 'e', 'i', 'o', 'u'];
const DISALLOWED: [[char; 2]; 4] = [['a', 'b'], ['c', 'd'], ['p', 'q'], ['x', 'y']];
pub fn solve_part_1(data: String) -> i64 {
    data.trim().lines().map(|line| {
        let mut num_vowels = 0;
        let mut appeared_twice = false;
        let mut last_character = '1';
        for c in line.chars() {
            if VOWELS.contains(&c) {
                num_vowels += 1;
            }
            if c == last_character {
                appeared_twice = true;
            }
            for d in DISALLOWED {
                if last_character == d[0] && c == d[1] {
                    return 0i64;
                }
            }
            last_character = c;
        }
        (num_vowels >= 3 && appeared_twice) as i64
    }).sum()
}

pub fn solve_part_2(data: String) -> i64 {
    data.trim().lines().map(|line| {
        let mut last_char = '1';
        let mut second_last_char = '2';
        let mut last_pair_registered = ['1', '2'];
        let mut pair_counts: Counter<[char; 2], i8> = Counter::new();
        let mut skipped_char = false;
        for c in line.chars() {
            if c == second_last_char {
                skipped_char = true;
            }
            let new_pair = [last_char, c];
            if new_pair != last_pair_registered {
                pair_counts += [new_pair];
                last_pair_registered = new_pair;
            } else {
                last_pair_registered = ['1', '2'];
            }
            second_last_char = last_char;
            last_char = c;
        }
        (skipped_char && pair_counts.values().any(|v| v >= &2)) as i64
    }).sum()
}

#[cfg(test)]
mod test_solver {
    use super::*;

    #[test]
    fn test_part_1() {
        assert_eq!(1, solve_part_1("ugknbfddgicrmopn".parse().unwrap()));
        assert_eq!(1, solve_part_1("aaa".parse().unwrap()));
        assert_eq!(0, solve_part_1("jchzalrnumimnmhp".parse().unwrap()));
        assert_eq!(0, solve_part_1("haegwjzuvuyypxyu".parse().unwrap()));
        assert_eq!(0, solve_part_1("dvszwmarrgswjxmb".parse().unwrap()));
    }

    #[test]
    fn test_part_2() {
        assert_eq!(1, solve_part_2("qjhvhtzxzqqjkmpb".parse().unwrap()));
        assert_eq!(1, solve_part_2("xxyxx".parse().unwrap()));
        assert_eq!(0, solve_part_2("uurcxstgmygtbstg".parse().unwrap()));
        assert_eq!(0, solve_part_2("ieodomkazucvgmuy".parse().unwrap()));
    }
}
