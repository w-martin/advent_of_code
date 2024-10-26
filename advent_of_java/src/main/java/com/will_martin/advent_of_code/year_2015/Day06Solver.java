package com.will_martin.advent_of_code.year_2015;

import com.will_martin.advent_of_code.Solver;
import lombok.val;

import java.util.regex.Pattern;

public class Day06Solver implements Solver {

    private static final Pattern pattern = Pattern.compile("(turn on|turn off|toggle) (\\d+),(\\d+) through (\\d+),(\\d+)");


    @Override
    public String solvePart1(String data) {
        data = data.trim();
        int height = 1_000;
        int width = 1_000;
        int size = width * height;
        var array = makeZeroedArray(size);
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
                                array[y * width + x] = (byte) ((byte) 1 - array[y * width + x]);
                            }
                        }
                    }
                    default -> {
                    }
                }
            }
        });
        return String.valueOf(sumArray(array, size));
    }

    @Override
    public String solvePart2(String data) {
        data = data.trim();
        int height = 1_000;
        int width = 1_000;
        int totalSize = width * height;
        var array = makeZeroedArray(totalSize);
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
                                array[y * width + x] = (byte) (Math.max(array[y * width + x] - 1, 0));
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
        return String.valueOf(sumArray(array, totalSize));
    }

    private static int sumArray(byte[] array, int size) {
        var sum = 0;
        for (int i = 0; i < size; i++) {
            sum += array[i];
        }
        return sum;
    }

    private static byte[] makeZeroedArray(int totalSize) {
        var array = new byte[totalSize];
        for (int i = 0; i < totalSize; i++) {
            array[i] = 0;
        }
        return array;
    }
}
