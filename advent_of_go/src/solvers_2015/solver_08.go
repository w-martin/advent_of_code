package solvers_2015

import (
	"regexp"
	"strings"
)

type Solver08 struct{}

var Solver08Part1Regex = regexp.MustCompile("(\\\\x.{2}|\\\\.)")
var Solver08Part2Regex = regexp.MustCompile("(\"|\\\\)")

func (Solver08) SolvePart1(data string) int {
	data = strings.TrimSpace(data)
	sum := 0
	for _, line := range strings.Split(data, "\n") {
		replacedLine := Solver08Part1Regex.ReplaceAllString(line[1:len(line)-1], "1")
		sum += len(line) - len(replacedLine)
	}
	return sum
}

func (Solver08) SolvePart2(data string) int {
	data = strings.TrimSpace(data)
	sum := 0
	for _, line := range strings.Split(data, "\n") {
		replacedLine := Solver08Part2Regex.ReplaceAllString(line, "1${1}")
		sum += 2 + len(replacedLine) - len(line)
	}
	return sum
}
