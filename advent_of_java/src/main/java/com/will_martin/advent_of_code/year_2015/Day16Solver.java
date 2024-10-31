package com.will_martin.advent_of_code.year_2015;

import com.will_martin.advent_of_code.Solver;
import lombok.val;

import java.util.HashMap;
import java.util.Map;
import java.util.Set;
import java.util.regex.Pattern;

public class Day16Solver implements Solver {
    private static final Pattern suePattern = Pattern.compile("Sue (?<number>\\d+): (?<entities>.*)");
    private static final Pattern entityPattern = Pattern.compile("(?<key>\\w+): (?<value>\\d+)(, )?");
    private final Map<String, Integer> facts;
    private final Set<String> moreThanKeys = Set.of("cats", "trees");
    private final Set<String> fewerThanKeys = Set.of("pomeranians", "goldfish");

    public Day16Solver() {
        facts = new HashMap<>(10);
        facts.put("children", 3);
        facts.put("cats", 7);
        facts.put("samoyeds", 2);
        facts.put("pomeranians", 3);
        facts.put("akitas", 0);
        facts.put("vizslas", 0);
        facts.put("goldfish", 5);
        facts.put("trees", 3);
        facts.put("cars", 2);
        facts.put("perfumes", 1);
    }

    @Override
    public String solvePart1(String data) {
        var match = suePattern.matcher(data);
        while (match.find()) {
            val sueNumber = match.group("number");
            boolean thisMightBeSue = true;
            var entityMatcher = entityPattern.matcher(match.group("entities"));
            while (thisMightBeSue && entityMatcher.find()) {
                String key = entityMatcher.group("key");
                String value = entityMatcher.group("value");
                Integer expected = facts.get(key);
                Integer actual = Integer.parseInt(value);
                if (!expected.equals(actual)) {
                    thisMightBeSue = false;
                }
            }
            if (thisMightBeSue) {
                return sueNumber;
            }
        }
        return "-1";
    }

    @Override
    public String solvePart2(String data) {
        var match = suePattern.matcher(data);
        while (match.find()) {
            val sueNumber = match.group("number");
            boolean thisMightBeSue = true;
            var entityMatcher = entityPattern.matcher(match.group("entities"));
            while (thisMightBeSue && entityMatcher.find()) {
                String key = entityMatcher.group("key");
                String value = entityMatcher.group("value");
                Integer expected = facts.get(key);
                Integer actual = Integer.parseInt(value);
                if (moreThanKeys.contains(key)) {
                    thisMightBeSue = expected < actual;
                } else if (fewerThanKeys.contains(key)) {
                    thisMightBeSue = expected > actual;
                } else {
                    thisMightBeSue = expected.equals(actual);
                }
            }
            if (thisMightBeSue) {
                return sueNumber;
            }
        }
        return "-1";
    }
}
