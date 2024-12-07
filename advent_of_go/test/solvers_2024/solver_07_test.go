package solvers_2024

import (
	"github.com/stretchr/testify/suite"
	"testing"
	"will-martin.com/advent_of_go/src/solvers_2024"
)

type Solver07Test struct {
	suite.Suite
	sut  *solvers_2024.Solver07
	data string
}

func TestSolver07(t *testing.T) {
	suite.Run(t, new(Solver07Test))
}

func (s *Solver07Test) SetupSuite() {
	s.sut = &solvers_2024.Solver07{}
	s.data = `
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20`
}

func (s *Solver07Test) TestSolvePart1() {
	s.Equal(3749, s.sut.SolvePart1(s.data))
}

func (s *Solver07Test) TestSolvePart2() {
	s.Equal(11387, s.sut.SolvePart2(s.data))
}

func (s *Solver07Test) TestConcat() {
	s.Equal(11387, s.sut.Concat(11, 387))
}
