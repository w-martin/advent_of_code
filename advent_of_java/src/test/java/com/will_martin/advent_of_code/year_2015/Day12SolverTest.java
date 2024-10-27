package com.will_martin.advent_of_code.year_2015;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class Day12SolverTest {
    private Day12Solver sut;

    @BeforeEach
    void setUp() {
        sut = new Day12Solver();
    }

    @Test
    void shouldSolvePart1() {
        assertEquals("6", sut.solvePart1("[1,2,3]"));
        assertEquals("6", sut.solvePart1("""
                {"a":2,"b":4}"""));
        assertEquals("3", sut.solvePart1("[[[3]]]"));
        assertEquals("3", sut.solvePart1("""
                {"a":{"b":4},"c":-1}"""));
        assertEquals("0", sut.solvePart1("""
                {"a":[-1,1]}"""));
        assertEquals("0", sut.solvePart1("""
                [-1,{"a":1}]"""));
        assertEquals("0", sut.solvePart1("[]"));
        assertEquals("0", sut.solvePart1("{}"));
    }

    @Test
    void shouldSolvePart2() {
        assertEquals("6", sut.solvePart2("[1,2,3]"));
        assertEquals("4", sut.solvePart2("""
                [1,{"c":"red","b":2},3]"""));
        assertEquals("0", sut.solvePart2("""
                {"d":"red","e":[1,2,3,4],"f":5}"""));
        assertEquals("6", sut.solvePart2("""
                [1,"red",5]"""));
    }

}
