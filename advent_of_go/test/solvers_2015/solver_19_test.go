package solvers_2015

import (
	"github.com/stretchr/testify/suite"
	"testing"
	"will-martin.com/advent_of_go/src/solvers_2015"
)

type Solver19Test struct {
	suite.Suite
	sut *solvers_2015.Solver19
}

func TestSolver19(t *testing.T) {
	suite.Run(t, new(Solver19Test))
}

func (s *Solver19Test) SetupSuite() {
	s.sut = &solvers_2015.Solver19{}
}

func (s *Solver19Test) TestSolvePart1() {
	s.Equal(4, s.sut.SolvePart1(`H => HO
H => OH
O => HH

HOH`))
	s.Equal(7, s.sut.SolvePart1(`H => HO
H => OH
O => HH

HOHOHO`))
}

func (s *Solver19Test) TestSolvePart2() {
	s.Equal(3, s.sut.SolvePart2(`e => H
e => O
H => HO
H => OH
O => HH

HOH`))
	s.Equal(6, s.sut.SolvePart2(`e => H
e => O
H => HO
H => OH
O => HH

HOHOHO`))
}
