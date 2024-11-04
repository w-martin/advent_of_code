package com.will_martin.advent_of_code.year_2015;

import com.will_martin.advent_of_code.Solver;
import lombok.Builder;
import lombok.val;

import java.util.*;
import java.util.regex.Pattern;

public class Day19Solver implements Solver {
    @Override
    public String solvePart1(String data) {
        parseData(data);
        var uniqueMolecules = new HashSet<String>();
        for (int i = 0; i < target.length(); i++) {
            val prefix = target.substring(0, i);
            for (val key : replacements.keySet()) {
                int endIndex = Math.min(i + key.length(), target.length());
                if (key.equals(target.substring(i, endIndex))) {
                    val values = replacements.get(key);
                    val suffix = target.substring(endIndex);
                    for (val value : values) {
                        uniqueMolecules.add(prefix + value + suffix);
                    }
                }
            }
        }
        return String.valueOf(uniqueMolecules.size());
    }

    private void parseData(final String data) {
        replacements = new HashMap<>();
        for (val line : data.trim().split("\n")) {
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
    private static class Option implements Comparable<Option> {
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
        var attemptedMolecules = new HashSet<Integer>();
        var q = new PriorityQueue<Option>();
        q.add(Option.builder().molecule(target).replacements(0).build());
        int minLength = Integer.MAX_VALUE;
        while (!q.isEmpty()) {
            val o = q.poll();
            val t = o.molecule;
            if (t.length() < minLength) {
                minLength = t.length();
                System.out.println(minLength);
            }
            if (t.equals("e")) {
                return String.valueOf(o.replacements);
            }
            val newReplacements = o.replacements + 1;
            for (val k : replacements.keySet()) {
                val values = replacements.get(k);
                for (val v : values) {
                    for (val newMolecule : getReplacements(t, v, k)) {
                        val hash = newMolecule.hashCode();
                        if (attemptedMolecules.add(hash)) {
                            q.add(Option.builder().molecule(newMolecule).replacements(newReplacements).build());
                        }
                    }
                }
            }
        }
        return "-1";
    }

    private Iterable<String> getReplacements(final String t, final String k, final String v) {
        List<String> replacementMolecules = new ArrayList<>();
        for (int i = 0; i < t.length(); i++) {
            int endIndex = Math.min(i + k.length(), t.length());
            if (k.equals(t.substring(i, endIndex))) {
                val prefix = t.substring(0, i);
                val suffix = t.substring(endIndex);
                replacementMolecules.add(prefix + v + suffix);
            }
        }
        return replacementMolecules;
    }

    private Map<String, List<String>> replacements;
    private String target;
}
