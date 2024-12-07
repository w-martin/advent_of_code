package solvers_2024

import (
	"container/heap"
	"math"
	"strconv"
	"strings"
)

type Solver07 struct{}

type Solver07Option struct {
	parts      *[]int
	partsIndex int
	total      int
	index      int
}

type Solver07Test struct {
	parts *[]int
	value int
}

type Solver07PriorityQueue []*Solver07Option

func (pq Solver07PriorityQueue) Len() int { return len(pq) }

func (pq Solver07PriorityQueue) Less(i, j int) bool {
	return pq[i].partsIndex > pq[j].partsIndex
}

func (pq Solver07PriorityQueue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
	pq[i].index = i
	pq[j].index = j
}

func (pq *Solver07PriorityQueue) Push(x any) {
	n := len(*pq)
	item := x.(*Solver07Option)
	item.index = n
	*pq = append(*pq, item)
}

func (pq *Solver07PriorityQueue) Pop() any {
	old := *pq
	n := len(old)
	item := old[n-1]
	item.index = -1
	*pq = old[0 : n-1]
	return item
}

func (s *Solver07) SolvePart1(data string) int {
	total := 0
	for _, line := range strings.Split(strings.TrimSpace(data), "\n") {
		total += s.solveLine(line, false)
	}
	return total
}

func (s *Solver07) isValid(test *Solver07Test, includeConcatenation bool) bool {
	q := make(Solver07PriorityQueue, 0)
	q = append(q, &Solver07Option{
		partsIndex: 1,
		total:      (*test.parts)[0],
		parts:      test.parts,
		index:      0,
	})
	found := false
	for len(q) > 0 {
		option := heap.Pop(&q).(*Solver07Option)
		if len(*option.parts) == option.partsIndex {
			if option.total == test.value {
				found = true
				break
			} else {
				continue
			}
		}
		value := (*option.parts)[option.partsIndex]
		var newValue int
		// +
		newValue = option.total + value
		if newValue <= test.value {
			heap.Push(&q, &Solver07Option{
				parts:      option.parts,
				partsIndex: option.partsIndex + 1,
				total:      newValue,
			})
		}
		// *
		newValue = option.total * value
		if newValue <= test.value {
			heap.Push(&q, &Solver07Option{
				parts:      option.parts,
				partsIndex: option.partsIndex + 1,
				total:      newValue,
			})
		}
		// ||
		if includeConcatenation {
			newValue = s.Concat(option.total, value)
			if newValue <= test.value {
				heap.Push(&q, &Solver07Option{
					parts:      option.parts,
					partsIndex: option.partsIndex + 1,
					total:      newValue,
				})
			}
		}
	}
	return found
}

func (s *Solver07) parseLine(line string) *Solver07Test {
	separator := strings.Index(line, ":")
	testValue := s.mustAtoi(line[:separator])
	stringParts := strings.Split(line[separator+2:], " ")
	parts := make([]int, len(stringParts))
	for i, part := range stringParts {
		parts[i] = s.mustAtoi(part)
	}
	return &Solver07Test{
		parts: &parts,
		value: testValue,
	}
}

func (Solver07) mustAtoi(data string) int {
	value, err := strconv.Atoi(data)
	if err != nil {
		panic(err)
	}
	return value
}

func (s *Solver07) SolvePart2(data string) int {
	total := 0
	for _, line := range strings.Split(strings.TrimSpace(data), "\n") {
		total += s.solveLine(line, true)
	}
	return total
}

func (s *Solver07) Concat(a int, b int) int {
	result := b + a*int(math.Pow10(int(math.Ceil(math.Log10(float64(b))))))
	return result
}

func (s *Solver07) solveLine(line string, includeConcatenation bool) int {
	line = strings.TrimSpace(line)
	if len(line) == 0 {
		return 0
	}
	test := s.parseLine(line)
	found := s.isValid(test, includeConcatenation)

	if found {
		return test.value
	}
	return 0
}
