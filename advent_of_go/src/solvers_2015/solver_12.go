package solvers_2015

import (
	"encoding/json"
)

type Solver12 struct{}

type Solver12Map struct {
	L []interface{}
	M map[string]interface{}
}

func (s *Solver12) SolvePart1(data string) int {
	var f interface{}

	if err := json.Unmarshal([]byte(data), &f); err != nil {
		panic(err)
	}
	return s.jsonSum1(f)
}

func (s *Solver12) jsonSum1(f interface{}) int {
	sum := 0
	switch v := f.(type) {
	case []interface{}:
		for _, fi := range f.([]interface{}) {
			sum += s.jsonSum1(fi)
		}
	case map[string]interface{}:
		m := f.(map[string]interface{})
		for _, v := range m {
			sum += s.jsonSum1(v)
		}
	case float64:
		sum += int(v)
	}
	return sum
}
func (s *Solver12) jsonSum2(f interface{}) int {
	sum := 0
	red := false
	switch v := f.(type) {
	case []interface{}:
		for _, v := range f.([]interface{}) {
			sum += s.jsonSum2(v)
		}
	case map[string]interface{}:
		m := f.(map[string]interface{})
		for _, v := range m {
			if v == "red" {
				red = true
				break
			} else {
				sum += s.jsonSum2(v)
			}
		}
	case float64:
		sum += int(v)
	}
	if red {
		return 0
	}
	return sum
}

func (s *Solver12) SolvePart2(data string) int {
	var f interface{}

	if err := json.Unmarshal([]byte(data), &f); err != nil {
		panic(err)
	}
	return s.jsonSum2(f)
}
