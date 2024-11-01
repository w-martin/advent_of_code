package com.will_martin.advent_of_code.year_2015;

import com.google.common.collect.Collections2;
import com.google.common.collect.ImmutableSet;
import com.google.common.collect.Sets;
import com.will_martin.advent_of_code.Solver;
import lombok.val;

import java.util.*;
import java.util.function.Predicate;

public class Day17Solver implements Solver {
    @Override
    public String solvePart1(String data) {
        return String.valueOf(getNumDistinctCombinationFor(150, data));
    }

    @Override
    public String solvePart2(String data) {
        return String.valueOf(getMinimumNumContainersFor(150, data));
    }

    public int getNumDistinctCombinationFor(int litres, String data) {
        Integer[] containerSizes = parseContainers(data);
        int totalNumContainers = containerSizes.length;
        Set<Integer> containerIndices = new HashSet<>(totalNumContainers);
        for (int i = 0; i <totalNumContainers; i++) {
            containerIndices.add(i);
        }
        int total = 0;
        for (int i = 1; i <= totalNumContainers; i++) {
            for (val combination : Sets.combinations(containerIndices, i)) {
                if (combination.stream().mapToInt(index -> containerSizes[index]).sum() == litres) {
                    total++;
                }
            }
        }
        return total;
    }

    private Integer[] parseContainers(String data) {
        return data.trim().lines().map(String::trim).filter(Predicate.not(String::isEmpty)).map(Integer::parseInt).toArray(Integer[]::new);
    }

    public int getMinimumNumContainersFor(int litres, String data) {
        Integer[] containerSizes = parseContainers(data);
        int totalNumContainers = containerSizes.length;
        Set<Integer> containerIndices = new HashSet<>(totalNumContainers);
        for (int i = 0; i <totalNumContainers; i++) {
            containerIndices.add(i);
        }
        int total = 0;
        for (int i = 1; i <= totalNumContainers; i++) {
            for (val combination : Sets.combinations(containerIndices, i)) {
                if (combination.stream().mapToInt(index -> containerSizes[index]).sum() == litres) {
                    total++;
                }
            }
            if (total > 0) {
                return total;
            }
        }
        return -1;
    }
}
