package solvers_2015

import (
	"github.com/ernestosuarez/itertools"
	"regexp"
	"strconv"
	"strings"
)

type Solver13 struct{}

var Solver13Regex = regexp.MustCompile(`^(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+).$`)

func (s *Solver13) SolvePart1(data string) int {
	nameToNameToGainMap := s.parseSeatingInformation(data)
	maxGain := s.findMaxGain(nameToNameToGainMap)
	return maxGain
}

func (s *Solver13) findMaxGain(nameToNameToGainMap map[string]map[string]int) int {
	keys := make([]string, 0, len(nameToNameToGainMap))
	for key := range nameToNameToGainMap {
		keys = append(keys, key)
	}
	maxGain := 0
	for combination := range itertools.PermutationsStr(keys, len(keys)) {
		gain := 0
		for i := 0; i < len(combination); i++ {
			name := combination[i]
			leftNeighbor := combination[(i+len(combination)-1)%len(combination)]
			rightNeighbor := combination[(i+1)%len(combination)]
			gain += nameToNameToGainMap[name][leftNeighbor] + nameToNameToGainMap[name][rightNeighbor]
		}
		if gain > maxGain {
			maxGain = gain
		}
	}
	return maxGain
}

func (s *Solver13) parseSeatingInformation(data string) map[string]map[string]int {
	nameToNameToGainMap := make(map[string]map[string]int)
	for _, line := range strings.Split(strings.TrimSpace(data), "\n") {
		if match := Solver13Regex.FindStringSubmatch(line); len(match) > 0 {
			name := match[1]
			gain, _ := strconv.Atoi(match[3])
			if match[2] == "lose" {
				gain *= -1
			}
			neighbor := match[4]
			if _, ok := nameToNameToGainMap[name]; !ok {
				nameToNameToGainMap[name] = make(map[string]int)
			}
			nameToNameToGainMap[name][neighbor] = gain
		}
	}
	return nameToNameToGainMap
}

func (s *Solver13) SolvePart2(data string) int {
	nameToNameToGainMap := s.parseSeatingInformation(data)
	nameToNameToGainMap["Me"] = make(map[string]int)
	for name := range nameToNameToGainMap {
		nameToNameToGainMap[name]["Me"] = 0
		nameToNameToGainMap["Me"][name] = 0
	}
	maxGain := s.findMaxGain(nameToNameToGainMap)
	return maxGain
}
