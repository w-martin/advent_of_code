package solvers_2015

import (
	"github.com/stretchr/testify/suite"
	"testing"
	"will-martin.com/advent_of_go/src/solvers_2015"
)

type Solver07Test struct {
	suite.Suite
	sut *solvers_2015.Solver07
}

func TestSolver07(t *testing.T) {
	suite.Run(t, new(Solver07Test))
}

func (s *Solver07Test) SetupSuite() {
	s.sut = &solvers_2015.Solver07{}
}

func (s *Solver07Test) TestSolvePart1() {
	data := `123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
`
	s.Equal(72, s.sut.SolvePart1("d\n"+data))
	s.Equal(507, s.sut.SolvePart1("e\n"+data))
	s.Equal(492, s.sut.SolvePart1("f\n"+data))
	s.Equal(114, s.sut.SolvePart1("g\n"+data))
	s.Equal(65412, s.sut.SolvePart1("h\n"+data))
	s.Equal(65079, s.sut.SolvePart1("i\n"+data))
	s.Equal(123, s.sut.SolvePart1("x\n"+data))
	s.Equal(456, s.sut.SolvePart1("y\n"+data))
}

func (s *Solver07Test) TestSolvePart2() {
	data := `
c OR b -> a
46066 -> c
9 -> b`
	s.Equal(46066, s.sut.SolvePart2("c\n"+data))
	s.Equal(46067, s.sut.SolvePart2("a\n"+data))
	s.Equal(46065, s.sut.SolvePart2("b\n"+data))
}
