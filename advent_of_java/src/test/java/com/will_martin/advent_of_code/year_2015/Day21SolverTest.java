package com.will_martin.advent_of_code.year_2015;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class Day21SolverTest {
    private Day21Solver sut;

    @BeforeEach
    void setUp() {
        sut = new Day21Solver();
    }

    @Test
    void testFight() {
        assertTrue(sut.playerWins(8, 5, 5, 12, 7, 2));
        assertFalse(sut.playerWins(8, 4, 5, 12, 7, 2));
    }

    @Test
    void testSolvePart1() {
        String result = sut.solvePart1("""
                Hit Points: 100
                Damage: 10
                Armor: 1""");
        assertNotNull(result);
    }

    @Test
    void testSolvePart2() {
        String result = sut.solvePart1("""
                Hit Points: 100
                Damage: 10
                Armor: 1""");
        assertNotNull(result);
    }
}
