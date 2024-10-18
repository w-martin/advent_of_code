package com.will_martin.advent_of_code.year_2015;

import com.will_martin.advent_of_code.Solver;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class Day03SolverTest {
    private Solver sut;

    @BeforeEach
    void setUp() {
        sut = new Day03Solver();
    }

    @Test
    void solvePart1() {
        assertEquals(2, sut.solvePart1(">"));
        assertEquals(4, sut.solvePart1("^>v<"));
        assertEquals(2, sut.solvePart1("^v^v^v^v^v"));
    }

    @Test
    void solvePart2() {
        assertEquals(3, sut.solvePart2("^v"));
        assertEquals(3, sut.solvePart2("^>v<"));
        assertEquals(11, sut.solvePart2("^v^v^v^v^v"));
    }
}
