package com.will_martin.advent_of_code.year_2015;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class Day02SolverTest {
    private Day02Solver sut;

    @BeforeEach
    void setUp() {
        sut = new Day02Solver();
    }

    @Test
    void solvePart1() {
        assertEquals(58, sut.solvePart1("2x3x4"));
        assertEquals(43, sut.solvePart1("1x1x10"));
        assertEquals(3632, sut.solvePart1("22x29x19"));
    }

    @Test
    void solvePart2() {
        assertEquals(34, sut.solvePart2("2x3x4"));
        assertEquals(14, sut.solvePart2("1x1x10"));
    }
}