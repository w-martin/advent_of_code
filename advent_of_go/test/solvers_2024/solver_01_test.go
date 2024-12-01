package solvers_2024

import (
	"github.com/stretchr/testify/suite"
	"testing"
	"will-martin.com/advent_of_go/src/solvers_2024"
)

type Solver01Test struct {
	suite.Suite
	sut *solvers_2024.Solver01
}

func TestSolver01(t *testing.T) {
	suite.Run(t, new(Solver01Test))
}

func (s *Solver01Test) SetupSuite() {
	s.sut = &solvers_2024.Solver01{}
}

func (s *Solver01Test) TestSolver01Part1() {
	s.Equal(11, s.sut.SolvePart1(`
3   4
4   3
2   5
1   3
3   9
3   3`))
}

func (s *Solver01Test) TestSolver01Part2() {
	s.Equal(31, s.sut.SolvePart2(`
3   4
4   3
2   5
1   3
3   9
3   3`))
}
