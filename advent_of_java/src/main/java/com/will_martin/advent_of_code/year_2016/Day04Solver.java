package com.will_martin.advent_of_code.year_2016;

import com.will_martin.advent_of_code.Solver;
import lombok.Builder;
import lombok.val;

import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day04Solver implements Solver {
    @Override
    public String solvePart1(String data) {
        val rooms = filterForValidChecksum(data);
        return String.valueOf(rooms.stream().mapToInt(r -> r.sectorId).sum());
    }

    private static final Pattern pattern = Pattern.compile("([a-z-]*)(\\d+)\\[([a-z]+)]");
    private static final String alphabet = "abcdefghijklmnopqrstuvwxyz";

    @Builder
    private static class Room {
        String encryptedName;
        Integer sectorId;
        String realName;

        public Optional<String> getRealName() {
            return Optional.ofNullable(realName);
        }
    }

    private List<Room> filterForValidChecksum(final String data) {
        List<Room> rooms = new ArrayList<>();
        for (final String line : data.trim().split("\n")) {
            Matcher matcher = pattern.matcher(line);
            if (matcher.matches()) {
                String encryptedName = matcher.group(1);
                val sectorId = Integer.parseInt(matcher.group(2));
                val checkSum = matcher.group(3);
                Map<Character, Integer> valueCounts = new HashMap<>();
                for (val c : encryptedName.replaceAll("-", "").toCharArray()) {
                    valueCounts.put(c, valueCounts.getOrDefault(c, 0) + 1);
                }
                String calculatedCheckSum = valueCounts.entrySet().stream()
                        .sorted(Map.Entry.<Character, Integer>comparingByValue().reversed()
                                .thenComparing(Map.Entry.comparingByKey()))
                        .limit(5)
                        .map(Map.Entry::getKey)
                        .collect(StringBuilder::new, StringBuilder::append, StringBuilder::append)
                        .toString();
                if (checkSum.equals(calculatedCheckSum)) {
                    rooms.add(Room.builder().sectorId(sectorId).encryptedName(encryptedName).build());
                }
            }
        }
        return rooms;
    }

    private static void computeRealName(final Room room) {
        StringBuilder realName = new StringBuilder();
        for (val c : room.encryptedName.toCharArray()) {
            if (c == '-') {
                realName.append(c);
            } else {
                realName.append(alphabet.charAt((alphabet.indexOf(c) + room.sectorId) % alphabet.length()));
            }
        }
        room.realName = realName.toString();
    }

    @Override
    public String solvePart2(String data) {
        val rooms = filterForValidChecksum(data);
        for (Room room : rooms) {
            computeRealName(room);
        }

        return String.valueOf(rooms.stream().filter(room -> room.realName.contains("north") && room.realName.contains("storage")).mapToInt(room -> room.sectorId).findFirst().orElse(-1));
    }
}
