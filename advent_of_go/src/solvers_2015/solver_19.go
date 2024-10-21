package solvers_2015

import (
	"container/heap"
	"strings"
)

type Solver19 struct {
	replacements map[string][]string
	molecule     string
}

var Solver19MaxInt = int(^uint(0) >> 1)

type Solver19Option struct {
	molecule        string
	numReplacements int
	index           int
}

type Solver19PriorityQueue []*Solver19Option

func (pq Solver19PriorityQueue) Len() int { return len(pq) }

func (pq Solver19PriorityQueue) Less(i, j int) bool {
	return pq[i].numReplacements < pq[j].numReplacements
}

func (pq Solver19PriorityQueue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
	pq[i].index = i
	pq[j].index = j
}

func (pq *Solver19PriorityQueue) Push(x any) {
	n := len(*pq)
	item := x.(*Solver19Option)
	item.index = n
	*pq = append(*pq, item)
}

func (pq *Solver19PriorityQueue) Pop() any {
	old := *pq
	n := len(old)
	item := old[n-1]
	item.index = -1
	*pq = old[0 : n-1]
	return item
}

func (pq *Solver19PriorityQueue) update(item *Solver19Option, distance int) {
	item.numReplacements = distance
	heap.Fix(pq, item.index)
}

func (s *Solver19) SolvePart1(data string) int {
	s.parseReplacements(data)
	molecules := map[string]bool{}
	for key, values := range s.replacements {
		keyLen := len(key)
		index := strings.Index(s.molecule, key)
		for 0 <= index && index < len(s.molecule) {
			nextIndexStart := index + keyLen
			for _, value := range values {
				newMolecule := (s.molecule)[:index] + value + (s.molecule)[nextIndexStart:]
				molecules[newMolecule] = true
			}
			index = strings.Index((s.molecule)[nextIndexStart:], key)
			if index != -1 {
				index += nextIndexStart
			}
		}
	}
	return len(molecules)
}

func (s *Solver19) parseReplacements(data string) {
	s.replacements = map[string][]string{}
	lines := strings.Split(strings.TrimSpace(data), "\n")
	for i, line := range lines {
		if i == len(lines)-1 {
			s.molecule = line
		} else {
			parts := strings.Split(line, " => ")
			for i, part := range parts {
				parts[i] = strings.TrimSpace(part)
			}
			if len(parts) > 1 {
				if _, ok := (s.replacements)[parts[0]]; !ok {
					(s.replacements)[parts[0]] = []string{}
				}
				(s.replacements)[parts[0]] = append((s.replacements)[parts[0]], parts[1])
			}
		}
	}
}

func (s *Solver19) SolvePart2(data string) int {
	s.parseReplacements(data)
	return s.findMinimumReplacement("e")
}

func (s *Solver19) findMinimumReplacement(currentString string) int {

	q := make(Solver19PriorityQueue, 0)
	q = append(q, &Solver19Option{
		molecule:        s.molecule,
		numReplacements: 0,
		index:           0,
	})
	visited := make(map[string]int)
	visited[s.molecule] = 0

	for len(q) > 0 {
		option := heap.Pop(&q).(*Solver19Option)
		if option.molecule == (currentString) {
			return option.numReplacements
		}
		newNumReplacements := option.numReplacements + 1
		for key, values := range s.replacements {
			for _, value := range values {
				keyLen := len(value)
				index := strings.Index(option.molecule, value)
				for 0 <= index && index < len(option.molecule) {
					nextIndexStart := index + keyLen
					newMolecule := option.molecule[:index] + key
					if nextIndexStart < len(option.molecule) {
						newMolecule += option.molecule[nextIndexStart:]
					}
					if oldNumReplacements, ok := visited[newMolecule]; !ok || newNumReplacements < oldNumReplacements {
						heap.Push(&q, &Solver19Option{
							molecule:        newMolecule,
							numReplacements: newNumReplacements,
							index:           0,
						})
						visited[newMolecule] = newNumReplacements
					}
					if nextIndexStart < len(option.molecule) {
						index = strings.Index(option.molecule[nextIndexStart:], key)
						if index != -1 {
							index += nextIndexStart
						}
					} else {
						index = -1
					}
				}
			}
		}
	}
	return Solver19MaxInt
}
