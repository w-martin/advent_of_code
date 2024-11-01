package com.will_martin.advent_of_code.year_2015;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class Day17SolverTest {
    private Day17Solver sut;
    private String data;

    @BeforeEach
    void setUp() {
        sut = new Day17Solver();
        data = """
                20
                15
                10
                5
                5

                """;
    }

    @Test
    void solvePart1() {
        assertEquals(4, sut.getNumDistinctCombinationFor(25, data));
    }

    @Test
    void solvePart2() {
        assertEquals(3, sut.getMinimumNumContainersFor(25, data));
    }
}
