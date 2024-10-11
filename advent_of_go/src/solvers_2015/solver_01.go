package solvers_2015

import "strings"

type Solver01 struct{}

func (Solver01) SolvePart1(data string) int {
	return strings.Count(data, "(") - strings.Count(data, ")")
}

func (Solver01) SolvePart2(data string) int {
	position := 0
	for i, c := range data {
		switch c {
		case '(':
			position++
		case ')':
			position--
		}
		if position < 0 {
			return 1 + i
		}
	}
	return -1
}
