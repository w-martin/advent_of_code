package com.will_martin.advent_of_code.year_2015;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class Day01SolverTest {
    private Day01Solver sut;

    @BeforeEach
    void setUp() {
        sut = new Day01Solver();
    }

    @Test
    void solvePart1() {
        assertEquals("0", sut.solvePart1("(())"));
        assertEquals("0", sut.solvePart1("()()"));
        assertEquals("3", sut.solvePart1("((("));
        assertEquals("3", sut.solvePart1("(()(()("));
        assertEquals("3", sut.solvePart1("))((((("));
        assertEquals("-1", sut.solvePart1("())"));
        assertEquals("-1", sut.solvePart1("))("));
        assertEquals("-3", sut.solvePart1(")))"));
        assertEquals("-3", sut.solvePart1(")())())"));
    }

    @Test
    void solvePart2() {
        assertEquals("1", sut.solvePart2(")"));
        assertEquals("5", sut.solvePart2("()())"));
    }
}
