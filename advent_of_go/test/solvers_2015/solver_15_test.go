package solvers_2015

import (
	"github.com/stretchr/testify/suite"
	"testing"
	"will-martin.com/advent_of_go/src/solvers_2015"
)

type Solver15Test struct {
	suite.Suite
	sut *solvers_2015.Solver15
}

func TestSolver15(t *testing.T) {
	suite.Run(t, new(Solver15Test))
}

func (s *Solver15Test) SetupSuite() {
	s.sut = &solvers_2015.Solver15{}
}

func (s *Solver15Test) TestSolvePart1() {
	s.Equal(62842880, s.sut.SolvePart1(`Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
`))
}

func (s *Solver15Test) TestSolvePart2() {
	s.Equal(57600000, s.sut.SolvePart2(`Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
`))
}
