package com.will_martin.advent_of_code.year_2015;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class Day11SolverTest {
    private Day11Solver sut;

    @BeforeEach
    void setUp() {
        sut = new Day11Solver();
    }

    @Test
    void shouldSolvePart1() {
        assertEquals("abcdffaa", sut.solvePart1("abcdefgh"));
        assertEquals("ghjaabcc", sut.solvePart1("ghijklmn"));
    }

}
