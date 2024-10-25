package com.will_martin.advent_of_code.year_2015;

import com.will_martin.advent_of_code.Solver;

public class Day10Solver implements Solver {
    @Override
    public Integer solvePart1(String data) {
        data = data.trim();
        for (int i = 0; i < 40; i++) {
            data = lookAndSay(data);
        }
        return data.length();
    }

    public String lookAndSay(final String data) {
        StringBuilder result = new StringBuilder();
        char last = 0;
        int n = 0;
        for (int i = 0; i < data.length(); i++) {
            final char c = data.charAt(i);
            if (c == last) {
                n++;
            } else {
                if (n > 0) {
                    result.append(n);
                    result.append(last);
                }
                n = 1;
                last = c;
            }
        }
        if (n > 0) {
            result.append(n);
            result.append(last);
        }
        return result.toString();
    }

    @Override
    public Integer solvePart2(String data) {
        data = data.trim();
        for (int i = 0; i < 50; i++) {
            data = lookAndSay(data);
        }
        return data.length();
    }
}
