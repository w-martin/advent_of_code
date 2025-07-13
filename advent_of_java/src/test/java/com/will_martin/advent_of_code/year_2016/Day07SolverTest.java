package com.will_martin.advent_of_code.year_2016;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class Day07SolverTest {
    private Day07Solver sut;

    @BeforeEach
    void setUp() {
        sut = new Day07Solver();
    }

    @Test
    void solvePart1() {
        assertEquals("2", sut.solvePart1("""
                abba[mnop]qrst
                   abcd[bddb]xyyx
                   aaaa[qwer]tyui
                   ioxxoj[asdfgh]zxcvbn
                """));
    }

    @Test
    void solvePart2() {
        assertEquals("3", sut.solvePart2("""
        aba[bab]xyz
        xyx[xyx]xyx
        aaa[kek]eke
        zazbz[bzb]cdb
                """));
    }
}
