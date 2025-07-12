package com.will_martin.advent_of_code.year_2016;

import com.will_martin.advent_of_code.Solver;
import lombok.Value;

import java.util.HashSet;
import java.util.regex.MatchResult;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day01Solver implements Solver {
    private static final Pattern pattern = Pattern.compile("([LR])(\\d+)");

    private enum Direction {
        NORTH,
        SOUTH,
        EAST,
        WEST
    }

    @Value
    private static class Location {
        Integer x;
        Integer y;
    }

    private Location solve(final String data, final boolean breakOnVisited) {
        HashSet<Location> visited = new HashSet<>();
        Direction direction = Direction.NORTH;
        Location position = new Location(0, 0);
        Matcher matcher = pattern.matcher(data);
        while (matcher.find()) {
            MatchResult matchResult = matcher.toMatchResult();
            direction = applyDirectionChange(matchResult, direction);
            int distance = Integer.parseInt(matchResult.group(2));
            while (distance-- > 0) {
                position = move(position, direction);
                if (breakOnVisited) {
                    if (!visited.add(position)) {
                        return position;
                    }
                }
            }
        }
        return position;
    }

    private static String getDistance(final Location position) {
        return String.valueOf(Math.abs(position.x) + Math.abs(position.y));
    }

    @Override
    public String solvePart1(String data) {
        return getDistance(solve(data, false));
    }

    private static Location move(Location location, Direction direction) {
        return switch (direction) {
            case NORTH -> new Location(location.x, location.y + 1);
            case SOUTH -> new Location(location.x, location.y - 1);
            case EAST -> new Location(location.x + 1, location.y);
            case WEST -> new Location(location.x - 1, location.y);
        };
    }

    private static Direction applyDirectionChange(MatchResult result, Direction direction) {
        switch (result.group(1)) {
            case "L":
                switch (direction) {
                    case NORTH:
                        direction = Direction.WEST;
                        break;
                    case SOUTH:
                        direction = Direction.EAST;
                        break;
                    case EAST:
                        direction = Direction.NORTH;
                        break;
                    case WEST:
                        direction = Direction.SOUTH;
                        break;
                }
                break;
            case "R":
                switch (direction) {
                    case NORTH:
                        direction = Direction.EAST;
                        break;
                    case SOUTH:
                        direction = Direction.WEST;
                        break;
                    case EAST:
                        direction = Direction.SOUTH;
                        break;
                    case WEST:
                        direction = Direction.NORTH;
                        break;
                }
                break;
        }
        return direction;
    }

    @Override
    public String solvePart2(String data) {

        return getDistance(solve(data, true));
    }
}
