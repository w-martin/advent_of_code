package test

import (
	"github.com/stretchr/testify/suite"
	"testing"
	"will-martin.com/advent_of_go/src/solvers_2015"
)

type SolverTemplateTest struct {
	suite.Suite
	sut *solvers_2015.SolverTemplate
}

func TestSolverTemplate(t *testing.T) {
	suite.Run(t, new(SolverTemplateTest))
}

func (s *SolverTemplateTest) SetupSuite() {
	s.sut = &solvers_2015.SolverTemplate{}
}

func (s *SolverTemplateTest) TestSolvePart1() {
	s.Equal(0, s.sut.SolvePart1(""))
}

func (s *SolverTemplateTest) TestSolvePart2() {
	s.Equal(0, s.sut.SolvePart2(""))
}