package com.will_martin.advent_of_code.year_2015;

import com.will_martin.advent_of_code.Solver;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class Day08SolverTest {
    private Solver sut;

    @BeforeEach
    void setUp() {
        sut = new Day08Solver();
    }

    @Test
    void solvePart1() {
        String data = """
""
"abc"
"aaa\\"aaa"
"\\x27"
                """;
        assertEquals(12, sut.solvePart1(data));
    }

    @Test
    void solvePart2() {
        String data = """
""
"abc"
"aaa\\"aaa"
"\\x27"
                """;
        assertEquals(19, sut.solvePart2(data));
    }

}
