package solvers_2015

import (
	"slices"
	"strings"
)

type Solver05 struct {
}

const vowels = "aeiou"

var badStrings = []string{"ab", "cd", "pq", "xy"}

func (s *Solver05) isNicePart1(data string) bool {
	numVowels := 0
	doubleLetter := false
	for i, character := range strings.Split(data, "") {
		if i > 0 && character == data[i-1:i] {
			doubleLetter = true
		}
		if strings.Contains(vowels, character) {
			numVowels++
		}
		if i > 0 && slices.Contains(badStrings, data[i-1:i+1]) {
			return false
		}
	}
	threeVowels := numVowels >= 3
	if threeVowels && doubleLetter {
		return true
	}
	return false
}

type Solver05Pair struct {
	letters string
	indexes [2]int
}

func (p *Solver05Pair) EqualsWithoutOverlap(other *Solver05Pair) bool {
	return p.letters == other.letters && !(p.indexes[0] == other.indexes[0] || p.indexes[1] == other.indexes[1] || p.indexes[0] == other.indexes[1] || p.indexes[1] == other.indexes[0])
}

func (s *Solver05) isNicePart2(data string) bool {
	letterRepeatsWithOneLetterInBetween := false
	pairRepeatsWithoutOverlap := false
	var pairs []Solver05Pair
	for i := 0; i < len(data); i++ {
		if i > 0 {
			if i > 1 && data[i] == data[i-2] {
				letterRepeatsWithOneLetterInBetween = true
			}
			pair := Solver05Pair{letters: data[i-1 : i+1], indexes: [2]int{i - 1, i}}
			for _, otherPair := range pairs {
				if pair.EqualsWithoutOverlap(&otherPair) {
					pairRepeatsWithoutOverlap = true
				}
			}
			if letterRepeatsWithOneLetterInBetween && pairRepeatsWithoutOverlap {
				break
			}
			pairs = append(pairs, pair)
		}
	}
	return letterRepeatsWithOneLetterInBetween && pairRepeatsWithoutOverlap
}

func (s *Solver05) SolvePart1(data string) int {
	niceStrings := 0
	for _, line := range strings.Split(strings.TrimSpace(data), "\n") {
		if s.isNicePart1(line) {
			niceStrings++
		}
	}
	return niceStrings
}

func (s *Solver05) SolvePart2(data string) int {
	niceStrings := 0
	for _, line := range strings.Split(strings.TrimSpace(data), "\n") {
		if s.isNicePart2(line) {
			niceStrings++
		}
	}
	return niceStrings
}
