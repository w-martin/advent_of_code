package solvers_2015

import (
	"github.com/stretchr/testify/suite"
	"testing"
	"will-martin.com/advent_of_go/src/solvers_2015"
)

type Solver14Test struct {
	suite.Suite
	sut *solvers_2015.Solver14
}

func TestSolver14(t *testing.T) {
	suite.Run(t, new(Solver14Test))
}

func (s *Solver14Test) SetupSuite() {
	s.sut = &solvers_2015.Solver14{}
}

func (s *Solver14Test) TestSolvePart1() {
	s.Equal(1120, s.sut.DistanceAfter(1_000, `Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.`))
}

func (s *Solver14Test) TestSolvePart2() {
	s.Equal(689, s.sut.ScoreAfter(1_000, `Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.`))
}
