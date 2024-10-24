package com.will_martin.advent_of_code.year_2015;

import com.will_martin.advent_of_code.Solver;
import lombok.Builder;
import lombok.val;

import java.util.*;

public class Day09Solver implements Solver {
    @Builder
    private static class Day09Option implements Comparable<Day09Option> {
        String node;
        Set<String> visited;
        Integer distance;

        @Override
        public int compareTo(Day09Option o) {
            return distance.compareTo(o.distance);
        }
    }

    @Override
    public Integer solvePart1(String data) {
        var G = parseGraph(data);
        var Q = new PriorityQueue<Day09Option>();
        for (String node : G.keySet()) {
            Q.add(new Day09Option(node, Set.of(node), 0));
        }
        while (!Q.isEmpty()) {
            val current = Q.poll();
            if (current.visited.size() == G.size()) {
                return current.distance;
            }
            G.get(current.node).forEach((neighbor, distance) -> {
                if (!current.visited.contains(neighbor)) {
                    var newVisited = new HashSet<>(current.visited);
                    newVisited.add(neighbor);
                    Q.add(new Day09Option(neighbor, newVisited, current.distance + distance));
                }
            });
        }
        return Integer.MAX_VALUE;
    }

    private static HashMap<String, HashMap<String, Integer>> parseGraph(String data) {
        var G = new HashMap<String, HashMap<String, Integer>>();
        data.trim().lines().forEach(line -> {
            val parts = line.trim().split(" ");
            if (parts.length == 5) {
                val distance = Integer.parseInt(parts[4]);
                val a = parts[0];
                val b = parts[2];
                G.putIfAbsent(a, new HashMap<>());
                G.putIfAbsent(b, new HashMap<>());
                G.get(a).put(b, distance);
                G.get(b).put(a, distance);
            }
        });
        return G;
    }

    @Override
    public Integer solvePart2(String data) {
        var G = parseGraph(data);
        var Q = new ArrayList<Day09Option>();
        for (String node : G.keySet()) {
            Q.add(new Day09Option(node, Set.of(node), 0));
        }
        int maxDistance = Integer.MIN_VALUE;
        while (!Q.isEmpty()) {
            val current = Q.removeLast();
            if (current.visited.size() == G.size()) {
                maxDistance = Math.max(maxDistance, current.distance);
                continue;
            }
            G.get(current.node).forEach((neighbor, distance) -> {
                if (!current.visited.contains(neighbor)) {
                    var newVisited = new HashSet<>(current.visited);
                    newVisited.add(neighbor);
                    Q.add(new Day09Option(neighbor, newVisited, current.distance + distance));
                }
            });
        }
        return maxDistance;
    }
}
