package solvers_2015

import (
	"github.com/patrickmn/go-cache"
	"regexp"
	"strconv"
	"strings"
)

type Solver07 struct {
	circuit map[string]string
	cache   *cache.Cache
}

var transformationRegex = regexp.MustCompile("^(.*) -> (\\w+)$")

var initialiserRegex = regexp.MustCompile("^(\\d+)$")

var combinatorRegex = regexp.MustCompile("^(\\w+) (AND|OR) (\\w+)$")

var shifterRegex = regexp.MustCompile("^(\\w+) ([LR]SHIFT) (\\d+)$")

var noterRegex = regexp.MustCompile("^NOT (\\w+)$")

var reffRegex = regexp.MustCompile("^(\\w+)$")

func (s *Solver07) resolveCachedInstruction(instruction string) uint16 {
	result, found := s.cache.Get(instruction)
	if found {
		return result.(uint16)
	} else {
		result := s.resolveInstruction(instruction)
		s.cache.Set(instruction, result, cache.NoExpiration)
		return result
	}
}
func (s *Solver07) resolveInstruction(instruction string) uint16 {
	matchGroups := initialiserRegex.FindStringSubmatch(instruction)
	if matchGroups != nil {
		u64, _ := strconv.ParseUint(instruction, 10, 16)
		return uint16(u64)
	}
	matchGroups = combinatorRegex.FindStringSubmatch(instruction)
	if matchGroups != nil {
		a := s.resolveCachedInstruction(matchGroups[1])
		b := s.resolveCachedInstruction(matchGroups[3])
		switch matchGroups[2] {
		case "AND":
			return a & b
		case "OR":
			return a | b
		}
	}
	matchGroups = shifterRegex.FindStringSubmatch(instruction)
	if matchGroups != nil {
		a := s.resolveCachedInstruction(matchGroups[1])
		u64, _ := strconv.ParseUint(matchGroups[3], 10, 16)
		u16 := uint16(u64)
		switch matchGroups[2] {
		case "LSHIFT":
			return a << u16
		case "RSHIFT":
			return a >> u16
		}
	}
	matchGroups = noterRegex.FindStringSubmatch(instruction)
	if matchGroups != nil {
		a := s.resolveCachedInstruction(matchGroups[1])
		return ^a
	}
	matchGroups = reffRegex.FindStringSubmatch(instruction)
	if matchGroups != nil {
		return s.resolveCachedInstruction(s.circuit[matchGroups[1]])
	}
	return 0
}

func (s *Solver07) SolvePart1(data string) int {
	s.circuit = make(map[string]string)
	s.cache = cache.New(0, 0)
	target := s.parseData(data)
	return int(s.resolveCachedInstruction(target))
}

func (s *Solver07) parseData(data string) string {
	target := ""
	for _, line := range strings.Split(strings.TrimSpace(data), "\n") {
		if len(target) == 0 {
			target = strings.TrimSpace(line)
			continue
		}
		matchGroups := transformationRegex.FindStringSubmatch(line)
		if matchGroups != nil {
			s.circuit[matchGroups[2]] = matchGroups[1]
		}
	}
	return target
}

func (s *Solver07) SolvePart2(data string) int {
	s.circuit = make(map[string]string)
	s.cache = cache.New(0, 0)
	s.cache.Set("b", uint16(46065), cache.NoExpiration)
	target := s.parseData(data)
	return int(s.resolveCachedInstruction(target))
}
