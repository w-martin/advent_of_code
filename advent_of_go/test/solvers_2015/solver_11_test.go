package solvers_2015

import (
	"github.com/stretchr/testify/suite"
	"testing"
	"will-martin.com/advent_of_go/src/solvers_2015"
)

type Solver11Test struct {
	suite.Suite
	sut *solvers_2015.Solver11
}

func TestSolver11(t *testing.T) {
	suite.Run(t, new(Solver11Test))
}

func (s *Solver11Test) SetupSuite() {
	s.sut = &solvers_2015.Solver11{}
}

func (s *Solver11Test) TestSolvePart1() {
	s.Equal("abcdffaa", s.sut.SolvePart1("abcdefgh"))
	s.Equal("ghjaabcc", s.sut.SolvePart1("ghijklmn"))
}
