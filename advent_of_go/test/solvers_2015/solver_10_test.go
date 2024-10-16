package solvers_2015

import (
	"github.com/stretchr/testify/suite"
	"testing"
	"will-martin.com/advent_of_go/src/solvers_2015"
)

type Solver10Test struct {
	suite.Suite
	sut *solvers_2015.Solver10
}

func TestSolver10(t *testing.T) {
	suite.Run(t, new(Solver10Test))
}

func (s *Solver10Test) SetupSuite() {
	s.sut = &solvers_2015.Solver10{}
}

func (s *Solver10Test) TestSolvePart1() {
	s.Equal(2, s.sut.SolvePart1("1\n1"))
	s.Equal(2, s.sut.SolvePart1("2\n1"))
	s.Equal(4, s.sut.SolvePart1("3\n1"))
	s.Equal(6, s.sut.SolvePart1("4\n1"))
	s.Equal(6, s.sut.SolvePart1("5\n1"))
}
