package com.will_martin.advent_of_code.year_2015;

import com.google.common.collect.BiMap;
import com.google.common.collect.HashBiMap;
import com.will_martin.advent_of_code.Solver;

import java.util.ArrayList;
import java.util.HashSet;

public class Day11Solver implements Solver {
    final BiMap<Character, Integer> characterIntegerBiMap;
    final HashSet<Integer> confusingCharacters;
    public Day11Solver() {
        characterIntegerBiMap = HashBiMap.create();
        for (int i = 0; i < 26; i++) {
            characterIntegerBiMap.put((char) ('a' + i), i);
        }
        confusingCharacters = new HashSet<>();
        confusingCharacters.add(characterIntegerBiMap.get('i'));
        confusingCharacters.add(characterIntegerBiMap.get('o'));
        confusingCharacters.add(characterIntegerBiMap.get('l'));
    }

    @Override
    public String solvePart1(String data) {
        var password = convertToArray(data);
        while (!isValid(password)) {
            incrementPassword(password);
        }
        return convertFromArray(password);
    }

    private boolean isValid(ArrayList<Integer> password) {
        boolean includesStraight = false;
        var pairs = new HashSet<Integer>();
        for (int i = 0; i < password.size(); i++) {
            Integer thisCharacter = password.get(i);
            if (confusingCharacters.contains(thisCharacter)) {
                return false;
            }
            if (i >= 1) {
                Integer lastCharacter = password.get(i - 1);
                if (thisCharacter.equals(lastCharacter)) {
                    pairs.add(thisCharacter);
                }
                if (i >= 2 && thisCharacter == lastCharacter - 1 && lastCharacter == password.get(i - 2) - 1) {
                    includesStraight = true;
                }
            }
        }
        return includesStraight && pairs.size() >= 2;
    }

    private void incrementPassword(ArrayList<Integer> data) {
        var index = 0;
        boolean shouldIncrementNext;
        do {
            shouldIncrementNext = incrementPasswordAt(data, index++);
        }
        while (shouldIncrementNext);
    }

    private boolean incrementPasswordAt(ArrayList<Integer> data, int index) {
        if (index == data.size()) {
            data.add(0);
            return false;
        }
        int value = data.get(index) + 1;
        if (value == 26) {
            data.set(index, 0);
            return true;
        } else {
            data.set(index, value);
            return false;
        }
    }

    private String convertFromArray(ArrayList<Integer> password) {
        var sb = new StringBuilder();
        for (int i : password) {
            sb.append(characterIntegerBiMap.inverse().get(i));
        }
        return sb.reverse().toString();
    }

    private ArrayList<Integer> convertToArray(String data) {
        data = data.trim();
        var password = new ArrayList<Integer>();
        for (int i = data.length() - 1; i >= 0; i--) {
            password.add(characterIntegerBiMap.get(data.charAt(i)));
        }
        return password;
    }

    @Override
    public String solvePart2(String data) {
        var password = convertToArray(data);
        while (!isValid(password)) {
            incrementPassword(password);
        }
        do {
            incrementPassword(password);
        }
        while (!isValid(password));
        return convertFromArray(password);
    }
}
