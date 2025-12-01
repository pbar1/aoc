use std::{cell::Cell, ops::Index};

pub fn part1(input: &String) -> i64 {
    // Only horizontal and vertical vents are in scope for part 1
    let segments = parse_line_segments(input)
        .into_iter()
        .filter(|seg| seg.start.0 == seg.end.0 || seg.start.1 == seg.end.0)
        .collect();

    let result = calculate_overlaps(segments);

    result as i64
}

pub fn part2(input: &String) -> i64 {
    // Diagonals are in scope for part 2
    let segments = parse_line_segments(input);

    let result = calculate_overlaps(segments);

    result as i64
}

fn parse_line_segments(input: &String) -> Vec<LineSegment> {
    let segments: Vec<LineSegment> = input
        .lines()
        .map(|line| {
            let s: Vec<&str> = line.split(" -> ").collect();
            let start: Vec<i16> = s
                .index(0)
                .split(",")
                .map(|n| n.parse::<i16>().unwrap())
                .collect();
            let end: Vec<i16> = s
                .index(1)
                .split(",")
                .map(|n| n.parse::<i16>().unwrap())
                .collect();
            LineSegment {
                start: (*start.index(0), *start.index(1)),
                end: (*end.index(0), *end.index(1)),
            }
        })
        .collect();
    segments
}

fn calculate_overlaps(segments: Vec<LineSegment>) -> i32 {
    let mut width = 0usize;
    let mut height = 0usize;
    for seg in &segments {
        if seg.start.0 as usize > width {
            width = seg.start.0 as usize
        }
        if seg.start.1 as usize > height {
            height = seg.start.1 as usize
        }
        if seg.end.0 as usize > width {
            width = seg.end.0 as usize
        }
        if seg.end.1 as usize > height {
            height = seg.end.1 as usize
        }
    }
    width += 1;
    height += 1;

    let vents = vec![vec![Cell::new(0); width]; height];
    for seg in &segments {
        for p in seg.points_within() {
            let n = vents.index(p.1 as usize).index(p.0 as usize).get();
            vents.index(p.1 as usize).index(p.0 as usize).set(n + 1);
        }
    }

    let mut result = 0;
    for y in 0..height {
        for x in 0..width {
            if vents.index(y).index(x).get() >= 2 {
                result += 1;
            }
        }
    }
    result
}

struct LineSegment {
    pub start: (i16, i16),
    pub end: (i16, i16),
}

impl LineSegment {
    fn points_within(&self) -> Vec<(i16, i16)> {
        let mut points: Vec<(i16, i16)> = Vec::new();
        points_within_rec(&mut points, self.start, self.end);
        points
    }
}

fn points_within_rec(accum: &mut Vec<(i16, i16)>, start: (i16, i16), end: (i16, i16)) {
    accum.push(start);

    if start == end {
        return;
    }

    let mut delta_x = 0i16;
    let mut delta_y = 0i16;
    if end.0 > start.0 {
        delta_x = 1;
    } else if end.0 < start.0 {
        delta_x = -1;
    }
    if end.1 > start.1 {
        delta_y = 1;
    } else if end.1 < start.1 {
        delta_y = -1;
    }

    let new_start = (start.0 + delta_x, start.1 + delta_y);
    points_within_rec(accum, new_start, end);
}
