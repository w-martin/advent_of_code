package solvers_2024

import (
	"math"
	"sort"
	"strconv"
	"strings"
)

type Solver01 struct{}

func (s Solver01) SolvePart1(data string) int {
	l, r := s.parseData(data)
	ls, rs := l[:], r[:]
	sort.Ints(ls)
	sort.Ints(rs)
	sum := 0.
	for i := 0; i < 1000; i++ {
		sum += math.Abs(float64(ls[i] - rs[i]))
	}
	return int(sum)
}

func (s Solver01) parseData(data string) ([1000]int, [1000]int) {
	var l, r [1000]int
	i := 0
	for _, line := range strings.Split(strings.TrimSpace(data), "\n") {
		parts := strings.Fields(line)
		if len(parts) < 2 {
			continue
		}
		if len(parts) > 2 {
			panic("Too many parts in line")
		}
		l[i] = s.forceAtoi(parts[0])
		r[i] = s.forceAtoi(parts[1])
		i++
	}
	return l, r
}

func (Solver01) forceAtoi(data string) int {
	value, err := strconv.Atoi(data)
	if err != nil {
		panic(err)
	}
	return value
}

func (Solver01) applyCounter(data [1000]int) map[int]int {
	result := make(map[int]int)
	for _, v := range data {
		result[v]++
	}
	return result
}

func (s Solver01) SolvePart2(data string) int {
	l, r := s.parseData(data)
	rCounter := s.applyCounter(r)
	similarity := 0
	for _, leftValue := range l {
		rightCount, ok := rCounter[leftValue]
		if ok {
			similarity += leftValue * rightCount
		}
	}
	return similarity
}
