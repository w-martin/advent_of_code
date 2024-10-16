package solvers_2015

import (
	"strings"
)

type Solver11 struct {
	digits        []uint8
	digitToAlpha  map[uint8]rune
	alphaToDigit  map[rune]uint8
	invalidDigits map[uint8]bool
}

func (s *Solver11) init() {
	solver11Alphabet := []rune("abcdefghijklmnopqrstuvwxyz")
	s.digitToAlpha = make(map[uint8]rune)
	s.alphaToDigit = make(map[rune]uint8)
	for i, r := range solver11Alphabet {
		u := uint8(i)
		s.digitToAlpha[u] = r
		s.alphaToDigit[r] = u
	}
	s.invalidDigits = make(map[uint8]bool)
	s.invalidDigits[s.alphaToDigit['i']] = true
	s.invalidDigits[s.alphaToDigit['o']] = true
	s.invalidDigits[s.alphaToDigit['l']] = true
}

func (s *Solver11) SolvePart1(data string) string {
	s.init()
	data = strings.TrimSpace(data)
	s.convertToDigits(data)
	s.increment()
	for !s.valid() {
		s.increment()
	}
	result := s.convertFromDigits()
	return result
}

func (s *Solver11) SolvePart2(data string) string {
	s.init()
	data = strings.TrimSpace(data)
	s.convertToDigits(data)
	s.increment()
	for !s.valid() {
		s.increment()
	}
	s.increment()
	for !s.valid() {
		s.increment()
	}
	result := s.convertFromDigits()
	return result
}

func (s *Solver11) convertToDigits(data string) {
	s.digits = make([]uint8, len(data))
	for i := len(data) - 1; i >= 0; i-- {
		s.digits[len(data)-i-1] = s.alphaToDigit[rune(data[i])]
	}
}

func (s *Solver11) convertFromDigits() string {
	sb := strings.Builder{}
	for i := len(s.digits) - 1; i >= 0; i-- {
		sb.WriteRune(s.digitToAlpha[s.digits[i]])
	}
	return sb.String()
}

func (s *Solver11) increment() {
	index := 0
	newValue := s.digits[index] + 1
	for newValue > 25 {
		s.digits[index] = 0
		index++
		if index > len(s.digits) {
			s.digits = append(s.digits, 0)
			return
		}
		newValue = s.digits[index] + 1
	}
	s.digits[index] = newValue
}

func (s *Solver11) valid() bool {
	hasIncreasingStraight := false
	hasTwoDifferentPairs := false
	pairs := make(map[uint8]bool)
	for i := 0; i < len(s.digits); i++ {
		if i >= 2 && s.digits[i]+1 == s.digits[i-1] && s.digits[i]+2 == s.digits[i-2] {
			hasIncreasingStraight = true
		}
		if s.invalidDigits[s.digits[i]] {
			return false
		}
		if i >= 1 && s.digits[i] == s.digits[i-1] && !pairs[s.digits[i]] {
			pairs[s.digits[i]] = true
		}
	}
	hasTwoDifferentPairs = len(pairs) >= 2
	return hasIncreasingStraight && hasTwoDifferentPairs
}
