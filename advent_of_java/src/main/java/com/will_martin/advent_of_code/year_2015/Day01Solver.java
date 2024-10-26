package com.will_martin.advent_of_code.year_2015;

import com.will_martin.advent_of_code.Solver;

public class Day01Solver implements Solver {
    @Override
    public String solvePart1(String data) {
        int sum = data.chars().map((c) -> switch (c) {
            case '(' -> 1;
            case ')' -> -1;
            default -> 0;
        }).sum();
        return String.valueOf(sum);
    }

    @Override
    public String solvePart2(String data) {
        var floor = 0;
        var counter = 1;
        for (char c : data.toCharArray()) {
            floor += switch (c) {
                case '(' -> 1;
                case ')' -> -1;
                default -> 0;
            };
            if (-1 == floor) {
                break;
            }
            counter++;
        }
        return String.valueOf(counter);
    }
}
