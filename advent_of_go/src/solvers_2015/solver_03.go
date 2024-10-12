package solvers_2015

import "github.com/hashicorp/go-set/v3"

type Solver03 struct{}

type Solver03Location struct {
	X int
	Y int
}

func (Solver03) SolvePart1(data string) int {
	location := Solver03Location{0, 0}
	visited := set.From[Solver03Location]([]Solver03Location{location})
	for _, c := range data {
		switch c {
		case '^':
			location.Y++
		case 'v':
			location.Y--
		case '>':
			location.X++
		case '<':
			location.X--
		}
		visited.Insert(location)
	}
	return visited.Size()
}

func (Solver03) SolvePart2(data string) int {
	locations := []Solver03Location{{0, 0}, {0, 0}}
	visited := set.From[Solver03Location]([]Solver03Location{locations[0]})
	index := 0
	for _, c := range data {
		location := locations[index]
		switch c {
		case '^':
			location.Y++
		case 'v':
			location.Y--
		case '>':
			location.X++
		case '<':
			location.X--
		}
		visited.Insert(location)
		locations[index] = location
		index = 1 - index
	}
	return visited.Size()
}
