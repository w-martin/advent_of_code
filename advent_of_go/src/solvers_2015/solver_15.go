package solvers_2015

import (
	"regexp"
	"strconv"
	"strings"
)

type Solver15 struct {
	calorieLimit bool
}
type Solver15Ingredient struct {
	capacity   int
	durability int
	flavor     int
	texture    int
	calories   int
	allocation int
	name       string
}

var Solver15Regex1 = regexp.MustCompile(`^(?P<name>\w+): capacity (?P<capacity>-?\d+), durability (?P<durability>-?\d+), flavor (?P<flavor>-?\d+), texture (?P<texture>-?\d+), calories (?P<calories>-?\d+)$`)

func (s *Solver15) SolvePart1(data string) int {
	s.calorieLimit = false
	ingredients := s.parseIngredients(data)
	return s.findMaxSubAllocation(ingredients, 0, 100)
}

func (s *Solver15) SolvePart2(data string) int {
	s.calorieLimit = true
	ingredients := s.parseIngredients(data)
	return s.findMaxSubAllocation(ingredients, 0, 100)
}

func (s *Solver15) parseIngredients(data string) []Solver15Ingredient {
	result := make([]Solver15Ingredient, 0)
	for _, line := range strings.Split(strings.TrimSpace(data), "\n") {
		result = append(result, s.parseIngredient(line))
	}
	return result
}

func (s *Solver15) parseIngredient(line string) Solver15Ingredient {
	match := Solver15Regex1.FindStringSubmatch(line)
	return Solver15Ingredient{
		name:       match[1],
		capacity:   s.mustAtoi(match[2]),
		durability: s.mustAtoi(match[3]),
		flavor:     s.mustAtoi(match[4]),
		texture:    s.mustAtoi(match[5]),
		calories:   s.mustAtoi(match[6]),
	}
}

func (s *Solver15) mustAtoi(s2 string) int {
	result, err := strconv.Atoi(s2)
	if err != nil {
		panic(err)
	}
	return result
}

func (s *Solver15) findMaxSubAllocation(ingredients []Solver15Ingredient, ingredientIndex int, remainingTeaspoons int) int {
	if ingredientIndex == len(ingredients)-1 {
		ingredients[ingredientIndex].allocation = remainingTeaspoons
		amounts := [4]int{0, 0, 0, 0}
		calories := 0
		for _, ingredient := range ingredients {
			amounts[0] += ingredient.capacity * ingredient.allocation
			amounts[1] += ingredient.durability * ingredient.allocation
			amounts[2] += ingredient.flavor * ingredient.allocation
			amounts[3] += ingredient.texture * ingredient.allocation
			calories += ingredient.calories * ingredient.allocation
		}
		if !s.calorieLimit || calories == 500 {
			return max(0, amounts[0]) * max(0, amounts[1]) * max(0, amounts[2]) * max(0, amounts[3])
		} else {
			return 0
		}
	}

	maxTotal := 0
	for i := 0; i < remainingTeaspoons; i++ {
		ingredients[ingredientIndex].allocation = i
		total := s.findMaxSubAllocation(ingredients, ingredientIndex+1, remainingTeaspoons-i)
		if total > maxTotal {
			maxTotal = total
		}
	}
	return maxTotal
}
