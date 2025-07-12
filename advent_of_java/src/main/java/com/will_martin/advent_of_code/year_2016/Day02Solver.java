package com.will_martin.advent_of_code.year_2016;

import com.will_martin.advent_of_code.Solver;
import lombok.Builder;
import lombok.val;

public class Day02Solver implements Solver {
    @Builder
    private static class Position {
        int x;
        int y;
    }


    @Override
    public String solvePart1(String data) {
        final char[][] keypad = {
                {'1', '2', '3'},
                {'4', '5', '6'},
                {'7', '8', '9'}
        };
        Position position = new Position(1, 1);
        return solve(position, keypad, data);
    }

    private String solve(Position position, char[][] keypad, String data) {
        StringBuilder result = new StringBuilder();
        for (val line : data.split("\n")) {
            applyInstructions(position, line, keypad);
            result.append(keypad[position.y][position.x]);
        }
        return result.toString();
    }

    private void applyInstructions(Position position, final String line, final char[][] keypad) {
        for (val c : line.toCharArray()) {
            int newX = position.x;
            int newY = position.y;
            switch (c) {
                case 'U':
                    newY = position.y > 0 ? position.y - 1 : position.y;
                    break;
                case 'D':
                    newY = position.y < keypad.length - 1 ? position.y + 1 : position.y;
                    break;
                case 'L':
                    newX = position.x > 0 ? position.x - 1 : position.x;
                    break;
                case 'R':
                    newX = position.x < keypad[0].length - 1 ? position.x + 1 : position.x;
                    break;
            }
            if ('x' != keypad[newY][newX]) {
                position.x = newX;
                position.y = newY;
            }
        }
    }

    @Override
    public String solvePart2(String data) {
        final char[][] keypad = {
                {'x', 'x', '1', 'x', 'x'},
                {'x', '2', '3', '4', 'x'},
                {'5', '6', '7', '8', '9'},
                {'x', 'A', 'B', 'C', 'x'},
                {'x', 'x', 'D', 'x', 'x'},
        };
        Position position = new Position(0, 2);
        return solve(position, keypad, data);
    }
}
