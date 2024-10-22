package solvers_2015

import (
	"container/heap"
	"strconv"
	"strings"
)

type Solver21 struct{}
type Solver21ItemType int32

const (
	WEAPON Solver21ItemType = 0
	ARMOR  Solver21ItemType = 1
	RING   Solver21ItemType = 2
)

type Solver21Player struct {
	HitPoints int
	Damage    int
	Armor     int
}

type Solver21Item struct {
	Cost   int
	Damage int
	Armor  int
	Type   Solver21ItemType
}

var ShopItems = []Solver21Item{
	{8, 4, 0, WEAPON},
	{10, 5, 0, WEAPON},
	{25, 6, 0, WEAPON},
	{40, 7, 0, WEAPON},
	{74, 8, 0, WEAPON},
	{13, 0, 1, ARMOR},
	{31, 0, 2, ARMOR},
	{53, 0, 3, ARMOR},
	{75, 0, 4, ARMOR},
	{102, 0, 5, ARMOR},
	{25, 1, 0, RING},
	{50, 2, 0, RING},
	{100, 3, 0, RING},
	{20, 0, 1, RING},
	{40, 0, 2, RING},
	{80, 0, 3, RING},
}

type Solver21Option struct {
	items map[int]bool
	gold  int
	index int
}

type Solver21PriorityQueue []*Solver21Option

func (pq Solver21PriorityQueue) Len() int { return len(pq) }

func (pq Solver21PriorityQueue) Less(i, j int) bool {
	return pq[i].gold < pq[j].gold
}

func (pq Solver21PriorityQueue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
	pq[i].index = i
	pq[j].index = j
}

func (pq *Solver21PriorityQueue) Push(x any) {
	n := len(*pq)
	item := x.(*Solver21Option)
	item.index = n
	*pq = append(*pq, item)
}

func (pq *Solver21PriorityQueue) Pop() any {
	old := *pq
	n := len(old)
	item := old[n-1]
	item.index = -1
	*pq = old[0 : n-1]
	return item
}

func (s Solver21) SolvePart1(data string) int {
	boss := s.ParsePlayer(data)
	player := Solver21Player{
		HitPoints: 100,
		Damage:    0,
		Armor:     0,
	}
	q := make(Solver21PriorityQueue, 0)
	q = append(q, &Solver21Option{
		items: map[int]bool{},
		gold:  0,
		index: 0,
	})

	for len(q) > 0 {
		option := heap.Pop(&q).(*Solver21Option)
		weaponCount := 0
		armorCount := 0
		ringCount := 0
		for itemIndex := range option.items {
			item := ShopItems[itemIndex]
			switch item.Type {
			case WEAPON:
				weaponCount++
			case ARMOR:
				armorCount++
			case RING:
				ringCount++
			}
		}
		if weaponCount == 1 {
			playerDamage := 0
			playerArmor := 0
			for itemIndex := range option.items {
				item := ShopItems[itemIndex]
				playerDamage += item.Damage
				playerArmor += item.Armor
			}
			player.Damage = playerDamage
			player.Armor = playerArmor
			if s.PlayerWins(player, boss) {
				return option.gold
			}
		}
		for itemIndex, item := range ShopItems {
			if weaponCount == 1 && item.Type == WEAPON {
				continue
			}
			if armorCount == 1 && item.Type == ARMOR {
				continue
			}
			if ringCount == 2 && item.Type == RING {
				continue
			}
			if _, ok := option.items[itemIndex]; ok {
				continue
			}
			newItems := make(map[int]bool)
			for k, v := range option.items {
				newItems[k] = v
			}
			newItems[itemIndex] = true
			newGold := option.gold + item.Cost
			heap.Push(&q, &Solver21Option{
				items: newItems,
				gold:  newGold,
				index: 0,
			})
		}
	}
	return -1
}
func (s Solver21) SolvePart2(data string) int {
	boss := s.ParsePlayer(data)
	player := Solver21Player{
		HitPoints: 100,
		Damage:    0,
		Armor:     0,
	}
	q := make(Solver21PriorityQueue, 0)
	q = append(q, &Solver21Option{
		items: make(map[int]bool),
		gold:  0,
		index: 0,
	})
	mostGoldSpent := 0
	for len(q) > 0 {
		option := heap.Pop(&q).(*Solver21Option)
		weaponCount := 0
		armorCount := 0
		ringCount := 0
		for itemIndex := range option.items {
			item := ShopItems[itemIndex]
			switch item.Type {
			case WEAPON:
				weaponCount++
			case ARMOR:
				armorCount++
			case RING:
				ringCount++
			}
		}
		if weaponCount == 1 {
			playerDamage := 0
			playerArmor := 0
			for itemIndex := range option.items {
				item := ShopItems[itemIndex]
				playerDamage += item.Damage
				playerArmor += item.Armor
			}
			player.Damage = playerDamage
			player.Armor = playerArmor
			if !s.PlayerWins(player, boss) && option.gold > mostGoldSpent {
				mostGoldSpent = option.gold
			}
		}
		for itemIndex, item := range ShopItems {
			if weaponCount == 1 && item.Type == WEAPON {
				continue
			}
			if armorCount == 1 && item.Type == ARMOR {
				continue
			}
			if ringCount == 2 && item.Type == RING {
				continue
			}
			if _, ok := option.items[itemIndex]; ok {
				continue
			}
			newItems := make(map[int]bool)
			for k, v := range option.items {
				newItems[k] = v
			}
			newItems[itemIndex] = true
			newGold := option.gold + item.Cost
			heap.Push(&q, &Solver21Option{
				items: newItems,
				gold:  newGold,
				index: 0,
			})
		}
	}
	return mostGoldSpent
}

func (s Solver21) ParsePlayer(data string) Solver21Player {
	boss := Solver21Player{
		HitPoints: 0,
		Damage:    0,
		Armor:     0,
	}
	for lineNumber, line := range strings.Split(strings.TrimSpace(data), "\n") {
		switch lineNumber {
		case 0:
			parts := strings.Split(line, " ")
			value, _ := strconv.Atoi(parts[len(parts)-1])
			boss.HitPoints = value
		case 1:
			parts := strings.Split(line, " ")
			value, _ := strconv.Atoi(parts[len(parts)-1])
			boss.Damage = value
		case 2:
			parts := strings.Split(line, " ")
			value, _ := strconv.Atoi(parts[len(parts)-1])
			boss.Armor = value
		}
	}
	return boss
}

func (s Solver21) PlayerWins(player Solver21Player, boss Solver21Player) bool {
	playerDamage := player.Damage - boss.Armor
	if playerDamage < 1 {
		playerDamage = 1
	}
	bossDamage := boss.Damage - player.Armor
	if bossDamage < 1 {
		bossDamage = 1
	}
	playerTurns := boss.HitPoints / playerDamage
	if boss.HitPoints%playerDamage != 0 {
		playerTurns++
	}
	bossTurns := player.HitPoints / bossDamage
	if player.HitPoints%bossDamage != 0 {
		bossTurns++
	}
	playerWins := playerTurns <= bossTurns
	return playerWins
}
