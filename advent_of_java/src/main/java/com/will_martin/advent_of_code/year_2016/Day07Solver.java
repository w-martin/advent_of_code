package com.will_martin.advent_of_code.year_2016;

import com.will_martin.advent_of_code.Solver;
import lombok.Value;

import java.util.Collection;
import java.util.HashSet;
import java.util.Set;

public class Day07Solver implements Solver {
    @Override
    public String solvePart1(final String data) {
        return String.valueOf(data.trim().lines()
                .map(String::trim)
                .mapToInt(line -> supportsTls(line) ? 1 : 0)
                .sum());
    }

    private boolean supportsTls(final String line) {
        boolean hasAbba = false;
        int index = 0;
        int nextHypernetStart = line.indexOf('[');
        while (nextHypernetStart != -1) {
            if (!hasAbba) {
                hasAbba = hasAbba(line.substring(index, nextHypernetStart));
            }
            int hypernetStop = line.indexOf(']', nextHypernetStart + 1);
            if (hasAbba(line.substring(nextHypernetStart + 1, hypernetStop))) {
                return false;
            }
            index = hypernetStop + 1;
            if (index == line.length()) {
                nextHypernetStart = -1;
                index--;
            } else {
                nextHypernetStart = line.indexOf('[', index);
            }
        }
        if (!hasAbba) {
            hasAbba = hasAbba(line.substring(index));
        }
        return hasAbba;
    }

    @Value
    private static class Aba {
        char a;
        char b;
    }

    private boolean supportsSsl(final String line) {
        Set<Aba> abas = new HashSet<>();
        Set<Aba> babs = new HashSet<>();
        int index = 0;
        int nextHypernetStart = line.indexOf('[');
        while (nextHypernetStart != -1) {
            abas.addAll(getAbas(line.substring(index, nextHypernetStart), false));
            int hypernetStop = line.indexOf(']', nextHypernetStart + 1);
            babs.addAll(getAbas(line.substring(nextHypernetStart + 1, hypernetStop), true));
            index = hypernetStop + 1;
            if (index == line.length()) {
                nextHypernetStart = -1;
                index--;
            } else {
                nextHypernetStart = line.indexOf('[', index);
            }
        }
        abas.addAll(getAbas(line.substring(index), false));
        abas.retainAll(babs);
        return !abas.isEmpty();
    }

    private Set<Aba> getAbas(final String segment, boolean reverse) {
        Set<Aba> abas = new HashSet<>();
        for (int i = 0; i < segment.length() - 2; i++) {
            if (segment.charAt(i) == segment.charAt(i + 2) && segment.charAt(i + 1) != segment.charAt(i)) {
                if (reverse) {
                    abas.add(new Aba(segment.charAt(i), segment.charAt(i + 1)));
                } else {
                    abas.add(new Aba(segment.charAt(i + 1), segment.charAt(i)));
                }
            }
        }
        return abas;
    }

    private boolean hasAbba(final String segment) {
        for (int i = 0; i < segment.length() - 3; i++) {
            if ((segment.charAt(i) == segment.charAt(i + 3))
                    && segment.charAt(i + 1) == segment.charAt(i + 2)
                    && segment.charAt(i) != segment.charAt(i + 1)) return true;
        }
        return false;
    }

    @Override
    public String solvePart2(String data) {
        return String.valueOf(data.trim().lines()
                .map(String::trim)
                .mapToInt(line -> supportsSsl(line) ? 1 : 0)
                .sum());
    }
}
