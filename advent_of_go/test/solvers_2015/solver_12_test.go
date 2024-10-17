package solvers_2015

import (
	"github.com/stretchr/testify/suite"
	"testing"
	"will-martin.com/advent_of_go/src/solvers_2015"
)

type Solver12Test struct {
	suite.Suite
	sut *solvers_2015.Solver12
}

func TestSolver12(t *testing.T) {
	suite.Run(t, new(Solver12Test))
}

func (s *Solver12Test) SetupSuite() {
	s.sut = &solvers_2015.Solver12{}
}

func (s *Solver12Test) TestSolvePart1() {
	s.Equal(6, s.sut.SolvePart1(`[1,2,3]`))
	s.Equal(6, s.sut.SolvePart1(`{"a":2,"b":4}`))
	s.Equal(3, s.sut.SolvePart1(`[[[3]]]`))
	s.Equal(3, s.sut.SolvePart1(`{"a":{"b":4},"c":-1}`))
	s.Equal(0, s.sut.SolvePart1(`{"a":[-1,1]}`))
	s.Equal(0, s.sut.SolvePart1(`[-1,{"a":1}]`))
	s.Equal(0, s.sut.SolvePart1(`[]`))
	s.Equal(0, s.sut.SolvePart1(`{}`))
}

func (s *Solver12Test) TestSolvePart2() {
	s.Equal(6, s.sut.SolvePart2(`[1,2,3]`))
	s.Equal(4, s.sut.SolvePart2(`[1,{"c":"red","b":2},3]`))
	s.Equal(0, s.sut.SolvePart2(`{"d":"red","e":[1,2,3,4],"f":5}`))
	s.Equal(6, s.sut.SolvePart2(`[1,"red",5]`))
}
