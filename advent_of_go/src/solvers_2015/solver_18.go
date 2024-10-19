package solvers_2015

import (
	"strings"
)

type Solver18 struct{}

func (s Solver18) SolvePart1(data string) int {
	return s.FindHowManyLightsOnAfter(100, data, false)
}

func (s Solver18) SolvePart2(data string) int {
	return s.FindHowManyLightsOnAfter(100, data, true)
}

func (s Solver18) FindHowManyLightsOnAfter(steps int, data string, cornersStayOn bool) int {
	lights := s.parseLights(data)
	gridSize := len(lights)
	if cornersStayOn {
		lights[0][0] = true
		lights[0][gridSize-1] = true
		lights[gridSize-1][0] = true
		lights[gridSize-1][gridSize-1] = true
	}
	for i := 0; i < steps; i++ {
		nextLights := make([][]bool, gridSize)
		for y := 0; y < gridSize; y++ {
			nextLights[y] = make([]bool, gridSize)
			for x := 0; x < gridSize; x++ {
				neighborsOn := 0
				for dy := -1; dy <= 1; dy++ {
					for dx := -1; dx <= 1; dx++ {
						if dy == 0 && dx == 0 {
							continue
						}
						nx := x + dx
						ny := y + dy
						if nx >= 0 && nx < gridSize && ny >= 0 && ny < gridSize && lights[ny][nx] {
							neighborsOn++
						}
					}
				}
				nextLights[y][x] = (lights[y][x] && (neighborsOn == 2 || neighborsOn == 3)) || !lights[y][x] && neighborsOn == 3
			}
		}
		if cornersStayOn {
			nextLights[0][0] = true
			nextLights[0][gridSize-1] = true
			nextLights[gridSize-1][0] = true
			nextLights[gridSize-1][gridSize-1] = true
		}
		lights = nextLights
	}
	return s.sumLights(lights)
}

func (s Solver18) sumLights(lights [][]bool) int {
	sum := 0
	for _, row := range lights {
		for _, light := range row {
			if light {
				sum++
			}
		}
	}
	return sum
}

func (s Solver18) parseLights(data string) [][]bool {
	lines := strings.Split(strings.TrimSpace(data), "\n")
	gridSize := len(lines)
	lights := make([][]bool, gridSize)
	for j, line := range lines {
		lights[j] = make([]bool, gridSize)
		for i, c := range line {
			lights[j][i] = c == '#'
		}
	}
	return lights
}
