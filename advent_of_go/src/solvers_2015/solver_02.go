package solvers_2015

import (
	"fmt"
	"strconv"
	"strings"
)

type Solver02 struct{}

type Box struct {
	l, w, h int
}

func (b *Box) ToString() string {
	return fmt.Sprintf("Box{l: %d, w: %d, h: %d}", b.l, b.w, b.h)
}

func NewBox(parts []string) *Box {
	l, _ := strconv.Atoi(parts[0])
	w, _ := strconv.Atoi(parts[1])
	h, _ := strconv.Atoi(parts[2])
	box := Box{h: h, w: w, l: l}
	return &box
}

func (b *Box) Sides() *[3]int {
	return &[3]int{b.l * b.w, b.l * b.h, b.w * b.h}
}

func (b *Box) SurfaceArea() int {
	sides := b.Sides()
	return 2 * (sides[0] + sides[1] + sides[2])
}

func (b *Box) SmallestSide() int {
	sides := b.Sides()
	return min(sides[0], sides[1], sides[2])
}

func (b *Box) Volume() int {
	return b.w * b.l * b.h
}

func (b *Box) SmallestPerimeter() int {
	return 2 * min(b.w+b.l, b.w+b.h, b.l+b.h)
}

func (Solver02) SolvePart1(data string) int {
	total := 0
	for _, line := range strings.Split(data, "\n") {
		parts := strings.Split(line, "x")
		if len(parts) != 3 {
			continue
		}
		box := NewBox(parts)
		total += box.SurfaceArea() + box.SmallestSide()
	}
	return total
}

func (Solver02) SolvePart2(data string) int {
	total := 0
	for _, line := range strings.Split(data, "\n") {
		parts := strings.Split(line, "x")
		if len(parts) != 3 {
			continue
		}
		box := NewBox(parts)
		total += box.SmallestPerimeter() + box.Volume()
	}
	return total
}
