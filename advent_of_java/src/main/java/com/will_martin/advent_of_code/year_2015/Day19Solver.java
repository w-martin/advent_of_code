package com.will_martin.advent_of_code.year_2015;

import com.will_martin.advent_of_code.Solver;
import lombok.Builder;
import lombok.val;

import java.util.*;

public class Day19Solver implements Solver {
    @Override
    public String solvePart1(String data) {
        parseData(data);
        var uniqueMolecules = new HashSet<String>();
        for (int i = 0; i < target.length(); i++) {
            val prefix = target.substring(0, i);
            for (val key: replacements.keySet()) {
                int endIndex = Math.min(i + key.length(), target.length());
                if (key.equals(target.substring(i, endIndex))) {
                    val values = replacements.get(key);
                    val suffix = target.substring(endIndex);
                    for (val value: values) {
                        uniqueMolecules.add(prefix + value + suffix);
                    }
                }
            }
        }
        return String.valueOf(uniqueMolecules.size());
    }

    private void parseData(final String data) {
        replacements = new HashMap<>();
        for(val line: data.trim().split("\n")) {
            if (line.isEmpty()) {
                continue;
            }
            val parts = line.split(" => ");
            if (parts.length == 1) {
                target = parts[0];
            } else {
                replacements.putIfAbsent(parts[0], new ArrayList<>());
                replacements.get(parts[0]).add(parts[1]);
            }
        }
    }
    @Builder
    private static class Option  implements Comparable<Option> {
        String molecule;
        Integer replacements;

        @Override
        public int compareTo(Option o) {
            return replacements.compareTo(o.replacements);
        }
    }

    @Override
    public String solvePart2(String data) {
        parseData(data);
        var q = new PriorityQueue<Option>();
        q.add(Option.builder().molecule(target).replacements(0).build());
        while (!q.isEmpty()) {
            val o = q.poll();
            val t = o.molecule;
            if (t.equals("e")) {
                return String.valueOf(o.replacements);
            }
            val newReplacements = o.replacements + 1;
            for (int i = 0; i < t.length(); i++) {
                val prefix = t.substring(0, i);
                for (val key: replacements.keySet()) {
                    val values = replacements.get(key);
                    for (val v : values) {
                        int endIndex = Math.min(i + v.length(), t.length());
                        if (v.equals(t.substring(i, endIndex))) {
                            val suffix = t.substring(endIndex);
                            q.add(Option.builder().molecule(prefix + key + suffix).replacements(newReplacements).build());
                        }
                    }
                }
            }
        }
        return "-1";
    }

    private Map<String, List<String>> replacements;
    private String target;
}
