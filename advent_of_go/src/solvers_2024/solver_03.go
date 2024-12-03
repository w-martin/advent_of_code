package solvers_2024

import (
	"regexp"
	"strconv"
)

type Solver03 struct {
	lastDo      int
	lastDont    int
	nextDo      int
	nextDont    int
	doIndexes   [][]int
	dontIndexes [][]int
}

var Solver03MulRegex = regexp.MustCompile(`mul\((?P<left>\d{1,3}),(?P<right>\d{1,3})\)`)
var Solver03DoRegex = regexp.MustCompile(`do\(\)`)
var Solver03DontRegex = regexp.MustCompile(`don't\(\)`)

func (s *Solver03) SolvePart1(data string) int {
	sum := 0
	for _, match := range Solver03MulRegex.FindAllStringSubmatch(data, -1) {
		sum += s.forceAtoi(match[1]) * s.forceAtoi(match[2])
	}
	return sum
}

func (Solver03) forceAtoi(data string) int {
	value, err := strconv.Atoi(data)
	if err != nil {
		panic(err)
	}
	return value
}

func (s *Solver03) SolvePart2(data string) int {
	sum := 0
	s.lastDont = -2
	s.lastDo = -1
	s.doIndexes = Solver03DoRegex.FindAllStringSubmatchIndex(data, -1)
	s.dontIndexes = Solver03DontRegex.FindAllStringSubmatchIndex(data, -1)
	s.setNextDont()
	s.setNextDo()
	mulIndexes := Solver03MulRegex.FindAllStringSubmatchIndex(data, -1)
	for _, matchIndex := range mulIndexes {
		if s.isEnabled(matchIndex[0]) {
			sum += s.forceAtoi(data[matchIndex[2]:matchIndex[3]]) * s.forceAtoi(data[matchIndex[4]:matchIndex[5]])
		}
	}
	return sum
}

func (s *Solver03) isEnabled(position int) bool {
	lastDont := s.lastDont
	for position > s.nextDont {
		lastDont = s.nextDont
		s.setNextDont()
		if s.nextDont == -2 {
			break
		}
	}
	if s.lastDont < lastDont {
		s.lastDont = lastDont
	}
	lastDo := s.lastDo
	for position > s.nextDo {
		lastDo = s.nextDo
		s.setNextDo()
		if s.nextDo == -1 {
			break
		}
	}
	if s.lastDo < lastDo {
		s.lastDo = lastDo
	}
	return s.lastDo > s.lastDont
}
func (s *Solver03) setNextDont() {
	if s.dontIndexes != nil {
		if s.nextDont = s.dontIndexes[0][0]; len(s.dontIndexes) > 1 {
			s.dontIndexes = s.dontIndexes[1:]
		} else {
			s.dontIndexes = nil
		}
	} else {
		s.nextDont = int(^uint(0) >> 1)
	}
}

func (s *Solver03) setNextDo() {
	if s.doIndexes != nil {
		if s.nextDo = s.doIndexes[0][0]; len(s.doIndexes) > 1 {
			s.doIndexes = s.doIndexes[1:]
		} else {
			s.doIndexes = nil
		}
	} else {
		s.nextDo = int(^uint(0) >> 1)
	}
}
