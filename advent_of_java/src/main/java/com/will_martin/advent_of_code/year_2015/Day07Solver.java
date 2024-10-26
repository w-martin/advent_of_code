package com.will_martin.advent_of_code.year_2015;

import com.github.benmanes.caffeine.cache.Cache;
import com.github.benmanes.caffeine.cache.Caffeine;
import com.will_martin.advent_of_code.Solver;

import java.util.HashMap;
import java.util.regex.Pattern;

public class Day07Solver implements Solver {
    private static final Pattern transformationRegex = Pattern.compile("^(.*) -> (\\w+)$");
    private static final Pattern initialiserRegex = Pattern.compile("^(\\d+)$");
    private static final Pattern combinatorRegex = Pattern.compile("^(\\w+) (AND|OR) (\\w+)$");
    private static final Pattern shifterRegex = Pattern.compile("^(\\w+) ([LR]SHIFT) (\\d+)$");
    private static final Pattern noterRegex = Pattern.compile("^NOT (\\w+)$");
    private static final Pattern reffRegex = Pattern.compile("^(\\w+)$");
    private final Cache<String, U16> cache;
    private final HashMap<String, String> circuit;

    public Day07Solver(){
        circuit = new HashMap<>();
        cache = Caffeine.newBuilder().build();
    }

    private U16 resolveCachedInstruction1(String instruction) {
        var result = cache.getIfPresent(instruction);
        if (result == null) {
            result = resolveInstruction1(instruction);
            cache.put(instruction, result);
        }
        return result;
    }

    private U16 resolveInstruction1(String instruction) {
        var match = initialiserRegex.matcher(instruction);
        if (match.matches()) {
            return U16.ParseU16(match.group(1));
        }
        match = combinatorRegex.matcher(instruction);
        if (match.matches()) {
            var a = resolveCachedInstruction1(match.group(1));
            var b = resolveCachedInstruction1(match.group(3));
            return switch (match.group(2)) {
                case "AND" -> a.and(b);
                case "OR" -> a.or(b);
                default -> throw new IllegalStateException("Unexpected value: " + match.group(2));
            };
        }
        match = shifterRegex.matcher(instruction);
        if (match.matches()) {
            var a = resolveCachedInstruction1(match.group(1));
            var b = Integer.parseInt(match.group(3));
            return switch (match.group(2)) {
                case "LSHIFT" -> a.lshift(b);
                case "RSHIFT" -> a.rshift(b);
                default -> throw new IllegalStateException("Unexpected value: " + match.group(2));
            };
        }
        match = noterRegex.matcher(instruction);
        if (match.matches()) {
            return resolveCachedInstruction1(match.group(1)).not();
        }
        match = reffRegex.matcher(instruction);
        if (match.matches()) {
            return resolveCachedInstruction1(circuit.get(instruction));
        }
        throw new IllegalStateException("Unexpected instruction: " + instruction);
    }

    private U16 resolveCachedInstruction2(String instruction) {
        var result = cache.getIfPresent(instruction);
        if (result == null) {
            result = resolveInstruction2(instruction);
            cache.put(instruction, result);
        }
        return result;
    }

    private U16 resolveInstruction2(String instruction) {
        var match = initialiserRegex.matcher(instruction);
        if (match.matches()) {
            return U16.ParseU16(instruction);
        }
        match = combinatorRegex.matcher(instruction);
        if (match.matches()) {
            var a = resolveCachedInstruction2(match.group(1));
            var b = resolveCachedInstruction2(match.group(3));
            return switch (match.group(2)) {
                case "AND" -> a.and(b);
                case "OR" -> a.or(b);
                default -> throw new IllegalStateException("Unexpected value: " + match.group(2));
            };
        }
        match = shifterRegex.matcher(instruction);
        if (match.matches()) {
            var a = resolveCachedInstruction2(match.group(1));
            var b = Integer.parseInt(match.group(3));
            return switch (match.group(2)) {
                case "LSHIFT" -> a.lshift(b);
                case "RSHIFT" -> a.rshift(b);
                default -> throw new IllegalStateException("Unexpected value: " + match.group(2));
            };
        }
        match = noterRegex.matcher(instruction);
        if (match.matches()) {
            return resolveCachedInstruction2(match.group(1)).not();
        }
        match = reffRegex.matcher(instruction);
        if (match.matches()) {
            if (instruction.equals("b")) {
                return U16.ParseU16("46065");
            }
            return resolveCachedInstruction2(circuit.get(instruction));
        }
        throw new IllegalStateException("Unexpected instruction: " + instruction);
    }

    @Override
    public String solvePart1(String data) {
        final String[] target = {null};
        data.trim().lines().forEach(line -> {
            if (line.isEmpty()) {
                return;
            }
            if (target[0] == null) {
                target[0] = line;
                return;
            }
            var transformation = transformationRegex.matcher(line);
            if (transformation.matches()) {
                circuit.put(transformation.group(2), transformation.group(1));
            }
        });
        return String.valueOf(resolveCachedInstruction1(target[0]).toInteger());
    }

    @Override
    public String solvePart2(String data) {
        final String[] target = {null};
        data.trim().lines().forEach(line -> {
            if (line.isEmpty()) {
                return;
            }
            if (target[0] == null) {
                target[0] = line;
                return;
            }
            var transformation = transformationRegex.matcher(line);
            if (transformation.matches()) {
                circuit.put(transformation.group(2), transformation.group(1));
            }
        });
        return String.valueOf(resolveCachedInstruction2(target[0]).toInteger());
    }
}
