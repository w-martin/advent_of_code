package com.will_martin.advent_of_code.year_2015;

import com.will_martin.advent_of_code.Solver;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class Day09SolverTest {
    private Solver sut;

    @BeforeEach
    void setUp() {
        sut = new Day09Solver();
    }

    @Test
    void solvePart1() {
        String data = """
London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
                """;
        assertEquals("605", sut.solvePart1(data));
    }

    @Test
    void solvePart2() {
        String data = """
London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
                """;
        assertEquals("982", sut.solvePart2(data));
    }

}
