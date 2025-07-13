package com.will_martin.advent_of_code.year_2016;

import com.will_martin.advent_of_code.Solver;
import lombok.SneakyThrows;
import lombok.val;
import org.apache.commons.codec.binary.Hex;

import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;

public class Day05Solver implements Solver {
    @SneakyThrows
    @Override
    public String solvePart1(String data) {
        MessageDigest md = MessageDigest.getInstance("MD5");
        StringBuilder result = new StringBuilder();
        data = data.trim();
        int index = 0;
        while (result.length() < 8) {
            byte[] input = (data + index).getBytes(StandardCharsets.UTF_8);
            byte[] digest = md.digest(input);
            String hexString = Hex.encodeHexString(digest);
            if (hexString.startsWith("00000")) {
                result.append(hexString.charAt(5));
            }
            index++;
        }
        return result.toString();
    }

    @SneakyThrows
    @Override
    public String solvePart2(String data) {
        MessageDigest md = MessageDigest.getInstance("MD5");
        Map<Integer, Character> resultMap = new HashMap<>();
        data = data.trim();
        int index = 0;
        while (resultMap.size() < 8) {
            byte[] input = (data + index).getBytes(StandardCharsets.UTF_8);
            byte[] digest = md.digest(input);
            String hexString = Hex.encodeHexString(digest);
            if (hexString.startsWith("00000")) {
                char c = hexString.charAt(5);
                if (Character.isDigit(c)) {
                    int position = Integer.parseInt(String.valueOf(c));
                    if (!resultMap.containsKey(position) && position >= 0 && position < 8) {
                        resultMap.put(position, hexString.charAt(6));
                    }
                }
            }
            index++;
        }
        return resultMap.entrySet().stream()
                .sorted(Map.Entry.comparingByKey())
                .map(Map.Entry::getValue)
                .collect(StringBuilder::new, StringBuilder::append, StringBuilder::append)
                .toString();
    }
}
