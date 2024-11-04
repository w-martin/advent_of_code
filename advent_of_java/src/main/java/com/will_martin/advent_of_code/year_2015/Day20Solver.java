package com.will_martin.advent_of_code.year_2015;

import com.will_martin.advent_of_code.Solver;
import lombok.val;

public class Day20Solver implements Solver {
    @Override
    public String solvePart1(String data) {
        val target = Integer.parseInt(data.trim());
        val maxHouses = Math.max(10_000, target /10);
        int[] houses = new int[maxHouses];
        for (int i = 1; i <= maxHouses; i++) {
            val numPresents = i * 10;
            for (int j = i; j <= maxHouses; j += i) {
                houses[j - 1] += numPresents;
            }
        }
        for (int i = 0; i < maxHouses; i++) {
            if (target <= houses[i]) {
                return String.valueOf(i + 1);
            }
        }
        return "-1";
    }

    @Override
    public String solvePart2(String data) {
        val target = Integer.parseInt(data.trim());
        val maxHouses = Math.max(10_000, target /10);
        int[] houses = new int[maxHouses];
        for (int i = 1; i <= maxHouses; i++) {
            val numPresents = i * 11;
            for (int j = i; j <= Math.min(maxHouses, i * 50); j += i) {
                houses[j - 1] += numPresents;
            }
        }
        for (int i = 0; i < maxHouses; i++) {
            if (target <= houses[i]) {
                return String.valueOf(i + 1);
            }
        }
        return "-1";
    }
}
