package com.will_martin.advent_of_code.year_2015;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class Day15SolverTest {
    private Day15Solver sut;
    private String data;

    @BeforeEach
    void setUp() {
        sut = new Day15Solver();
        data = """
                Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
                Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
                """;
    }

    @Test
    void solvePart1() {
        assertEquals("62842880", sut.solvePart1(data));
    }

    @Test
    void solvePart2() {
        assertEquals("57600000", sut.solvePart2(data));
    }
}
