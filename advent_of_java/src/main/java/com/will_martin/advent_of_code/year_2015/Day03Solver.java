package com.will_martin.advent_of_code.year_2015;

import com.will_martin.advent_of_code.Solver;
import org.apache.commons.lang3.tuple.ImmutablePair;
import org.apache.commons.lang3.tuple.Pair;

public class Day03Solver implements Solver {


    @Override
    public String solvePart1(String data) {
        var visitedHouses = new java.util.HashSet<Pair<Integer, Integer>>();
        var x = 0;
        var y = 0;
        visitedHouses.add(new ImmutablePair<>(x, y));
        for (var c : data.toCharArray()) {
            switch (c) {
                case '^':
                    y++;
                    break;
                case 'v':
                    y--;
                    break;
                case '>':
                    x++;
                    break;
                case '<':
                    x--;
                    break;
            }
            visitedHouses.add(new ImmutablePair<>(x, y));
        }
        return String.valueOf(visitedHouses.size());
    }

    @Override
    public String solvePart2(String data) {
        var visitedHouses = new java.util.HashSet<Pair<Integer, Integer>>();
        var x1 = 0;
        var y1 = 0;
        var x2 = 0;
        var y2 = 0;
        visitedHouses.add(new ImmutablePair<>(x1, y1));
        var alternate = false;
        for (var c : data.toCharArray()) {
            if (alternate) {
                switch (c) {
                    case '^':
                        y1++;
                        break;
                    case 'v':
                        y1--;
                        break;
                    case '>':
                        x1++;
                        break;
                    case '<':
                        x1--;
                        break;
                }
                visitedHouses.add(new ImmutablePair<>(x1, y1));
            } else {
                switch (c) {
                    case '^':
                        y2++;
                        break;
                    case 'v':
                        y2--;
                        break;
                    case '>':
                        x2++;
                        break;
                    case '<':
                        x2--;
                        break;
                }
                visitedHouses.add(new ImmutablePair<>(x2, y2));
            }
            alternate = !alternate;
        }
        return String.valueOf(visitedHouses.size());
    }
}
