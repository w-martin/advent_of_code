package solvers_2015

import (
	"github.com/stretchr/testify/suite"
	"testing"
	"will-martin.com/advent_of_go/src/solvers_2015"
)

type Solver18Test struct {
	suite.Suite
	sut *solvers_2015.Solver18
}

func TestSolver18(t *testing.T) {
	suite.Run(t, new(Solver18Test))
}

func (s *Solver18Test) SetupSuite() {
	s.sut = &solvers_2015.Solver18{}
}

func (s *Solver18Test) TestSolvePart1() {
	s.Equal(4, s.sut.FindHowManyLightsOnAfter(4, `.#.#.#
...##.
#....#
..#...
#.#..#
####..`, false))
}

func (s *Solver18Test) TestSolvePart2() {
	s.Equal(17, s.sut.FindHowManyLightsOnAfter(5, `.#.#.#
...##.
#....#
..#...
#.#..#
####..`, true))
}
