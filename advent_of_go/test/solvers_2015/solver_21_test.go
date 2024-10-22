package solvers_2015

import (
	"github.com/stretchr/testify/suite"
	"testing"
	"will-martin.com/advent_of_go/src/solvers_2015"
)

type Solver21Test struct {
	suite.Suite
	sut *solvers_2015.Solver21
}

func TestSolver21(t *testing.T) {
	suite.Run(t, new(Solver21Test))
}

func (s *Solver21Test) SetupSuite() {
	s.sut = &solvers_2015.Solver21{}
}

func (s *Solver21Test) TestPlayerWins() {
	s.Equal(true, s.sut.PlayerWins(
		solvers_2015.Solver21Player{8, 5, 5},
		solvers_2015.Solver21Player{12, 7, 2}))
	s.Equal(false, s.sut.PlayerWins(
		solvers_2015.Solver21Player{8, 4, 5},
		solvers_2015.Solver21Player{12, 7, 2}))

}

func (s *Solver21Test) TestSolvePart2() {
	s.Equal(0, s.sut.SolvePart2(""))
}
