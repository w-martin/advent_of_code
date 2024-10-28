package com.will_martin.advent_of_code.year_2015;

import com.google.common.collect.Collections2;
import com.will_martin.advent_of_code.Solver;
import lombok.val;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.regex.Pattern;

public class Day13Solver implements Solver {

    private static final Pattern REGEX = Pattern.compile("(?<a>\\w+) would (?<gainOrLoss>gain|lose) (?<gain>\\d+) happiness units by sitting next to (?<b>\\w+).");
    public static final String ME = "me";

    @Override
    public String solvePart1(String data) {
        Map<String, Map<String, Integer>> attendees = parseAttendees(data);
        Integer maxGain = findBestTable(attendees);
        return String.valueOf(maxGain);
    }

    private static Integer findBestTable(Map<String, Map<String, Integer>> attendees) {
        Integer maxGain = Integer.MIN_VALUE;
        for (List<String> table : Collections2.permutations(attendees.keySet())) {
            int gain = 0;
            for (int i = 0; i < table.size(); i++) {
                val current = table.get(i);
                val last = table.get(i > 0 ? i - 1 : table.size() - 1);
                val next = table.get(i < table.size() - 1 ? i + 1 : 0);
                Map<String, Integer> currentNeighbourGain = attendees.get(current);
                gain += currentNeighbourGain.get(last);
                gain += currentNeighbourGain.get(next);
            }
            if (gain > maxGain) {
                maxGain = gain;
            }
        }
        return maxGain;
    }

    private static Map<String, Map<String, Integer>> parseAttendees(String data) {
        Map<String, Map<String, Integer>> attendees = new HashMap<>();
        var matcher = REGEX.matcher(data);
        while (matcher.find()) {
            var a = matcher.group("a");
            var b = matcher.group("b");
            var isGain = "gain".equals(matcher.group("gainOrLoss"));
            var gain = Integer.parseInt(matcher.group("gain"));
            if (!isGain) {
                gain *= -1;
            }
            attendees.putIfAbsent(a, new HashMap<>());
            attendees.get(a).put(b, gain);
        }
        return attendees;
    }

    @Override
    public String solvePart2(String data) {
        Map<String, Map<String, Integer>> attendees = parseAttendees(data);
        HashMap<String, Integer> myGainMap = new HashMap<>();
        attendees.put(ME, myGainMap);
        for (String attendee : attendees.keySet()) {
            attendees.get(attendee).put(ME, 0);
            myGainMap.put(attendee, 0);
        }
        Integer maxGain = findBestTable(attendees);
        return String.valueOf(maxGain);
    }
}
