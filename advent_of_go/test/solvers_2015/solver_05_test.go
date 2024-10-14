package solvers_2015

import (
	"github.com/stretchr/testify/suite"
	"testing"
	"will-martin.com/advent_of_go/src/solvers_2015"
)

type Solver05Test struct {
	suite.Suite
	sut *solvers_2015.Solver05
}

func TestSolver05(t *testing.T) {
	suite.Run(t, new(Solver05Test))
}

func (s *Solver05Test) SetupSuite() {
	s.sut = &solvers_2015.Solver05{}
}

func (s *Solver05Test) TestSolvePart1() {
	s.Equal(1, s.sut.SolvePart1("ugknbfddgicrmopn"))
	s.Equal(1, s.sut.SolvePart1("aaa"))
	s.Equal(0, s.sut.SolvePart1("jchzalrnumimnmhp"))
	s.Equal(0, s.sut.SolvePart1("haegwjzuvuyypxyu"))
	s.Equal(0, s.sut.SolvePart1("dvszwmarrgswjxmb"))
}

func (s *Solver05Test) TestSolvePart2() {
	s.Equal(1, s.sut.SolvePart2("qjhvhtzxzqqjkmpb"))
	s.Equal(1, s.sut.SolvePart2("xxyxx"))
	s.Equal(0, s.sut.SolvePart2("uurcxstgmygtbstg"))
	s.Equal(0, s.sut.SolvePart2("ieodomkazucvgmuy"))
}
