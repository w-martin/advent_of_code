package solvers_2015

import (
	"github.com/stretchr/testify/suite"
	"testing"
	"will-martin.com/advent_of_go/src/solvers_2015"
)

type Solver03Test struct {
	suite.Suite
	sut *solvers_2015.Solver03
}

func TestSolver03(t *testing.T) {
	suite.Run(t, new(Solver03Test))
}

func (s *Solver03Test) SetupSuite() {
	s.sut = &solvers_2015.Solver03{}
}

func (s *Solver03Test) TestSolvePart1() {
	s.Equal(2, s.sut.SolvePart1(">"))
	s.Equal(4, s.sut.SolvePart1("^>v<"))
	s.Equal(2, s.sut.SolvePart1("^v^v^v^v^v"))
}

func (s *Solver03Test) TestSolvePart2() {
	s.Equal(3, s.sut.SolvePart2("^v"))
	s.Equal(3, s.sut.SolvePart2("^>v<"))
	s.Equal(11, s.sut.SolvePart2("^v^v^v^v^v"))
}
