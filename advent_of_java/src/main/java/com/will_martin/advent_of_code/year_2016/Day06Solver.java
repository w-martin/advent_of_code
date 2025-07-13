package com.will_martin.advent_of_code.year_2016;

import com.will_martin.advent_of_code.Solver;
import lombok.val;

import java.util.HashMap;
import java.util.Map;

public class Day06Solver implements Solver {
    @Override
    public String solvePart1(String data) {
        char[][] characterArray = data.trim().lines()
                .map(String::trim)
                .map(String::toCharArray)
                .toArray(char[][]::new);
        StringBuilder result = new StringBuilder();
        for (int column = 0; column < characterArray[0].length; column++) {
            Map<Character, Integer> valueCounts =  new HashMap<>();
            for (val row : characterArray) {
                char character = row[column];
                valueCounts.put(character, valueCounts.getOrDefault(character, 0) + 1);
            }
            result.append(valueCounts.entrySet().stream()
                    .max(Map.Entry.comparingByValue())
                    .map(Map.Entry::getKey)
                    .orElseThrow());
        }
        return result.toString();
    }

    @Override
    public String solvePart2(String data) {
        char[][] characterArray = data.trim().lines()
                .map(String::trim)
                .map(String::toCharArray)
                .toArray(char[][]::new);
        StringBuilder result = new StringBuilder();
        for (int column = 0; column < characterArray[0].length; column++) {
            Map<Character, Integer> valueCounts =  new HashMap<>();
            for (val row : characterArray) {
                char character = row[column];
                valueCounts.put(character, valueCounts.getOrDefault(character, 0) + 1);
            }
            result.append(valueCounts.entrySet().stream()
                    .min(Map.Entry.comparingByValue())
                    .map(Map.Entry::getKey)
                    .orElseThrow());
        }
        return result.toString();
    }
}
