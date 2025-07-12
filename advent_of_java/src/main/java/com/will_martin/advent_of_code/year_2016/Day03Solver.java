package com.will_martin.advent_of_code.year_2016;

import com.will_martin.advent_of_code.Solver;
import lombok.val;

import java.util.Arrays;

public class Day03Solver implements Solver {
    @Override
    public String solvePart1(String data) {
        return solve(data, true);
    }

    private static String solve(final String data, final boolean horizontal) {
        int sum = 0;
        final int[][] inputGrid = Arrays.stream(data.trim().split("\n"))
                .map(line -> Arrays.stream(line.trim().split("\\s+"))
                        .mapToInt(Integer::parseInt)
                        .toArray())
                .toArray(int[][]::new);
        if (horizontal) {
            for (val sides : inputGrid) {
                if (isTriangle(sides)) {
                    sum++;
                }
            }
        } else {
            int[] sides = new int[3];
            for (int columnId = 0; columnId < inputGrid[0].length; columnId++) {
                for (int rowId = 0; rowId < inputGrid.length; rowId += 3) {
                    sides[0] = inputGrid[rowId][columnId];
                    sides[1] = inputGrid[rowId + 1][columnId];
                    sides[2] = inputGrid[rowId + 2][columnId];
                    if (isTriangle(sides)) {
                        sum++;
                    }
                }
            }
        }
        return String.valueOf(sum);
    }

    private static boolean isTriangle(int[] sides) {
        return (sides.length == 3) &&
                (sides[0] + sides[1] > sides[2]) &&
                (sides[0] + sides[2] > sides[1])
                && (sides[1] + sides[2] > sides[0]);
    }

    @Override
    public String solvePart2(String data) {
        return solve(data, false);
    }
}
