package solvers_2015

import (
	"github.com/ernestosuarez/itertools"
	"strconv"
	"strings"
)

type Solver17 struct{}

func (s Solver17) SolvePart1(data string) int {
	return s.FindStorageCombinations(150, data)
}

func (s Solver17) SolvePart2(data string) int {
	return s.FindMinimumStorageCombinations(150, data)
}

func (s Solver17) FindStorageCombinations(liters int, data string) int {
	containers := s.ParseContainers(data)
	total := 0
	for i := 1; i <= len(containers); i++ {
		for combination := range itertools.CombinationsInt(containers, i) {
			if liters == s.Sum(combination) {
				total++
			}
		}
	}
	return total
}

func (s Solver17) ParseContainers(data string) []int {
	containers := make([]int, 0)
	for _, line := range strings.Split(strings.TrimSpace(data), "\n") {
		containers = append(containers, s.MustAtoi(line))
	}
	return containers
}

func (s Solver17) MustAtoi(intText string) int {
	i, err := strconv.Atoi(intText)
	if err != nil {
		panic(err)
	}
	return i
}

func (s Solver17) Sum(array []int) int {
	total := 0
	for _, c := range array {
		total += c
	}
	return total
}

func (s Solver17) FindMinimumStorageCombinations(liters int, data string) int {
	containers := s.ParseContainers(data)
	total := 0
	for i := 1; i <= len(containers); i++ {
		for combination := range itertools.CombinationsInt(containers, i) {
			if liters == s.Sum(combination) {
				total++
			}
		}
		if total > 0 {
			return total
		}
	}
	return total
}
