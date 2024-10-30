package com.will_martin.advent_of_code.year_2015;

import com.will_martin.advent_of_code.Solver;
import lombok.Builder;

import java.util.ArrayList;
import java.util.List;
import java.util.regex.Pattern;

public class Day15Solver implements Solver {
    private static final Pattern ingredientRegex = Pattern.compile("(?<name>\\w+): capacity (?<capacity>-?\\d+), durability (?<durability>-?\\d+), flavor (?<flavor>-?\\d+), texture (?<texture>-?\\d+), calories (?<calories>-?\\d+)");
    private final static int teaspoons = 100;
    private Integer calorieLimit;

    @Builder
    private static class Ingredient {
        private final String name;
        private final int capacity;
        private final int durability;
        private final int flavor;
        private final int texture;
        private final int calories;
        @Builder.Default
        int allocation = 0;
    }

    @Override
    public String solvePart1(String data) {
        calorieLimit = null;
        List<Ingredient> ingredientList = parseIngredients(data);
        return String.valueOf(findMaxAllocation(ingredientList, 0, teaspoons));
    }

    private int findMaxAllocation(List<Ingredient> ingredientList, int ingredientIndex, int remainingTeaspoons) {
        if (ingredientIndex == ingredientList.size() - 1) {
            ingredientList.get(ingredientIndex).allocation = remainingTeaspoons;
            int sumCapacity = Math.max(0, ingredientList.stream().mapToInt(ingredient -> ingredient.capacity * ingredient.allocation).sum());
            int sumDurability = Math.max(0, ingredientList.stream().mapToInt(ingredient -> ingredient.durability * ingredient.allocation).sum());
            int sumFlavor = Math.max(0, ingredientList.stream().mapToInt(ingredient -> ingredient.flavor * ingredient.allocation).sum());
            int sumTexture = Math.max(0, ingredientList.stream().mapToInt(ingredient -> ingredient.texture * ingredient.allocation).sum());
            int sumCalories = Math.max(0, ingredientList.stream().mapToInt(ingredient -> ingredient.calories * ingredient.allocation).sum());
            if (calorieLimit != null && sumCalories != calorieLimit) {
                return 0;
            }
            return sumCapacity * sumDurability * sumFlavor * sumTexture;
        }
        int highScore = Integer.MIN_VALUE;
        for (int i = 0; i < remainingTeaspoons; i++) {
            ingredientList.get(ingredientIndex).allocation = i;
            int score = findMaxAllocation(ingredientList, ingredientIndex + 1, remainingTeaspoons - i);
            if (score > highScore) {
                highScore = score;
            }
        }
        return highScore;
    }

    private List<Ingredient> parseIngredients(final String data) {
        var result = new ArrayList<Ingredient>();
        var matcher = ingredientRegex.matcher(data);
        while (matcher.find()) {
            result.add(Ingredient.builder().
                    name(matcher.group("name")).
                    capacity(Integer.parseInt(matcher.group("capacity"))).
                    durability(Integer.parseInt(matcher.group("durability"))).
                    flavor(Integer.parseInt(matcher.group("flavor"))).
                    texture(Integer.parseInt(matcher.group("texture"))).
                    calories(Integer.parseInt(matcher.group("calories"))).
                    build()
            );
        }
        return result;
    }

    @Override
    public String solvePart2(String data) {
        calorieLimit = 500;
        List<Ingredient> ingredientList = parseIngredients(data);
        return String.valueOf(findMaxAllocation(ingredientList, 0, teaspoons));
    }
}
