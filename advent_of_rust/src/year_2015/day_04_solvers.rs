use crypto::digest::Digest;
use crypto::md5::Md5;

pub fn solve_part_1(data: String) -> i64 {
    let mut hasher = Md5::new();
    let prefix = data.trim().as_bytes();
    for counter in 0..u64::MAX {
        hasher.input(prefix);
        hasher.input(counter.to_string().as_bytes());
        let mut output = [0; 16];
        hasher.result(&mut output);
        if output[..2] == [0, 0] && output[2] <= 0x0F {
            return counter as i64;
        }
        hasher.reset();
    }
    -1
}

pub fn solve_part_2(data: String) -> i64 {
    let mut hasher = Md5::new();
    let prefix = data.trim().as_bytes();
    for counter in 0..u64::MAX {
        hasher.input(prefix);
        hasher.input(counter.to_string().as_bytes());
        let mut output = [0; 16];
        hasher.result(&mut output);
        if output[..3] == [0, 0, 0] {
            return counter as i64;
        }
        hasher.reset();
    }
    -1
}

#[cfg(test)]
mod test_solver {
    use super::*;

    #[test]
    fn test_part_1() {
        assert_eq!(609043, solve_part_1("abcdef".parse().unwrap()));
        assert_eq!(1048970, solve_part_1("pqrstuv".parse().unwrap()));
    }
}
