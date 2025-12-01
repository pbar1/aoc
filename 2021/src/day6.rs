pub fn part1(input: &String) -> i64 {
    let result = simulate(input, 80);

    result as i64
}

pub fn part2(input: &String) -> i64 {
    let result = simulate(input, 256);

    result as i64
}

fn simulate(input: &String, days: i32) -> u64 {
    let mut age_counts = [0u64; 9];

    input
        .trim()
        .split(',')
        .map(|s| s.trim().parse::<usize>().unwrap())
        .for_each(|age| age_counts[age] += 1);

    for _ in 0..days {
        age_counts.rotate_left(1);
        age_counts[6] += age_counts[8];
    }

    let result: u64 = age_counts.iter().sum();
    result
}
