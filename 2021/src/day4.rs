use std::{cell::Cell, ops::Index};

pub fn part1(input: &String) -> i64 {
    let bingo_game = read_bingo(input);

    let result = bingo_game.first_winner_score();

    result as i64
}

pub fn part2(input: &String) -> i64 {
    let bingo_game = read_bingo(input);

    let result = bingo_game.last_winner_score();

    result as i64
}

// Split contents of input by double newline. First match is the list of numbers,
// remaining matches are the bingo boards.
fn read_bingo(input: &String) -> BingoGame {
    let splits: Vec<&str> = input.split("\n\n").collect();

    let numbers: Vec<i32> = splits
        .index(0)
        .split(',')
        .map(|s| s.parse::<i32>().unwrap())
        .collect();

    let mut boards = Vec::new();
    for i in 1..splits.len() {
        let number_grid: Vec<Vec<i32>> = splits
            .index(i)
            .lines()
            .map(|row| {
                row.split_whitespace()
                    .map(|col| col.parse::<i32>().unwrap())
                    .collect()
            })
            .collect();

        let height = number_grid.len();
        let width = number_grid.index(0).len();
        let marked_grid = vec![vec![Cell::new(false); width]; height];

        let board = BingoBoard {
            number_grid,
            marked_grid,
            won: Cell::new(false),
        };
        boards.push(board)
    }

    BingoGame { numbers, boards }
}

struct BingoGame {
    pub numbers: Vec<i32>,
    pub boards: Vec<BingoBoard>,
}

impl BingoGame {
    fn first_winner_score(&self) -> i32 {
        for n in &self.numbers {
            let mut winning_scores: Vec<i32> = Vec::new();

            for b in &self.boards {
                let won = b.receive_number(*n);
                if won {
                    let score = b.calculate_score(*n);
                    winning_scores.push(score);
                }
            }

            // It isn't stated in the problem, but there might be ties; find the highest score
            if winning_scores.len() > 0 {
                winning_scores.sort();
                let result = *winning_scores.last().unwrap();
                return result;
            }
        }

        // If this is returned, there was no winner (this won't happen)
        -1
    }

    fn last_winner_score(&self) -> i32 {
        let mut winning_scores: Vec<i32> = Vec::new();

        for n in &self.numbers {
            for b in &self.boards {
                if b.won.get() {
                    continue;
                }

                let won = b.receive_number(*n);
                if won {
                    let score = b.calculate_score(*n);
                    winning_scores.push(score);
                }
            }
        }

        if winning_scores.len() > 0 {
            let result = *winning_scores.last().unwrap();
            return result;
        }

        // If this is returned, there was no winner (this won't happen)
        -1
    }
}

struct BingoBoard {
    pub number_grid: Vec<Vec<i32>>,
    pub marked_grid: Vec<Vec<Cell<bool>>>,
    pub won: Cell<bool>,
}

impl BingoBoard {
    // Returns immediately on a calculated win, even if there are duplicates needing to be marked.
    // However, it doesn't seem to matter as this results in a correct answer.
    fn receive_number(&self, number: i32) -> bool {
        for y in 0..self.number_grid.len() {
            for x in 0..self.number_grid.index(y).len() {
                if *self.number_grid.index(y).index(x) == number {
                    self.marked_grid.index(y).index(x).set(true);
                    if self.check_won(x, y) {
                        self.won.set(true);
                        return true;
                    }
                }
            }
        }
        false
    }

    fn check_won(&self, x: usize, y: usize) -> bool {
        self.marked_grid.index(y).iter().all(|col| col.get())
            || self.marked_grid.iter().all(|row| row.index(x).get())
    }

    fn calculate_score(&self, winning_num: i32) -> i32 {
        let mut unmarked_total = 0;
        for y in 0..self.number_grid.len() {
            for x in 0..self.number_grid.index(y).len() {
                if !self.marked_grid.index(y).index(x).get() {
                    unmarked_total += self.number_grid.index(y).index(x);
                }
            }
        }
        return winning_num * unmarked_total;
    }
}
