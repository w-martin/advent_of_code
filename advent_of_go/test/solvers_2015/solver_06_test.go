package solvers_2015

import (
	"github.com/stretchr/testify/suite"
	"testing"
	"will-martin.com/advent_of_go/src/solvers_2015"
)

type Solver06Test struct {
	suite.Suite
	sut *solvers_2015.Solver06
}

func TestSolver06(t *testing.T) {
	suite.Run(t, new(Solver06Test))
}

func (s *Solver06Test) SetupSuite() {
	s.sut = &solvers_2015.Solver06{}
}

func (s *Solver06Test) TestSolvePart1() {
	s.Equal(1_000_000, s.sut.SolvePart1("turn on 0,0 through 999,999"))
	s.Equal(1_000, s.sut.SolvePart1("toggle 0,0 through 999,0"))
	s.Equal(0, s.sut.SolvePart1("turn off 499,499 through 500,500"))
}

func (s *Solver06Test) TestSolvePart2() {
	s.Equal(1, s.sut.SolvePart2("turn on 0,0 through 0,0"))
	s.Equal(2_000_000, s.sut.SolvePart2("toggle 0,0 through 999,999"))
}
