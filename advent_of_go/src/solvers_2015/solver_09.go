package solvers_2015

import (
	"container/heap"
	"slices"
	"strconv"
	"strings"
)

type Solver09Neighbour struct {
	name     string
	distance int
}

type Solver09Option struct {
	visited  []string
	distance int
	index    int
}

type Solver09PriorityQueue []*Solver09Option

func (pq Solver09PriorityQueue) Len() int { return len(pq) }

func (pq Solver09PriorityQueue) Less(i, j int) bool {
	return pq[i].distance < pq[j].distance
}

func (pq Solver09PriorityQueue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
	pq[i].index = i
	pq[j].index = j
}

func (pq *Solver09PriorityQueue) Push(x any) {
	n := len(*pq)
	item := x.(*Solver09Option)
	item.index = n
	*pq = append(*pq, item)
}

func (pq *Solver09PriorityQueue) Pop() any {
	old := *pq
	n := len(old)
	item := old[n-1]
	item.index = -1
	*pq = old[0 : n-1]
	return item
}

func (pq *Solver09PriorityQueue) update(item *Solver09Option, distance int) {
	item.distance = distance
	heap.Fix(pq, item.index)
}

type Solver09 struct{}

func (Solver09) ParseGraph(data string) *map[string][]Solver09Neighbour {
	graph := make(map[string][]Solver09Neighbour)
	for _, line := range strings.Split(data, "\n") {
		parts := strings.Split(line, " ")
		if len(parts) != 5 {
			continue
		}
		distance, _ := strconv.Atoi(parts[4])
		if _, ok := graph[parts[0]]; !ok {
			graph[parts[0]] = []Solver09Neighbour{}
		}
		if _, ok := graph[parts[2]]; !ok {
			graph[parts[2]] = []Solver09Neighbour{}
		}
		graph[parts[0]] = append(graph[parts[0]], Solver09Neighbour{parts[2], distance})
		graph[parts[2]] = append(graph[parts[2]], Solver09Neighbour{parts[0], distance})
	}
	return &graph
}

func (solver *Solver09) SolvePart1(data string) int {
	graph := *solver.ParseGraph(data)
	q := make(Solver09PriorityQueue, 0)
	for k := range graph {
		q = append(q, &Solver09Option{[]string{k}, 0, 0})
	}
	for len(q) > 0 {
		option := heap.Pop(&q).(*Solver09Option)
		if len(option.visited) == len(graph) {
			return option.distance
		}
		head := option.visited[len(option.visited)-1]
		for _, neighbour := range graph[head] {
			if !slices.Contains(option.visited, neighbour.name) {
				heap.Push(&q, &Solver09Option{append(slices.Clone(option.visited), neighbour.name), option.distance + neighbour.distance, 0})
			}
		}
	}
	return -1
}

func (solver *Solver09) SolvePart2(data string) int {
	graph := *solver.ParseGraph(data)
	q := make(Solver09PriorityQueue, 0)
	for k := range graph {
		q = append(q, &Solver09Option{[]string{k}, 0, 0})
	}
	result := 0
	for len(q) > 0 {
		option := heap.Pop(&q).(*Solver09Option)
		if len(option.visited) == len(graph) {
			result = min(result, option.distance)
		}
		head := option.visited[len(option.visited)-1]
		for _, neighbour := range graph[head] {
			if !slices.Contains(option.visited, neighbour.name) {
				heap.Push(&q, &Solver09Option{append(slices.Clone(option.visited), neighbour.name), option.distance - neighbour.distance, 0})
			}
		}
	}
	return -result
}
