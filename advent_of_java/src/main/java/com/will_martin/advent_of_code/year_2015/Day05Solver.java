package com.will_martin.advent_of_code.year_2015;

import com.will_martin.advent_of_code.Solver;
import lombok.val;
import org.apache.commons.lang3.tuple.ImmutablePair;
import org.apache.commons.lang3.tuple.Pair;

import java.util.Arrays;
import java.util.HashSet;
import java.util.List;

public class Day05Solver implements Solver {
    private static final List<Character> vowels = Arrays.asList('a', 'e', 'i', 'o', 'u');
    private static final String[] badStrings = new String[]{"ab", "cd", "pq", "xy"};

    @Override
    public String solvePart1(String data) {
        data = data.trim();
        return data.lines().map(line -> {
            val hasBadString = Arrays.stream(badStrings).anyMatch(line::contains);
            var hasCharacterMoreThanOnce = false;
            int sumVowels = 0;
            Character lastCharacter = null;
            for (Character c : line.toCharArray()) {
                if (c == lastCharacter) {
                    hasCharacterMoreThanOnce = true;
                }
                if (vowels.contains(c)) {
                    sumVowels++;
                }
                lastCharacter = c;
            }
            val hasMoreThanThreeVowels = sumVowels >= 3;
            return (!hasBadString && (hasMoreThanThreeVowels && hasCharacterMoreThanOnce)) ? 1 : 0;
        }).reduce(0, Integer::sum).toString();
    }

    @Override
    public String solvePart2(String data) {
        data = data.trim();
        return data.lines().map(line -> {
            var pairSet = new HashSet<Pair<Character, Character>>();
            var twoPair = false;
            var oneBetween = false;
            Character lastCharacter = '1';
            Character secondLastCharacter = '2';
            Pair<Character, Character> lastPairRegistered = null;
            for (Character c : line.toCharArray()) {
                boolean oneBetweenAtC = c == secondLastCharacter;
                if (oneBetweenAtC) {
                    oneBetween = true;
                }
                val pair = new ImmutablePair<>(lastCharacter, c);
                if (!(pair.equals(lastPairRegistered))) {
                    if (pairSet.contains(pair)) {
                        twoPair = true;
                    } else {
                        pairSet.add(pair);
                        lastPairRegistered = pair;
                    }
                } else {
                    lastPairRegistered = null;
                }
                secondLastCharacter = lastCharacter;
                lastCharacter = c;
            }
            return (twoPair && oneBetween) ? 1 : 0;
        }).reduce(0, Integer::sum).toString();
    }
}
