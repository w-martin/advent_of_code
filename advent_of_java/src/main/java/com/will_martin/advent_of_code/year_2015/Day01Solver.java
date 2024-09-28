package com.will_martin.advent_of_code.year_2015;

import com.will_martin.advent_of_code.Solver;

public class Day01Solver implements Solver {
    @Override
    public Integer solvePart1(String data) {
        return data.chars().map((c) -> switch (c) {
            case '(' -> 1;
            case ')' -> -1;
            default -> 0;
        }).sum();
    }

    @Override
    public Integer solvePart2(String data) {
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
        return counter;
    }
}
