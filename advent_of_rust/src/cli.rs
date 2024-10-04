use clap::Parser;
use clap_num::number_range;
use std::path::PathBuf;

pub mod year_2015 {
    pub mod day_01_solvers;
    pub mod day_02_solvers;
    pub mod day_03_solvers;
    pub mod day_04_solvers;
    pub mod day_05_solvers;
    pub mod day_06_solvers;
    pub mod day_07_solvers;
}
pub mod year_2023 {
    pub mod day_01_solvers;
}

fn parse_year(s: &str) -> Result<u16, String> {
    number_range(s, 2015, 2024)
}
fn parse_day(s: &str) -> Result<u8, String> {
    number_range(s, 1, 25)
}
fn parse_part(s: &str) -> Result<u8, String> {
    number_range(s, 1, 2)
}

#[derive(Parser)]
#[command(version, about, long_about = None)]
struct Cli {
    #[clap(long, value_parser=parse_year)]
    year: u16,
    #[clap(long, value_parser=parse_day)]
    day: u8,
    #[clap(long, value_parser=parse_part)]
    part: u8,
    #[clap(long)]
    data_root: PathBuf
}

fn main() {
    let args = Cli::parse();
    println!("Running day {} part {} data_root {}", args.day, args.part, args.data_root.to_string_lossy());

    let filename = args.data_root.join(args.year.to_string()).join(format!("day_{:02}.txt", args.day));
    println!("Reading file: {}", filename.to_string_lossy());
    let data = std::fs::read_to_string(filename).expect("Unable to read file");
    let mut result = -1;
    match (args.year, args.day, args.part) {
        (2015, 1, 1) => {
            result = year_2015::day_01_solvers::solve_part_1(data);
        }
        (2015, 1, 2) => {
            result = year_2015::day_01_solvers::solve_part_2(data);
        }
        (2015, 2, 1) => {
            result = year_2015::day_02_solvers::solve_part_1(data);
        }
        (2015, 2, 2) => {
            result = year_2015::day_02_solvers::solve_part_2(data);
        }
        (2015, 3, 1) => {
            result = year_2015::day_03_solvers::solve_part_1(data);
        }
        (2015, 3, 2) => {
            result = year_2015::day_03_solvers::solve_part_2(data);
        }
        (2015, 4, 1) => {
            result = year_2015::day_04_solvers::solve_part_1(data);
        }
        (2015, 4, 2) => {
            result = year_2015::day_04_solvers::solve_part_2(data);
        }
        (2015, 5, 1) => {
            result = year_2015::day_05_solvers::solve_part_1(data);
        }
        (2015, 5, 2) => {
            result = year_2015::day_05_solvers::solve_part_2(data);
        }
        (2015, 6, 1) => {
            result = year_2015::day_06_solvers::solve_part_1(data);
        }
        (2015, 6, 2) => {
            result = year_2015::day_06_solvers::solve_part_2(data);
        }
        (2015, 7, 1) => {
            result = year_2015::day_07_solvers::solve_part_1(data);
        }
        (2015, 7, 2) => {
            result = year_2015::day_07_solvers::solve_part_2(data);
        }
        (2023, 1, 1) => {
            result = year_2023::day_01_solvers::solve_part_1(data);
        }
        (2023, 1, 2) => {
            result = year_2023::day_01_solvers::solve_part_2(data);
        }
        _ => {
            println!("Day {} Part {} not implemented", args.day, args.part);
        }
    }
    println!("{}", result);
}
