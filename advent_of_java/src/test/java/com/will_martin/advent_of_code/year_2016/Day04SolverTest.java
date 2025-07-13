package com.will_martin.advent_of_code.year_2016;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class Day04SolverTest {
    private Day04Solver sut;

    @BeforeEach
    void setUp() {
        sut = new Day04Solver();
    }

    @Test
    void solvePart1() {
        assertEquals("1514", sut.solvePart1("""
                aaaaa-bbb-z-y-x-123[abxyz]
                a-b-c-d-e-f-g-h-987[abcde]
                not-a-real-room-404[oarel]
                totally-real-room-200[decoy]
                """));
    }

    @Test
    void solvePart2() {
        assertEquals("-1", sut.solvePart2("""
                aaaaa-bbb-z-y-x-123[abxyz]
                a-b-c-d-e-f-g-h-987[abcde]
                not-a-real-room-404[oarel]
                totally-real-room-200[decoy]
                """));
    }
}
