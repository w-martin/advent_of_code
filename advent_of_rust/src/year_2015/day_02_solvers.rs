const SEPARATOR: char = 'x';

struct Box {
    l: i32,
    w: i32,
    h: i32,
}

impl Box {
    fn surface_area(&self) -> i32 {
        self.sides().iter().sum::<i32>() * 2
    }

    fn sides(&self) -> [i32; 3] {
        [self.l * self.w, self.w * self.h, self.h * self.l]
    }

    fn smallest_side(&self) -> i32 {
        *self.sides().iter().min().unwrap()
    }

    fn volume(&self) -> i32 {
        self.l * self.w * self.h
    }

    fn smallest_perimeter(&self) -> i32 {
        let mut edges = [self.l, self.w, self.h];
        edges.sort();
        edges[0] * 2 + edges[1] * 2
    }

    fn parse_sides(line: &str) -> Box {
        let mut line = line;
        let mut divider_position = line.find(SEPARATOR).unwrap();
        let l = &line[..divider_position].parse::<i32>().unwrap();
        line = &line[divider_position + 1..];

        divider_position = line.find(SEPARATOR).unwrap();
        let w = &line[..divider_position].parse::<i32>().unwrap();
        line = &line[divider_position + 1..];

        let h = &line.parse::<i32>().unwrap();
        Box::new(*l, *w, *h)
    }

    fn new(l: i32, w: i32, h: i32) -> Box {
        Box { l, w, h }
    }
}

pub fn solve_part_1(data: String) -> i64 {
    let result: i32 = data.lines().into_iter().map(|line| {
        let b = Box::parse_sides(line);
        b.surface_area() + b.smallest_side()
    }).sum();
    result as i64
}

pub fn solve_part_2(data: String) -> i64 {
    let result: i32 = data.lines().into_iter().map(|line| {
        let b = Box::parse_sides(line);
        b.volume() + b.smallest_perimeter()
    }).sum();
    result as i64
}

#[cfg(test)]
mod test_solver {
    use super::*;

    #[test]
    fn test_part_1() {
        assert_eq!(58, solve_part_1("2x3x4".parse().unwrap()));
        assert_eq!(43, solve_part_1("1x1x10".parse().unwrap()));
    }

    #[test]
    fn test_part_2() {
        assert_eq!(34, solve_part_2("2x3x4".parse().unwrap()));
        assert_eq!(14, solve_part_2("1x1x10".parse().unwrap()));
    }
}
