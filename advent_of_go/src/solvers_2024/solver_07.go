package solvers_2024

import (
	"strconv"
	"strings"
)

type Solver07 struct{}

type Solver07Option struct {
	parts []int
	total int
}

func (s *Solver07) SolvePart1(data string) int {
	total := 0
	for _, line := range strings.Split(strings.TrimSpace(data), "\n") {
		line = strings.TrimSpace(line)
		if len(line) == 0 {
			continue
		}
		testValue, parts := s.parseLine(line)
		q := make([]*Solver07Option, 0)
		q = append(q, &Solver07Option{
			parts: parts[1:],
			total: parts[0],
		})
		found := false
		for len(q) > 0 {
			option := q[0]
			if len(q) > 1 {
				q = q[1:]
			} else {
				q = make([]*Solver07Option, 0)
			}
			if len(option.parts) == 0 {
				if option.total == testValue {
					found = true
					break
				} else {
					continue
				}
			}
			value := option.parts[0]
			var remainingParts []int
			if len(option.parts) > 1 {
				remainingParts = option.parts[1:]
			} else {
				remainingParts = make([]int, 0)
			}
			q = append(q, &Solver07Option{
				parts: remainingParts,
				total: option.total + value,
			}, &Solver07Option{
				parts: remainingParts,
				total: option.total * value,
			})
		}
		if found {
			total += testValue
		}
	}

	return total
}

func (s *Solver07) parseLine(line string) (int, []int) {
	separator := strings.Index(line, ":")
	testValue := s.mustAtoi(line[:separator])
	stringParts := strings.Split(line[separator+2:], " ")
	parts := make([]int, len(stringParts))
	for i, part := range stringParts {
		parts[i] = s.mustAtoi(part)
	}
	return testValue, parts
}

func (Solver07) mustAtoi(data string) int {
	value, err := strconv.Atoi(data)
	if err != nil {
		panic(err)
	}
	return value
}

func (s *Solver07) SolvePart2(data string) int {
	total := 0
	for _, line := range strings.Split(strings.TrimSpace(data), "\n") {
		line = strings.TrimSpace(line)
		if len(line) == 0 {
			continue
		}
		testValue, parts := s.parseLine(line)
		q := make([]*Solver07Option, 0)
		q = append(q, &Solver07Option{
			parts: parts[1:],
			total: parts[0],
		})
		found := false
		for len(q) > 0 {
			option := q[0]
			if len(q) > 1 {
				q = q[1:]
			} else {
				q = make([]*Solver07Option, 0)
			}
			if len(option.parts) == 0 {
				if option.total == testValue {
					found = true
					break
				} else {
					continue
				}
			}
			value := option.parts[0]
			var remainingParts []int
			if len(option.parts) > 1 {
				remainingParts = option.parts[1:]
			} else {
				remainingParts = make([]int, 0)
			}
			q = append(q, &Solver07Option{
				parts: remainingParts,
				total: option.total + value,
			}, &Solver07Option{
				parts: remainingParts,
				total: option.total * value,
			}, &Solver07Option{
				parts: remainingParts,
				total: s.Concat(option.total, value),
			})
		}
		if found {
			total += testValue
		}
	}

	return total
}

func (s *Solver07) Concat(a int, b int) int {
	result, _ := strconv.Atoi(strconv.Itoa(a) + strconv.Itoa(b))
	return result
}
