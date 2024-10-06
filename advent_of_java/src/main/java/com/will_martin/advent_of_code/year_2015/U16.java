package com.will_martin.advent_of_code.year_2015;

import lombok.Value;

@Value
public class U16 {
    boolean[] buffer;

    public static U16 ParseU16(String valueText) {
        int value = Integer.parseUnsignedInt(valueText);
        boolean[] b = new boolean[16];
        for (int i = 0; i <b.length; i++) {
            boolean bit = (value % 2) > 0;
            b[i] = bit;
            value /= 2;
        }
        return new U16(b);
    }

    public U16 and(final U16 other) {
        boolean[] result = new boolean[16];
        for (int i = 0; i < result.length; i++) {
            result[i] = buffer[i] && other.buffer[i];
        }
        return new U16(result);
    }

    public U16 or(final U16 other) {
        boolean[] result = new boolean[16];
        for (int i = 0; i < result.length; i++) {
            result[i] = buffer[i] || other.buffer[i];
        }
        return new U16(result);
    }

    public U16 not() {
        boolean[] result = new boolean[16];
        for (int i = 0; i < result.length; i++) {
            result[i] = !buffer[i];
        }
        return new U16(result);
    }

    public U16 lshift(final int amount) {
        boolean[] result = new boolean[16];
        for (int i = 0; i < result.length; i++) {
            result[i] = (i < amount) ? false : buffer[i - amount];
        }
        return new U16(result);
    }

    public U16 rshift(final int amount) {
        boolean[] result = new boolean[16];
        for (int i = 0; i < result.length; i++) {
            result[i] = (i >= buffer.length - amount) ? false : buffer[i + amount];
        }
        return new U16(result);
    }

    public Integer toInteger() {
        int result = 0;
        for (int i = 0; i < buffer.length; i++) {
            if (buffer[i]) {
                result += (int) Math.pow(2, i);
            }
        }
        return result;
    }
}
