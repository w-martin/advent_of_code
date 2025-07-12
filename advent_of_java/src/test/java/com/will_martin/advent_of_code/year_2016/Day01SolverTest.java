package com.will_martin.advent_of_code.year_2016;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class Day01SolverTest {
    private Day01Solver sut;

    @BeforeEach
    void setUp() {
        sut = new Day01Solver();
    }

    @Test
    void solvePart1() {
        assertEquals("5", sut.solvePart1("R2, L3"));
        assertEquals("2", sut.solvePart1("R2, R2, R2"));
        assertEquals("12", sut.solvePart1("R5, L5, R5, R3 "));
    }

    @Test
    void solvePart2() {
        assertEquals("4", sut.solvePart2("R8, R4, R4, R8,"));
    }
}
