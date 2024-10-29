package com.will_martin.advent_of_code.year_2015;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class Day14SolverTest {
    private Day14Solver sut;

    @BeforeEach
    void setUp() {
        sut = new Day14Solver();
    }

    @Test
    void solvePart1() {
        assertEquals(1120, sut.distanceAfter(1_000, """
                Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
                Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
                """));
    }

    @Test
    void solvePart2() {
        assertEquals(689, sut.pointsAfter(1_000, """
                Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
                Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
                """));
    }
}
