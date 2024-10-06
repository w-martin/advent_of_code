package com.will_martin.advent_of_code.year_2015;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class U16Test {

    @Test
    void testAnd() {
        assertEquals(1, U16.ParseU16("5").and(U16.ParseU16("3")).toInteger());
    }

    @Test
    void testOr() {
        assertEquals(7, U16.ParseU16("5").or(U16.ParseU16("2")).toInteger());
    }

    @Test
    void testNot() {
        assertEquals(Short.MAX_VALUE - Short.MIN_VALUE - 5, U16.ParseU16("5").not().toInteger());
    }

    @Test
    void testRshift() {
        assertEquals(1, U16.ParseU16("5").rshift(2).toInteger());
    }

    @Test
    void testLshift() {
        assertEquals(20, U16.ParseU16("5").lshift(2).toInteger());
    }

    @Test
    void testParseU16() {
        assertEquals(456, U16.ParseU16("456").toInteger());
    }

    @Test
    void testRshiftYG() {
        assertEquals(114, U16.ParseU16("456").rshift(2).toInteger());
    }
}
