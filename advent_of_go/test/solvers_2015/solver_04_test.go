package solvers_2015

import (
	"github.com/stretchr/testify/suite"
	"testing"
	"will-martin.com/advent_of_go/src/solvers_2015"
)

type Solver04Test struct {
	suite.Suite
	sut *solvers_2015.Solver04
}

func TestSolver04(t *testing.T) {
	suite.Run(t, new(Solver04Test))
}

func (s *Solver04Test) SetupSuite() {
	s.sut = &solvers_2015.Solver04{}
}

func (s *Solver04Test) TestSolvePart1() {
	s.Equal(609043, s.sut.SolvePart1("abcdef"))
	s.Equal(1048970, s.sut.SolvePart1("pqrstuv"))
}
