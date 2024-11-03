package com.will_martin.advent_of_code.year_2015;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class Day19SolverTest {
    private Day19Solver sut;
    private String data;

    @BeforeEach
    void setUp() {
        sut = new Day19Solver();
    }

    @Test
    void solvePart1() {
        assertEquals("4", sut.solvePart1("""
                H => HO
                H => OH
                O => HH

                HOH
                """));
        assertEquals("7", sut.solvePart1("""
                H => HO
                H => OH
                O => HH

                HOHOHO
                """));
    }

    @Test
    void solvePart2() {
        assertEquals("3", sut.solvePart2("""
                e => H
                e => O
                H => HO
                H => OH
                O => HH

                HOH
                """));
        assertEquals("6", sut.solvePart2("""
                e => H
                e => O
                H => HO
                H => OH
                O => HH

                HOHOHO
                """));
    }
}
