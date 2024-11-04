package com.will_martin.advent_of_code.year_2015;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class Day20SolverTest {
    private Day20Solver sut;

    @BeforeEach
    void setUp() {
        sut = new Day20Solver();
    }

    @Test
    void solvePart1() {
        assertEquals("1", sut.solvePart1("10"));
        assertEquals("2", sut.solvePart1("30"));
        assertEquals("3", sut.solvePart1("40"));
        assertEquals("4", sut.solvePart1("70"));
    }
}
