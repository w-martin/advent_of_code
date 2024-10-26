package com.will_martin.advent_of_code.year_2015;

import com.will_martin.advent_of_code.Solver;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day08Solver implements Solver {
    private static final Pattern specialCharacterRegex1 = Pattern.compile("(\\\\x.{2}|\\\\.)");
    private static final Pattern specialCharacterRegex2 = Pattern.compile("(\"|\\\\)");

    @Override
    public String solvePart1(String data) {
        return data.trim().lines().map(line -> {
            int totalLength = line.length();
            line = line.substring(1, line.length() - 1);

            // build new string with specials replaced by '1'
            Matcher matcher = specialCharacterRegex1.matcher(line);
            StringBuilder output = new StringBuilder();
            int lastIndex = 0;
            while (matcher.find()) {
                output.append(line, lastIndex, matcher.start()).append("1");
                lastIndex = matcher.end();
            }
            if (lastIndex < line.length()) {
                output.append(line, lastIndex, line.length());
            }

            int numSpecialCharacters = output.length();
            return totalLength - numSpecialCharacters;
        }).reduce(0, Integer::sum).toString();
    }

    private static String convert(String token) {
        return "\\" + token;
    }

    @Override
    public String solvePart2(String data) {
        return data.trim().lines().map(line -> {
            int originalLength = line.length();

            // build new string with specials replaced by '1'
            Matcher matcher = specialCharacterRegex2.matcher(line);
            StringBuilder output = new StringBuilder();
            output.append("\"");
            int lastIndex = 0;
            while (matcher.find()) {
                output.append(line, lastIndex, matcher.start())
                        .append(convert(matcher.group(1)));
                lastIndex = matcher.end();
            }
            if (lastIndex < line.length()) {
                output.append(line, lastIndex, line.length());
            }
            output.append("\"");
            int newLength = output.length();
            return newLength - originalLength;
        }).reduce(0, Integer::sum).toString();
    }
}
