package com.will_martin.advent_of_code.year_2016;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class Day03SolverTest {
    private Day03Solver sut;

    @BeforeEach
    void setUp() {
        sut = new Day03Solver();
    }

    @Test
    void solvePart1() {
        assertEquals("1", sut.solvePart1("""
                5 10 25
                5 10 12"""));
    }

    @Test
    void solvePart2() {
        assertEquals("6", sut.solvePart2("""
                101 301 501
                     102 302 502
                     103 303 503
                     201 401 601
                     202 402 602
                     203 403 603
                """));
    }
}
