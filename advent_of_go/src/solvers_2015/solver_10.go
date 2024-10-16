package solvers_2015

import (
	"fmt"
	"strconv"
	"strings"
)

type Solver10 struct {
	stringBuilder strings.Builder
}

func (s *Solver10) SolvePart1(data string) int {
	s.stringBuilder.Reset()
	data = strings.TrimSpace(data)
	dataParts := strings.Split(data, "\n")
	timesToRepeat := 40
	if len(dataParts) > 1 {
		timesToRepeat, _ = strconv.Atoi(dataParts[0])
		s.stringBuilder.WriteString(dataParts[1])
	} else {
		s.stringBuilder.WriteString(dataParts[0])
	}
	for timesToRepeat > 0 {
		s.ReadAloud()
		timesToRepeat--
	}
	return s.stringBuilder.Len()
}

func (s *Solver10) SolvePart2(data string) int {
	s.stringBuilder.Reset()
	data = strings.TrimSpace(data)
	dataParts := strings.Split(data, "\n")
	timesToRepeat := 50
	if len(dataParts) > 1 {
		timesToRepeat, _ = strconv.Atoi(dataParts[0])
		s.stringBuilder.WriteString(dataParts[1])
	} else {
		s.stringBuilder.WriteString(dataParts[0])
	}
	for timesToRepeat > 0 {
		s.ReadAloud()
		timesToRepeat--
	}
	return s.stringBuilder.Len()
}

func (s *Solver10) ReadAloud() {
	count := 0
	var last rune
	digits := s.stringBuilder.String()
	lastSize := s.stringBuilder.Len()
	s.stringBuilder.Reset()
	s.stringBuilder.Grow(lastSize)
	for _, c := range []rune(digits) {
		if c == last {
			count++
		} else {
			if count > 0 {
				s.stringBuilder.WriteString(fmt.Sprintf("%d%c", count, last))
			}
			last = c
			count = 1
		}
	}
	if count > 0 {
		s.stringBuilder.WriteString(fmt.Sprintf("%d%c", count, last))
	}
}
