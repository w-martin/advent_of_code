package solvers_2015

import (
	"fmt"
	"strconv"
	"strings"
)

type Solver20 struct{}

func (s Solver20) SolvePart1(data string) int {
	target := s.MustAtoi(strings.TrimSpace(data))
	N := target / 2
	houses := make([]int, N)
	for i := 1; i < N; i++ {
		for j := i; j < N; j += i {
			houses[j] += i * 10
		}
	}
	argLowest := -1
	for i, v := range houses {
		if v >= target {
			fmt.Println("Found", i, "with", v, ">=", target)
			return i
		}
	}
	fmt.Println("Found nothing")
	return argLowest
}

func (s Solver20) SolvePart2(data string) int {
	target := s.MustAtoi(strings.TrimSpace(data))
	N := target / 2
	houses := make([]int, N)
	for i := 1; i < N; i++ {
		for j := i; j < min(N, i*50); j += i {
			houses[j] += i * 11
		}
	}
	argLowest := -1
	for i, v := range houses {
		if v >= target {
			fmt.Println("Found", i, "with", v, ">=", target)
			return i
		}
	}
	fmt.Println("Found nothing")
	return argLowest
}

func (s Solver20) MustAtoi(data string) int {
	value, err := strconv.Atoi(data)
	if err != nil {
		panic(err)
	}
	return value
}
