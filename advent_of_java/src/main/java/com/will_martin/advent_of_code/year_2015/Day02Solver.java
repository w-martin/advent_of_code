package com.will_martin.advent_of_code.year_2015;

import com.will_martin.advent_of_code.Solver;
import lombok.Value;
import lombok.val;

import java.util.Optional;
import java.util.stream.IntStream;

public class Day02Solver implements Solver {

    @Value
    private class Box {
        Integer l;
        Integer w;
        Integer h;
    }

    @Override
    public Integer solvePart1(String data) {
        return data.lines().map(line -> {
            var box = parseBox(line);
            if (box.isEmpty()) {
                return 0;
            }
            val sides = new int[]{
                    box.get().getH() * box.get().getW(),
                    box.get().getH() * box.get().getL(),
                    box.get().getL() * box.get().getW(),
            };
            return 2 * IntStream.of(sides).sum() + IntStream.of(sides).min().orElse(0);
        }).reduce(0, Integer::sum);
    }

    private Optional<Box> parseBox(String line) {
        var firstDivider = line.indexOf('x');
        if (-1 == firstDivider) {
            return Optional.empty();
        }
        int offset = firstDivider + 1;
        var secondDivider = line.indexOf('x', offset);
        if (-1 == secondDivider) {
            return Optional.empty();
        }
        val l = Integer.parseInt(line, 0, firstDivider, 10);
        val w = Integer.parseInt(line, firstDivider + 1, secondDivider, 10);
        val h = Integer.parseInt(line, 1 + secondDivider, line.length(), 10);
        return Optional.of(new Box(l, w, h));
    }

    @Override
    public Integer solvePart2(String data) {
        return data.lines().map(line -> {
            var box = parseBox(line);
            if (box.isEmpty()) {
                return 0;
            }
            var edges = new int[]{
                    box.get().getH() + box.get().getW(),
                    box.get().getH() + box.get().getL(),
                    box.get().getL() + box.get().getW(),
            };
            val smallestPerimeter = IntStream.of(edges).sorted().limit(1).sum() * 2;
            val volume = box.get().getH() * box.get().getW() * box.get().getL();
            return smallestPerimeter + volume;
        }).reduce(0, Integer::sum);
    }
}
