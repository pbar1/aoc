pub fn part1(input: &String) -> i64 {
    let positions: Vec<i32> = input
        .split(',')
        .map(|s| s.trim().parse::<i32>().unwrap())
        .collect();

    let mean = mean(&positions);

    // Smart brute force
    let mut lowest_cost = std::i32::MAX;
    for pos in (mean / 2)..(mean * 2) {
        let mut cost = 0;
        for n in &positions {
            let diff = (n - pos).abs();
            cost += diff;
        }

        if cost < lowest_cost {
            lowest_cost = cost;
        }
    }

    lowest_cost as i64
}

pub fn part2(input: &String) -> i64 {
    let positions: Vec<i32> = input
        .split(',')
        .map(|s| s.trim().parse::<i32>().unwrap())
        .collect();

    let mean = mean(&positions);

    // Smart brute force
    let mut lowest_cost = std::i32::MAX;
    for pos in (mean / 2)..(mean * 2) {
        let mut cost = 0;
        for n in &positions {
            let diff = triangular((n - pos).abs());
            cost += diff;
        }

        if cost < lowest_cost {
            lowest_cost = cost;
        }
    }

    lowest_cost as i64
}

fn triangular(n: i32) -> i32 {
    n * (n + 1) / 2
}

fn mean(numbers: &Vec<i32>) -> i32 {
    let sum: i32 = numbers.iter().sum();
    sum / numbers.len() as i32
}
