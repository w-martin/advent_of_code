package com.will_martin.advent_of_code.year_2015;

import com.will_martin.advent_of_code.Solver;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class Day06SolverTest {
    private Solver sut;

    @BeforeEach
    void setUp() {
        sut = new Day06Solver();
    }

    @Test
    void solvePart1() {
        assertEquals(String.valueOf(1_000_000), sut.solvePart1("turn on 0,0 through 999,999"));
        assertEquals(String.valueOf(1_000), sut.solvePart1("toggle 0,0 through 999,0"));
        assertEquals(String.valueOf(0), sut.solvePart1("turn off 499,499 through 500,500"));
    }

    @Test
    void solvePart2() {
        assertEquals(String.valueOf(1), sut.solvePart2("turn on 0,0 through 0,0"));
        assertEquals(String.valueOf(2000000), sut.solvePart2("toggle 0,0 through 999,999"));
    }

}
