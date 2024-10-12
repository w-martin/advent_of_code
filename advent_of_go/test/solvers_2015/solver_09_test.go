package solvers_2015

import (
	"github.com/stretchr/testify/suite"
	"strings"
	"testing"
	"will-martin.com/advent_of_go/src/solvers_2015"
)

type Solver09Test struct {
	suite.Suite
	sut  *solvers_2015.Solver09
	data string
}

func TestSolver09(t *testing.T) {
	suite.Run(t, new(Solver09Test))
}

func (s *Solver09Test) SetupSuite() {
	s.sut = &solvers_2015.Solver09{}
	s.data = `London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141`
}

func (s *Solver09Test) TestSolvePart1() {
	s.Equal(605, s.sut.SolvePart1(strings.Clone(s.data)))
}

func (s *Solver09Test) TestSolvePart2() {
	s.Equal(982, s.sut.SolvePart2(strings.Clone(s.data)))
}
