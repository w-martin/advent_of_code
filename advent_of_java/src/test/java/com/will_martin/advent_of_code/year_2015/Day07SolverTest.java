package com.will_martin.advent_of_code.year_2015;

import com.will_martin.advent_of_code.Solver;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class Day07SolverTest {
    private Solver sut;

    @BeforeEach
    void setUp() {
        sut = new Day07Solver();
    }

    @Test
    void solvePart1() {
        String data = """
123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
                """;
        assertEquals(72, sut.solvePart1("d\n" + data));
        assertEquals(507, sut.solvePart1("e\n" + data));
        assertEquals(492, sut.solvePart1("f\n" + data));
        assertEquals(114, sut.solvePart1("g\n" + data));
        assertEquals(65412, sut.solvePart1("h\n" + data));
        assertEquals(65079, sut.solvePart1("i\n" + data));
        assertEquals(123, sut.solvePart1("x\n" + data));
        assertEquals(456, sut.solvePart1("y\n" + data));
    }

    @Test
    void solvePart2() {
        String data = """
c OR b -> a
46066 -> c
9 -> b
""";
        assertEquals(46066, sut.solvePart2("c\n" + data));
        assertEquals(46067, sut.solvePart2("a\n" + data));
        assertEquals(46065, sut.solvePart2("b\n" + data));
    }

}
