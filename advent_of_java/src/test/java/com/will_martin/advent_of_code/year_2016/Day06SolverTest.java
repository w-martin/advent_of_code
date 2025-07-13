package com.will_martin.advent_of_code.year_2016;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class Day06SolverTest {
    private Day06Solver sut;

    @BeforeEach
    void setUp() {
        sut = new Day06Solver();
    }

    @Test
    void solvePart1() {
        assertEquals("easter", sut.solvePart1("""
                eedadn
                   drvtee
                   eandsr
                   raavrd
                   atevrs
                   tsrnev
                   sdttsa
                   rasrtv
                   nssdts
                   ntnada
                   svetve
                   tesnvt
                   vntsnd
                   vrdear
                   dvrsen
                   enarar
                """));
    }

    @Test
    void solvePart2() {
        assertEquals("advent", sut.solvePart2("""
                eedadn
                   drvtee
                   eandsr
                   raavrd
                   atevrs
                   tsrnev
                   sdttsa
                   rasrtv
                   nssdts
                   ntnada
                   svetve
                   tesnvt
                   vntsnd
                   vrdear
                   dvrsen
                   enarar
                """));
    }
}
