package com.will_martin.advent_of_code.year_2015;

import com.will_martin.advent_of_code.Solver;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class Day04SolverTest {
    private Solver sut;

    @BeforeEach
    void setUp() {
        sut = new Day04Solver();
    }

    @Test
    void solvePart1() {
        assertEquals(609043, sut.solvePart1("abcdef"));
        assertEquals(1048970, sut.solvePart1("pqrstuv"));
    }

}
