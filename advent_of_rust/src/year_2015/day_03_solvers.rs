use std::collections::HashSet;

pub fn solve_part_1(data: String) -> i64 {
    let mut coordinates_visited = HashSet::new();
    let mut x = 0;
    let mut y = 0;
    coordinates_visited.insert((x, y));
    for direction in data.chars() {
        match direction {
            '^' => y += 1,
            'v' => y -= 1,
            '>' => x += 1,
            '<' => x -= 1,
            _ => {
                continue;
            }
        };
        coordinates_visited.insert((x, y));
    };
    coordinates_visited.iter().count() as i64
}

pub fn solve_part_2(data: String) -> i64 {
    let mut coordinates_visited = HashSet::new();
    let mut x1 = 0;
    let mut y1 = 0;
    let mut x2 = 0;
    let mut y2 = 0;
    let mut alternate = false;
    coordinates_visited.insert((x1, y1));
    for direction in data.chars() {
        if alternate {
            match direction {
                '^' => y1 += 1,
                'v' => y1 -= 1,
                '>' => x1 += 1,
                '<' => x1 -= 1,
                _ => {
                    continue;
                }
            };
            coordinates_visited.insert((x1, y1));
        } else {
            match direction {
                '^' => y2 += 1,
                'v' => y2 -= 1,
                '>' => x2 += 1,
                '<' => x2 -= 1,
                _ => {
                    continue;
                }
            };
            coordinates_visited.insert((x2, y2));
        }
        alternate = !alternate;
    };
    coordinates_visited.iter().count() as i64
}

#[cfg(test)]
mod test_solver {
    use super::*;

    #[test]
    fn test_part_1() {
        assert_eq!(2, solve_part_1(">".parse().unwrap()));
        assert_eq!(4, solve_part_1("^>v<".parse().unwrap()));
        assert_eq!(2, solve_part_1("^v^v^v^v^v".parse().unwrap()));
    }

    #[test]
    fn test_part_2() {
        assert_eq!(3, solve_part_2("^v".parse().unwrap()));
        assert_eq!(3, solve_part_2("^>v<".parse().unwrap()));
        assert_eq!(11, solve_part_2("^v^v^v^v^v".parse().unwrap()));
    }
}
