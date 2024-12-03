package solvers_2024

import (
	"github.com/stretchr/testify/suite"
	"testing"
	"will-martin.com/advent_of_go/src/solvers_2024"
)

type Solver03Test struct {
	suite.Suite
	sut  *solvers_2024.Solver03
	data string
}

func TestSolver03(t *testing.T) {
	suite.Run(t, new(Solver03Test))
}

func (s *Solver03Test) SetupSuite() {
	s.sut = &solvers_2024.Solver03{}
}

func (s *Solver03Test) TestSolvePart1() {
	s.Equal(161, s.sut.SolvePart1("xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"))
}

func (s *Solver03Test) TestSolvePart2() {
	s.Equal(48, s.sut.SolvePart2("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"))
}
