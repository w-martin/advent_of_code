package solvers_2015

import (
	"bytes"
	"crypto/md5"
	"encoding/hex"
	"strconv"
	"strings"
)

type Solver04 struct{}

func (s *Solver04) SolvePart1(data string) int {
	return s.findSuffixForZeroesMd5(strings.TrimSpace(data), 5)
}

func (s *Solver04) findSuffixForZeroesMd5(data string, numStartingZeroes int) int {
	var buffer bytes.Buffer
	for i := 0; i < numStartingZeroes; i++ {
		buffer.WriteString("0")
	}
	match := buffer.String()

	i := 0
	for {
		dataWithSuffix := data + strconv.Itoa(i)
		hash := md5.Sum([]byte(dataWithSuffix))
		encoded := hex.EncodeToString(hash[:])
		if encoded[0:numStartingZeroes] == match {
			return i
		}
		i++
	}
}

func (s *Solver04) SolvePart2(data string) int {
	return s.findSuffixForZeroesMd5(strings.TrimSpace(data), 6)
}
