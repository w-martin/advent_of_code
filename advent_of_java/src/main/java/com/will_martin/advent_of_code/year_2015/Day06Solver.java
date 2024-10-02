package com.will_martin.advent_of_code.year_2015;

import com.will_martin.advent_of_code.Solver;
import lombok.val;

import java.util.Arrays;
import java.util.regex.Pattern;
import java.util.stream.IntStream;

public class Day06Solver implements Solver {

    private static final Pattern pattern = Pattern.compile("(turn on|turn off|toggle) (\\d+),(\\d+) through (\\d+),(\\d+)");


    @Override
    public Integer solvePart1(String data) {
        data = data.trim();
        int height = 1_000;
        int width = 1_000;
        var array = new int[height * width];
        Arrays.fill(array, 0);
        data.lines().forEach(line -> {
            var matcher = pattern.matcher(line);
            if (matcher.find()) {
                val x0 = Integer.parseInt(matcher.group(2));
                val x1 = Integer.parseInt(matcher.group(4));
                val y0 = Integer.parseInt(matcher.group(3));
                val y1 = Integer.parseInt(matcher.group(5));
                switch (matcher.group(1)) {
                    case "turn on" -> {
                        for (int x = x0; x <= x1; x++) {
                            for (int y = y0; y <= y1; y++) {
                                array[y * width + x] = 1;
                            }
                        }
                    }
                    case "turn off" -> {
                        for (int x = x0; x <= x1; x++) {
                            for (int y = y0; y <= y1; y++) {
                                array[y * width + x] = 0;
                            }
                        }
                    }
                    case "toggle" -> {
                        for (int x = x0; x <= x1; x++) {
                            for (int y = y0; y <= y1; y++) {
                                array[y * width + x] = 1 - array[y * width + x];
                            }
                        }
                    }
                    default -> {
                    }
                }
            }
        });
        return IntStream.of(array).parallel().sum();
    }

    @Override
    public Integer solvePart2(String data) {
        data = data.trim();
        int height = 1_000;
        int width = 1_000;
        var array = new int[height * width];
        Arrays.fill(array, 0);
        data.lines().forEach(line -> {
            var matcher = pattern.matcher(line);
            if (matcher.find()) {
                val x0 = Integer.parseInt(matcher.group(2));
                val x1 = Integer.parseInt(matcher.group(4));
                val y0 = Integer.parseInt(matcher.group(3));
                val y1 = Integer.parseInt(matcher.group(5));
                switch (matcher.group(1)) {
                    case "turn on" -> {
                        for (int x = x0; x <= x1; x++) {
                            for (int y = y0; y <= y1; y++) {
                                array[y * width + x] += 1;
                            }
                        }
                    }
                    case "turn off" -> {
                        for (int x = x0; x <= x1; x++) {
                            for (int y = y0; y <= y1; y++) {
                                array[y * width + x] = Math.max(0, array[y * width + x] - 1);
                            }
                        }
                    }
                    case "toggle" -> {
                        for (int x = x0; x <= x1; x++) {
                            for (int y = y0; y <= y1; y++) {
                                array[y * width + x] += 2;
                            }
                        }
                    }
                    default -> {
                    }
                }
            }
        });
        return IntStream.of(array).parallel().sum();
    }
}
