package solvers_2015

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestSolvePart1(t *testing.T) {
	assert.Equal(t, 0, SolvePart1("(())"))
	assert.Equal(t, 0, SolvePart1("()()"))
	assert.Equal(t, 3, SolvePart1("((("))
	assert.Equal(t, 3, SolvePart1("(()(()("))
	assert.Equal(t, 3, SolvePart1("))((((("))
	assert.Equal(t, -1, SolvePart1("())"))
	assert.Equal(t, -1, SolvePart1("))("))
	assert.Equal(t, -3, SolvePart1(")))"))
	assert.Equal(t, -3, SolvePart1(")())())"))
}

func TestSolvePart2(t *testing.T) {
	assert.Equal(t, 1, SolvePart2(")"))
	assert.Equal(t, 5, SolvePart2("()())"))
}
