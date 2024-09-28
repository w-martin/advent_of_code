use clap::Parser;
use clap_num::number_range;

pub mod year_2015 {
    pub mod day_01_solvers;
    pub mod day_02_solvers;
    pub mod day_03_solvers;
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
    #[clap(short, value_parser=parse_year)]
    year: u16,
    #[clap(short, value_parser=parse_day)]
    day: u8,
    #[clap(short, value_parser=parse_part)]
    part: u8,
}

fn main() {
    let cli = Cli::parse();
    let year = cli.year;
    let day = cli.day;
    let part = cli.part;

    println!("Running day {} part {}", day, part);

    let filename = format!("../data/{}/day_{:02}.txt", year, day);
    let data = std::fs::read_to_string(filename).expect("Unable to read file");
    let mut result = -1;
    match (year, day, part) {
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
        (2023, 1, 1) => {
            result = year_2023::day_01_solvers::solve_part_1(data);
        }
        (2023, 1, 2) => {
            result = year_2023::day_01_solvers::solve_part_2(data);
        }
        _ => {
            println!("Day {} Part {} not implemented", day, part);
        }
    }
    println!("{}", result);
}
