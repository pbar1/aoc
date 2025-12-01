use std::collections::HashMap;

use itertools::Itertools;

pub fn part1(input: &String) -> i64 {
    let result: usize = input
        .lines()
        .map(|line| {
            line.split(" | ")
                .nth(1)
                .unwrap()
                .split_whitespace()
                .map(|digit| match digit.len() {
                    2 | 4 | 3 | 7 => 1, // ie, the unique lengths of 1, 4, 7, 8
                    _ => 0,
                })
                .sum::<usize>()
        })
        .sum();

    result as i64
}

pub fn part2(input: &String) -> i64 {
    let mut result = 0;

    for line in input.lines() {
        let mut split = line.split(" | ");

        let signals: Vec<String> = split
            .next()
            .unwrap()
            .split_whitespace()
            .map(|s| s.chars().sorted().collect())
            .collect();
        let dec = CharDecoder::from(signals);

        let display: Vec<String> = split
            .next()
            .unwrap()
            .split_whitespace()
            .map(|s| s.chars().sorted().collect())
            .collect();
        let decoded = dec.translate(display);

        result += decoded;
    }

    result as i64
}

struct CharDecoder {
    map: HashMap<String, char>,
}

impl From<Vec<String>> for CharDecoder {
    fn from(signals: Vec<String>) -> Self {
        let mut map = HashMap::new();
        let mut len_fives = Vec::new();
        let mut len_sixes = Vec::new();
        let mut seven = String::from("");
        let mut four = String::from("");
        let mut eight = String::from("");
        let mut six = String::from("");
        for s in signals {
            match s.len() {
                2 => {
                    map.insert(s, '1');
                }
                3 => {
                    seven = s.clone();
                    map.insert(s, '7');
                }
                4 => {
                    four = s.clone();
                    map.insert(s, '4');
                }
                7 => {
                    eight = s.clone();
                    map.insert(s, '8');
                }
                5 => len_fives.push(s),
                6 => len_sixes.push(s),
                _ => panic!("won't happen"),
            };
        }

        let mut remaining_len_fives = Vec::new();
        for s in len_fives {
            let mut contains: Vec<bool> = Vec::new();
            for c in seven.chars() {
                contains.push(s.contains(c));
            }
            if contains.iter().all(|b| *b) {
                map.insert(s, '3');
            } else {
                remaining_len_fives.push(s);
            }
        }

        let mut remaining_len_sixes = Vec::new();
        for s in len_sixes {
            let mut contains: Vec<bool> = Vec::new();
            for c in four.chars() {
                contains.push(s.contains(c));
            }
            if contains.iter().all(|b| *b) {
                map.insert(s, '9');
            } else {
                remaining_len_sixes.push(s);
            }
        }

        for s in remaining_len_sixes {
            let mut contains: Vec<bool> = Vec::new();
            for c in seven.chars() {
                contains.push(s.contains(c));
            }
            if contains.iter().all(|b| *b) {
                map.insert(s, '0');
            } else {
                six = s.clone();
                map.insert(s, '6');
            }
        }

        // construct set of 8 - 6
        let mut eight_minus_six = Vec::new();
        for c in eight.chars() {
            if !six.contains(c) {
                eight_minus_six.push(c);
            }
        }

        for s in remaining_len_fives {
            let mut contains: Vec<bool> = Vec::new();
            for c in &eight_minus_six {
                contains.push(s.contains(*c));
            }
            if contains.iter().all(|b| *b) {
                map.insert(s, '2');
            } else {
                map.insert(s, '5');
            }
        }

        CharDecoder { map }
    }
}

impl CharDecoder {
    fn translate(&self, display: Vec<String>) -> i32 {
        let chars: Vec<char> = display
            .iter()
            .map(|s| *self.map.get(s.as_str()).unwrap())
            .collect();
        let digits: String = chars.iter().collect();
        digits.parse::<i32>().unwrap()
    }
}
