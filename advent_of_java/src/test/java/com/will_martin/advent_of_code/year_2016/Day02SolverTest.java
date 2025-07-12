package com.will_martin.advent_of_code.year_2016;

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
        assertEquals("1985", sut.solvePart1("""
                ULL
                RRDDD
                LURDL
                UUUUD"""));
    }

    @Test
    void solvePart2() {
        assertEquals("5DB3", sut.solvePart2("""
                ULL
                RRDDD
                LURDL
                UUUUD"""));
    }
}
