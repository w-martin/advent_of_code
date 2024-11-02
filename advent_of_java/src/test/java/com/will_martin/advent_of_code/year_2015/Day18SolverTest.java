package com.will_martin.advent_of_code.year_2015;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class Day18SolverTest {
    private Day18Solver sut;
    private String data;

    @BeforeEach
    void setUp() {
        sut = new Day18Solver();
    }

    @Test
    void solvePart1() {
        assertEquals(4, sut.getNumLightsOnAfter(4, """
                .#.#.#
                      ...##.
                      #....#
                      ..#...
                      #.#..#
                      ####..""", 6,false));
    }

    @Test
    void solvePart2() {
        assertEquals(17, sut.getNumLightsOnAfter(5, """
                ##.#.#
                ...##.
                #....#
                ..#...
                #.#..#
                ####.#""", 6,true));
    }
}
