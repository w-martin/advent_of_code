package solvers_2015

import (
	"regexp"
	"strconv"
	"strings"
)

type Solver16 struct{}

var Solver16Regex = regexp.MustCompile(`(\w+): (\d+)`)

func (s *Solver16) SolvePart1(data string) int {
	knownFacts := map[string]int{
		"children":    3,
		"cats":        7,
		"samoyeds":    2,
		"pomeranians": 3,
		"akitas":      0,
		"vizslas":     0,
		"goldfish":    5,
		"trees":       3,
		"cars":        2,
		"perfumes":    1,
	}
	for i, line := range strings.Split(strings.TrimSpace(data), "\n") {
		found := true
		for _, match := range Solver16Regex.FindAllStringSubmatch(line, -1) {
			name := match[1]
			value := match[2]
			if knownFacts[name] != s.mustAtoi(value) {
				found = false
				break
			}
		}
		if found {
			return 1 + i
		}
	}
	return 0
}

func (s *Solver16) SolvePart2(data string) int {
	knownFacts := map[string]int{
		"children":    3,
		"cats":        7,
		"samoyeds":    2,
		"pomeranians": 3,
		"akitas":      0,
		"vizslas":     0,
		"goldfish":    5,
		"trees":       3,
		"cars":        2,
		"perfumes":    1,
	}
	moreThan := map[string]bool{
		"cats":  true,
		"trees": true,
	}
	fewerThan := map[string]bool{
		"pomeranians": true,
		"goldfish":    true,
	}
	for i, line := range strings.Split(strings.TrimSpace(data), "\n") {
		found := true
		for _, match := range Solver16Regex.FindAllStringSubmatch(line, -1) {
			name := match[1]
			value := s.mustAtoi(match[2])
			expected := knownFacts[name]
			if _, ok := moreThan[name]; ok {
				found = value > expected
			} else if _, ok := fewerThan[name]; ok {
				found = value < expected
			} else {
				found = value == expected
			}
			if !found {
				break
			}
		}
		if found {
			return 1 + i
		}
	}
	return 0
}

func (s *Solver16) mustAtoi(value string) int {
	result, err := strconv.Atoi(value)
	if err != nil {
		panic(err)
	}
	return result
}
