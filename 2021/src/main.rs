mod day1;
mod day2;
mod day3;
mod day4;
mod day5;
mod day6;
mod day7;
mod day8;

use std::{fs, ops::Index};

use stopwatch::Stopwatch;

fn main() {
    let parts: Vec<(fn(&String) -> i64, fn(&String) -> i64)> = vec![
        (day1::part1, day1::part2),
        (day2::part1, day2::part2),
        (day3::part1, day3::part2),
        (day4::part1, day4::part2),
        (day5::part1, day5::part2),
        (day6::part1, day6::part2),
        (day7::part1, day7::part2),
        (day8::part1, day8::part2),
    ];

    println!("PART RESULT MICROS");
    for day in 0..parts.len() {
        let (part1, part2) = *parts.index(day);
        let part_vec = vec![part1, part2];

        let filename = format!("./input/day{}.txt", day + 1);
        let input = fs::read_to_string(filename).unwrap();

        for p in 0..part_vec.len() {
            let part = *part_vec.index(p);
            let sw = Stopwatch::start_new();
            let result = part(&input);
            let elapsed = sw.elapsed().as_micros();
            println!("{}-{} {} {}", day + 1, p + 1, result, elapsed);
        }
    }
}
