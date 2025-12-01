use std::ops::{Deref, Index};

pub fn part1(input: &String) -> i64 {
    let commands = input.lines();

    let mut horizontal = 0;
    let mut depth = 0;

    for s in commands {
        let split: Vec<&str> = s.split(' ').collect();
        let command = split.index(0).deref();
        let unit: i32 = split.index(1).parse().unwrap();

        match command {
            "forward" => horizontal += unit,
            "down" => depth += unit,
            "up" => depth -= unit,
            _ => panic!("not a valid command"),
        }
    }

    let result = horizontal * depth;

    result as i64
}

pub fn part2(input: &String) -> i64 {
    let commands = input.lines();

    let mut horizontal = 0;
    let mut depth = 0;
    let mut aim = 0;

    for s in commands {
        let split: Vec<&str> = s.split(' ').collect();
        let command = split.index(0).deref();
        let unit: i32 = split.index(1).parse().unwrap();

        match command {
            "forward" => {
                horizontal += unit;
                depth += aim * unit;
            }
            "down" => aim += unit,
            "up" => aim -= unit,
            _ => panic!("not a valid command"),
        }
    }

    let result = horizontal * depth;

    result as i64
}
