package com.will_martin.advent_of_code.year_2015;

import com.will_martin.advent_of_code.Solver;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class Day05SolverTest {
    private Solver sut;

    @BeforeEach
    void setUp() {
        sut = new Day05Solver();
    }

    @Test
    void solvePart1() {
        assertEquals(1, sut.solvePart1("ugknbfddgicrmopn"));
        assertEquals(1, sut.solvePart1("aaa"));
        assertEquals(0, sut.solvePart1("jchzalrnumimnmhp"));
        assertEquals(0, sut.solvePart1("haegwjzuvuyypxyu"));
        assertEquals(0, sut.solvePart1("dvszwmarrgswjxmb"));
    }

    @Test
    void solvePart2() {
        assertEquals(1, sut.solvePart2("qjhvhtzxzqqjkmpb"));
        assertEquals(1, sut.solvePart2("xxyxx"));
        assertEquals(0, sut.solvePart2("uurcxstgmygtbstg"));
        assertEquals(0, sut.solvePart2("ieodomkazucvgmuy"));
    }

}