package solvers_2015

import (
	"github.com/stretchr/testify/suite"
	"testing"
	"will-martin.com/advent_of_go/src/solvers_2015"
)

type Solver01Test struct {
	suite.Suite
	sut *solvers_2015.Solver01
}

func TestSolver01(t *testing.T) {
	suite.Run(t, new(Solver01Test))
}

func (s *Solver01Test) SetupSuite() {
	s.sut = &solvers_2015.Solver01{}
}

func (s *Solver01Test) TestSolver01Part1() {
	s.Equal(0, s.sut.SolvePart1("(())"))
	s.Equal(0, s.sut.SolvePart1("()()"))
	s.Equal(3, s.sut.SolvePart1("((("))
	s.Equal(3, s.sut.SolvePart1("(()(()("))
	s.Equal(3, s.sut.SolvePart1("))((((("))
	s.Equal(-1, s.sut.SolvePart1("())"))
	s.Equal(-1, s.sut.SolvePart1("))("))
	s.Equal(-3, s.sut.SolvePart1(")))"))
	s.Equal(-3, s.sut.SolvePart1(")())())"))
}

func (s *Solver01Test) TestSolver01Part2() {
	s.Equal(1, s.sut.SolvePart2(")"))
	s.Equal(5, s.sut.SolvePart2("()())"))
}
