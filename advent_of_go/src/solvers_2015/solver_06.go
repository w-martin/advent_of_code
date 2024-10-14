package solvers_2015

import (
	"regexp"
	"strconv"
	"strings"
)

type Solver06 struct{}

func (Solver06) SolvePart1(data string) int {
	regex := regexp.MustCompile(`^(?P<instruction>turn on|turn off|toggle) (?P<x0>\d+),(?P<y0>\d+) through (?P<x1>\d+),(?P<y1>\d+)$`)
	var lights [1000][1000]bool
	for _, line := range strings.Split(strings.TrimSpace(data), "\n") {
		matchGroups := regex.FindStringSubmatch(line)
		instruction := matchGroups[1]
		x0, _ := strconv.Atoi(matchGroups[2])
		y0, _ := strconv.Atoi(matchGroups[3])
		x1, _ := strconv.Atoi(matchGroups[4])
		y1, _ := strconv.Atoi(matchGroups[5])
		switch instruction {
		case "turn on":
			for x := x0; x <= x1; x++ {
				for y := y0; y <= y1; y++ {
					lights[x][y] = true
				}
			}
		case "turn off":
			for x := x0; x <= x1; x++ {
				for y := y0; y <= y1; y++ {
					lights[x][y] = false
				}
			}
		case "toggle":
			for x := x0; x <= x1; x++ {
				for y := y0; y <= y1; y++ {
					lights[x][y] = !lights[x][y]
				}
			}
		}
	}
	count := 0
	for _, row := range lights {
		for _, light := range row {
			if light {
				count++
			}
		}
	}
	return count
}

func (Solver06) SolvePart2(data string) int {
	regex := regexp.MustCompile(`^(?P<instruction>turn on|turn off|toggle) (?P<x0>\d+),(?P<y0>\d+) through (?P<x1>\d+),(?P<y1>\d+)$`)
	var lights [1000][1000]int8
	for _, line := range strings.Split(strings.TrimSpace(data), "\n") {
		matchGroups := regex.FindStringSubmatch(line)
		instruction := matchGroups[1]
		x0, _ := strconv.Atoi(matchGroups[2])
		y0, _ := strconv.Atoi(matchGroups[3])
		x1, _ := strconv.Atoi(matchGroups[4])
		y1, _ := strconv.Atoi(matchGroups[5])
		switch instruction {
		case "turn on":
			for x := x0; x <= x1; x++ {
				for y := y0; y <= y1; y++ {
					lights[x][y] += 1
				}
			}
		case "turn off":
			for x := x0; x <= x1; x++ {
				for y := y0; y <= y1; y++ {
					lights[x][y] = max(0, lights[x][y]-1)
				}
			}
		case "toggle":
			for x := x0; x <= x1; x++ {
				for y := y0; y <= y1; y++ {
					lights[x][y] += 2
				}
			}
		}
	}
	count := int32(0)
	for _, row := range lights {
		for _, light := range row {
			count += int32(light)
		}
	}
	return int(count)
}
