package com.will_martin.advent_of_code.year_2015;

import com.will_martin.advent_of_code.Solver;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class Day10SolverTest {
    private Day10Solver sut;

    @BeforeEach
    void setUp() {
        sut = new Day10Solver();
    }

    @Test
    void shouldLookAndSay() {
        assertEquals("11", sut.lookAndSay("1"));
        assertEquals("21", sut.lookAndSay("11"));
        assertEquals("1211", sut.lookAndSay("21"));
        assertEquals("111221", sut.lookAndSay("1211"));
        assertEquals("312211", sut.lookAndSay("111221"));
    }

}
