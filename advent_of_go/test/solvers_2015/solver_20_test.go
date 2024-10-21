package solvers_2015

import (
	"github.com/stretchr/testify/suite"
	"testing"
	"will-martin.com/advent_of_go/src/solvers_2015"
)

type Solver20Test struct {
	suite.Suite
	sut *solvers_2015.Solver20
}

func TestSolver20(t *testing.T) {
	suite.Run(t, new(Solver20Test))
}

func (s *Solver20Test) SetupSuite() {
	s.sut = &solvers_2015.Solver20{}
}

func (s *Solver20Test) TestSolvePart1() {
	s.Equal(1, s.sut.SolvePart1(`10`))
	s.Equal(2, s.sut.SolvePart1(`30`))
	s.Equal(4, s.sut.SolvePart1(`70`))
	s.Equal(6, s.sut.SolvePart1(`120`))
	s.Equal(8, s.sut.SolvePart1(`150`))
}
