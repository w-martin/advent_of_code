package com.will_martin.advent_of_code.year_2015;

import com.will_martin.advent_of_code.Solver;
import lombok.Builder;
import lombok.val;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day14Solver implements Solver {

    private static final Pattern reindeerRegex = Pattern.compile("(?<name>\\w+) can fly (?<speed>\\d+) km/s for (?<flightTime>\\d+) seconds, but then must rest for (?<restTime>\\d+) seconds.");

    @Builder
    private static class Reindeer {
        String name;
        int speed;
        int flightTime;
        int restTime;
        @Builder.Default
        int actionUntil = 0;
        @Builder.Default
        boolean flying = true;
    }

    @Override
    public String solvePart1(String data) {
        return String.valueOf(distanceAfter(2503, data));
    }

    public Integer distanceAfter(int time, String data) {
        List<Reindeer> reindeerList = parseReindeer(data);
        var distances = new int[reindeerList.size()];
        for (int i = 0; i < reindeerList.size(); i++) {
            val reindeer = reindeerList.get(i);
            int iterationTime = reindeer.flightTime + reindeer.restTime;
            int iterationDistance = reindeer.flightTime * reindeer.speed;
            int fullIterations = time / iterationTime;
            int remainderTime = time - (fullIterations * iterationTime);
            int remainderDistance = Math.min(remainderTime, reindeer.flightTime) * reindeer.speed;
            distances[i] = fullIterations * iterationDistance + remainderDistance;
        }
        return Arrays.stream(distances).max().orElse(-1);
    }

    private List<Reindeer> parseReindeer(String data) {
        Matcher matcher = reindeerRegex.matcher(data);
        var result = new ArrayList<Reindeer>();
        while (matcher.find()) {
            result.add(
                    Reindeer.builder()
                            .name("name")
                            .speed(Integer.parseInt(matcher.group("speed")))
                            .flightTime(Integer.parseInt(matcher.group("flightTime")))
                            .restTime(Integer.parseInt(matcher.group("restTime")))
                            .build()
            );
        }
        return result;
    }

    public Integer pointsAfter(int time, String data) {
        List<Reindeer> reindeerList = parseReindeer(data);
        var distances = new int[reindeerList.size()];
        var points = new int[reindeerList.size()];
        for (var reindeer : reindeerList) {
            reindeer.actionUntil = reindeer.flightTime;
        }
        for (int t = 0; t < time; t++) {
            for (int i = 0; i < reindeerList.size(); i++) {
                val reindeer = reindeerList.get(i);
                if (reindeer.actionUntil == t) {
                    reindeer.flying = !reindeer.flying;
                    reindeer.actionUntil += reindeer.flying ? reindeer.flightTime : reindeer.restTime;
                }
                if (reindeer.flying) {
                    distances[i] += reindeer.speed;
                }
            }
            for (val argmax : argmaxes(distances)) {
                points[argmax]++;
            }
        }
        return max(points);
    }

    private static List<Integer> argmaxes(int[] array) {
        int max = max(array);
        List<Integer> argmaxes = new ArrayList<>();
        for (int i = 0; i < array.length; i++) {
            if (array[i] == max) {
                argmaxes.add(i);
            }
        }
        return argmaxes;
    }

    private static int max(int[] array) {
        Integer max = null;
        for (int i = 0; i < array.length; i++) {
            var t = array[i];
            if (max == null || t > max) {
                max = t;
            }
        }
        return max;
    }

    @Override
    public String solvePart2(String data) {
        return String.valueOf(pointsAfter(2503, data));
    }
}
