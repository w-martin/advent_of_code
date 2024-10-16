package solvers_2015

import (
	"github.com/stretchr/testify/suite"
	"testing"
	"will-martin.com/advent_of_go/src/solvers_2015"
)

type Solver08Test struct {
	suite.Suite
	sut *solvers_2015.Solver08
}

func TestSolver08(t *testing.T) {
	suite.Run(t, new(Solver08Test))
}

func (s *Solver08Test) SetupSuite() {
	s.sut = &solvers_2015.Solver08{}
}

func (s *Solver08Test) TestSolvePart1() {
	s.Equal(2, s.sut.SolvePart1(`""`))
	s.Equal(2, s.sut.SolvePart1(`"abc"`))
	s.Equal(3, s.sut.SolvePart1(`"aaa\"aaa"`))
	s.Equal(5, s.sut.SolvePart1(`"\x27"`))
	s.Equal(12, s.sut.SolvePart1(`

""
"abc"
"aaa\"aaa"
"\x27"`))
}

func (s *Solver08Test) TestSolvePart2() {
	s.Equal(4, s.sut.SolvePart2(`""`))
	s.Equal(4, s.sut.SolvePart2(`"abc"`))
	s.Equal(6, s.sut.SolvePart2(`"aaa\"aaa"`))
	s.Equal(5, s.sut.SolvePart2(`"\x27"`))
	s.Equal(19, s.sut.SolvePart2(`

""
"abc"
"aaa\"aaa"
"\x27"`))
}
