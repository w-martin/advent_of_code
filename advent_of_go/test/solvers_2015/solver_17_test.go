package solvers_2015

import (
	"github.com/stretchr/testify/suite"
	"testing"
	"will-martin.com/advent_of_go/src/solvers_2015"
)

type Solver17Test struct {
	suite.Suite
	sut *solvers_2015.Solver17
}

func TestSolver17(t *testing.T) {
	suite.Run(t, new(Solver17Test))
}

func (s *Solver17Test) SetupSuite() {
	s.sut = &solvers_2015.Solver17{}
}

func (s *Solver17Test) TestSolvePart1() {
	s.Equal(4, s.sut.FindStorageCombinations(25, "20\n15\n10\n5\n5"))
}

func (s *Solver17Test) TestSolvePart2() {
	s.Equal(3, s.sut.FindMinimumStorageCombinations(25, "20\n15\n10\n5\n5"))
}
