package com.will_martin.advent_of_code.year_2015;

import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.will_martin.advent_of_code.Solver;
import lombok.SneakyThrows;

import java.util.List;
import java.util.Map;

public class Day12Solver implements Solver {
    @SneakyThrows
    @Override
    public String solvePart1(String data) {
        ObjectMapper objectMapper = new ObjectMapper();
        Object l = objectMapper.readValue(data, new TypeReference<>(){});
        return String.valueOf(innerSum1(l));
    }

    private Integer innerSum1(Object object) {
        if (object instanceof List<?>) {
            return ((List<?>) object).stream().mapToInt(this::innerSum1).sum();
        } else if (object instanceof Integer) {
            return (Integer) object;
        } else if (object instanceof Map<?, ?> map) {
            return map.values().stream().mapToInt(this::innerSum1).sum();
        }
        return 0;
    }

    private Integer innerSum2(Object object) {
        if (object instanceof List<?>) {
            return ((List<?>) object).stream().mapToInt(this::innerSum2).sum();
        } else if (object instanceof Integer) {
            return (Integer) object;
        } else if (object instanceof Map<?, ?> map) {
            if (map.containsValue("red")) {
                return 0;
            }
            return map.values().stream().mapToInt(this::innerSum2).sum();
        }
        return 0;
    }

    @SneakyThrows
    @Override
    public String solvePart2(String data) {
        ObjectMapper objectMapper = new ObjectMapper();
        Object l = objectMapper.readValue(data, new TypeReference<>(){});
        return String.valueOf(innerSum2(l));
    }
}
