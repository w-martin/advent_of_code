package com.will_martin.advent_of_code.year_2016;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class Day05SolverTest {
    private Day05Solver sut;

    @BeforeEach
    void setUp() {
        sut = new Day05Solver();
    }

    @Test
    void solvePart1() {
        assertEquals("18f47a30", sut.solvePart1("""
                abc
                """));
    }

    @Test
    void solvePart2() {
        assertEquals("05ace8e3", sut.solvePart2("""
                abc
                """));
    }
}
