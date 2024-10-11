package test

import (
	"github.com/stretchr/testify/suite"
	"testing"
	"will-martin.com/advent_of_go/src/solvers_2015"
)

type Solver02Test struct {
	suite.Suite
	sut *solvers_2015.Solver02
}

func TestSolver02(t *testing.T) {
	suite.Run(t, new(Solver02Test))
}

func (s *Solver02Test) SetupSuite() {
	s.sut = &solvers_2015.Solver02{}
}

func (s *Solver02Test) TestSolvePart1() {
	s.Equal(58, s.sut.SolvePart1("2x3x4"))
	s.Equal(43, s.sut.SolvePart1("1x1x10"))
}

func (s *Solver02Test) TestSolvePart2() {
	s.Equal(34, s.sut.SolvePart2("2x3x4"))
	s.Equal(14, s.sut.SolvePart2("1x1x10"))
}
