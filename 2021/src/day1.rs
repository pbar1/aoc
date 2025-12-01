use std::ops::Index;

pub fn part1(input: &String) -> i64 {
    let nums: Vec<i32> = input
        .lines()
        .map(|line| line.parse::<i32>().unwrap())
        .collect();

    let mut result = 0;
    for i in 1..nums.len() {
        if nums.index(i) > nums.index(i - 1) {
            result += 1;
        }
    }

    result
}

pub fn part2(input: &String) -> i64 {
    let nums: Vec<i32> = input
        .lines()
        .map(|line| line.parse::<i32>().unwrap())
        .collect();

    let mut result = 0;
    for i in 3..nums.len() {
        let sum_a = nums.index(i - 3) + nums.index(i - 2) + nums.index(i - 1);
        let sum_b = nums.index(i - 2) + nums.index(i - 1) + nums.index(i);
        if sum_b > sum_a {
            result += 1;
        }
    }

    result
}
