package com.will_martin.advent_of_code.year_2015;

import com.will_martin.advent_of_code.Solver;
import lombok.SneakyThrows;
import lombok.val;

import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class Day04Solver implements Solver {
    @SneakyThrows
    @Override
    public String solvePart1(String data) {
        return String.valueOf(findHashWithNumZeroes(data, 5));
    }

    private int findHashWithNumZeroes(String data, int numZeroes) throws NoSuchAlgorithmException {
        data = data.trim();
        var md = MessageDigest.getInstance("MD5");
        for (int counter = 0; counter < Integer.MAX_VALUE; counter++) {
            val hash = md.digest((data + counter).getBytes(StandardCharsets.UTF_8));
            if (startsWithZeroes(hash, numZeroes)) {
                return counter;
            }
        }
        return -1;
    }

    private boolean startsWithZeroes(byte[] hash, int numZeroes) {
        int numZeroBytes = numZeroes / 2;
        for (int i = 0; i < numZeroBytes; i++) {
            if (hash[i] != 0) {
                return false;
            }
        }
        if (numZeroes % 2 == 1) {
            return (hash[numZeroBytes] & 0xf0) == 0;
        }
        return true;
    }

    @SneakyThrows
    @Override
    public String solvePart2(String data) {
        return String.valueOf(findHashWithNumZeroes(data, 6));
    }
}
