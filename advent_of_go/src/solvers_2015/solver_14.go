package solvers_2015

import (
	"regexp"
	"slices"
	"strconv"
	"strings"
)

type Solver14 struct{}

var Solver14DistanceAfterRegex = regexp.MustCompile(`^(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.$`)

type Solver14Flier struct {
	name       string
	speed      int
	flightTime int
	restTime   int
}

func (s *Solver14) SolvePart1(data string) int {
	return s.DistanceAfter(2503, data)
}

func (s *Solver14) SolvePart2(data string) int {
	return s.ScoreAfter(2503, data)
}

func (s *Solver14) DistanceAfter(maxTime int, data string) int {
	fliers := s.parseFliers(data)
	maxTravelled := 0
	for _, flier := range fliers {
		intervalTime := flier.flightTime + flier.restTime
		numFlights := maxTime / intervalTime
		travelled := flier.speed * flier.flightTime * numFlights
		remainder := maxTime - (numFlights * intervalTime)
		travelled += flier.speed * min(remainder, flier.flightTime)
		if travelled > maxTravelled {
			maxTravelled = travelled
		}
	}
	return maxTravelled
}

func (s *Solver14) parseFliers(data string) []Solver14Flier {
	fliers := make([]Solver14Flier, 0)
	for _, line := range strings.Split(strings.TrimSpace(data), "\n") {
		if match := Solver14DistanceAfterRegex.FindStringSubmatch(line); len(match) > 0 {
			speed, _ := strconv.Atoi(match[2])
			flightTime, _ := strconv.Atoi(match[3])
			restTime, _ := strconv.Atoi(match[4])
			fliers = append(fliers, Solver14Flier{
				name:       match[1],
				speed:      speed,
				flightTime: flightTime,
				restTime:   restTime,
			})
		}
	}
	return fliers
}

func (s *Solver14) ScoreAfter(maxTime int, data string) int {
	fliers := s.parseFliers(data)
	distances := make([]int, len(fliers))
	restingUntil := make([]int, len(fliers))
	flyingUntil := make([]int, len(fliers))
	scores := make([]int, len(fliers))
	for i, flier := range fliers {
		flyingUntil[i] = flier.flightTime
	}
	for time := 0; time <= maxTime; time++ {
		for i, flier := range fliers {
			if restingUntil[i] == time {
				flyingUntil[i] = time + flier.flightTime
			}
			if flyingUntil[i] > time {
				distances[i] += flier.speed
			} else if flyingUntil[i] == time {
				restingUntil[i] = time + flier.restTime
			}
		}
		maxDistance := slices.Max(distances)
		for i := range distances {
			if distances[i] == maxDistance {
				scores[i]++
			}
		}
	}
	return slices.Max(scores)
}
