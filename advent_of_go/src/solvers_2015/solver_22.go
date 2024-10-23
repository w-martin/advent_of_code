package solvers_2015

import (
	"container/heap"
	"strconv"
	"strings"
)

type Solver22 struct{}

//`Hit Points: 58
//Damage: 9`

type Player struct {
	HitPoints int
	Mana      int
	Armor     int
	Damage    int
}
type Spell struct {
	Name     string
	Cost     int
	Duration int
	Cast     func(*Player, *Player)
	Effect   func(*Player, *Player)
	End      func(*Player, *Player)
}

var spells = []Spell{
	{
		Name: "Magic Missile",
		Cost: 53,
		Cast: func(caster, target *Player) {
			target.HitPoints -= 4
		},
		Duration: 1,
		End:      func(caster, target *Player) {},
		Effect:   func(caster, target *Player) {},
	},
	{
		Name: "Drain",
		Cost: 73,
		Cast: func(caster, target *Player) {
			target.HitPoints -= 2
			caster.HitPoints += 2
		},
		Duration: 1,
		End:      func(caster, target *Player) {},
		Effect:   func(caster, target *Player) {},
	},
	{
		Name: "Shield",
		Cost: 113,
		Cast: func(caster, target *Player) {
			caster.Armor += 7
		},
		Duration: 6,
		End: func(caster, target *Player) {
			caster.Armor -= 7
		},
		Effect: func(caster, target *Player) {},
	},
	{
		Name: "Poison",
		Cost: 173,
		Effect: func(caster, target *Player) {
			target.HitPoints -= 3
		},
		Duration: 6,
		End:      func(caster, target *Player) {},
		Cast:     func(caster, target *Player) {},
	},
	{
		Name: "Recharge",
		Cost: 229,
		Effect: func(caster, target *Player) {
			caster.Mana += 101
		},
		Duration: 5,
		End:      func(caster, target *Player) {},
		Cast:     func(caster, target *Player) {},
	},
}

type Solver22Option struct {
	player       Player
	boss         Player
	activeSpells map[int]int
	manaSpent    int
	index        int
}

type Solver22PriorityQueue []*Solver22Option

func (pq Solver22PriorityQueue) Len() int { return len(pq) }

func (pq Solver22PriorityQueue) Less(i, j int) bool {
	return pq[i].manaSpent < pq[j].manaSpent
}

func (pq Solver22PriorityQueue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
	pq[i].index = i
	pq[j].index = j
}

func (pq *Solver22PriorityQueue) Push(x any) {
	n := len(*pq)
	item := x.(*Solver22Option)
	item.index = n
	*pq = append(*pq, item)
}

func (pq *Solver22PriorityQueue) Pop() any {
	old := *pq
	n := len(old)
	item := old[n-1]
	item.index = -1
	*pq = old[0 : n-1]
	return item
}
func (s Solver22) SolvePart1(data string) int {
	bossHp, bossDamage := 0, 0
	for lineNumber, line := range strings.Split(strings.TrimSpace(data), "\n") {
		switch lineNumber {
		case 0:
			parts := strings.Split(line, " ")
			value, _ := strconv.Atoi(parts[len(parts)-1])
			bossHp = value
		case 1:
			parts := strings.Split(line, " ")
			value, _ := strconv.Atoi(parts[len(parts)-1])
			bossDamage = value
		}
	}
	player := Player{HitPoints: 50, Mana: 500, Armor: 0, Damage: 0}
	boss := Player{HitPoints: bossHp, Mana: 0, Armor: 0, Damage: bossDamage}

	q := make(Solver22PriorityQueue, 0)
	// player first turn
	for spellIndex, spell := range spells {
		if spell.Cost > player.Mana {
			continue
		}
		newPlayer := Player{
			HitPoints: player.HitPoints,
			Mana:      player.Mana - spell.Cost,
			Armor:     player.Armor,
			Damage:    player.Damage,
		}
		newBoss := Player{
			HitPoints: boss.HitPoints,
			Mana:      boss.Mana,
			Armor:     boss.Armor,
			Damage:    boss.Damage,
		}
		newActiveSpells := map[int]int{}
		newActiveSpells[spellIndex] = spell.Duration
		spell.Cast(&newPlayer, &newBoss)
		newOption := &Solver22Option{
			player:       newPlayer,
			boss:         newBoss,
			activeSpells: newActiveSpells,
			manaSpent:    spell.Cost,
			index:        0,
		}
		heap.Push(&q, newOption)
	}
	for len(q) > 0 {
		option := heap.Pop(&q).(*Solver22Option)
		// boss turn
		if option.boss.HitPoints <= 0 {
			return option.manaSpent
		}
		for activeSpellIndex := range option.activeSpells {
			spell := spells[activeSpellIndex]
			spell.Effect(&option.player, &option.boss)
			option.activeSpells[activeSpellIndex]--
			if option.activeSpells[activeSpellIndex] < 1 {
				spell.End(&option.player, &option.boss)
				delete(option.activeSpells, activeSpellIndex)
			}
		}
		if option.boss.HitPoints <= 0 {
			return option.manaSpent
		}
		option.player.HitPoints -= max(1, option.boss.Damage-option.player.Armor)
		if option.player.HitPoints <= 0 {
			continue
		}
		// player turn
		for activeSpellIndex := range option.activeSpells {
			spell := spells[activeSpellIndex]
			spell.Effect(&option.player, &option.boss)
			option.activeSpells[activeSpellIndex]--
			if option.activeSpells[activeSpellIndex] < 1 {
				spell.End(&option.player, &option.boss)
				delete(option.activeSpells, activeSpellIndex)
			}
		}
		for spellIndex, spell := range spells {
			if _, ok := option.activeSpells[spellIndex]; ok || spell.Cost > option.player.Mana {
				continue
			}
			newPlayer := Player{
				HitPoints: option.player.HitPoints,
				Mana:      option.player.Mana - spell.Cost,
				Armor:     option.player.Armor,
				Damage:    option.player.Damage,
			}
			newBoss := Player{
				HitPoints: option.boss.HitPoints,
				Mana:      option.boss.Mana,
				Armor:     option.boss.Armor,
				Damage:    option.boss.Damage,
			}
			newActiveSpells := map[int]int{}
			for k, v := range option.activeSpells {
				newActiveSpells[k] = v
			}
			newActiveSpells[spellIndex] = spell.Duration
			spell.Cast(&newPlayer, &newBoss)
			newOption := &Solver22Option{
				player:       newPlayer,
				boss:         newBoss,
				activeSpells: newActiveSpells,
				manaSpent:    option.manaSpent + spell.Cost,
				index:        0,
			}
			heap.Push(&q, newOption)
		}
	}
	return -1
}
func (s Solver22) SolvePart2(data string) int {
	bossHp, bossDamage := 0, 0
	for lineNumber, line := range strings.Split(strings.TrimSpace(data), "\n") {
		switch lineNumber {
		case 0:
			parts := strings.Split(line, " ")
			value, _ := strconv.Atoi(parts[len(parts)-1])
			bossHp = value
		case 1:
			parts := strings.Split(line, " ")
			value, _ := strconv.Atoi(parts[len(parts)-1])
			bossDamage = value
		}
	}
	player := Player{HitPoints: 50, Mana: 500, Armor: 0, Damage: 0}
	boss := Player{HitPoints: bossHp, Mana: 0, Armor: 0, Damage: bossDamage}

	q := make(Solver22PriorityQueue, 0)
	// player first turn
	for spellIndex, spell := range spells {
		if spell.Cost > player.Mana {
			continue
		}
		newPlayer := Player{
			HitPoints: player.HitPoints - 1,
			Mana:      player.Mana - spell.Cost,
			Armor:     player.Armor,
			Damage:    player.Damage,
		}
		if newPlayer.HitPoints <= 0 {
			continue
		}
		newBoss := Player{
			HitPoints: boss.HitPoints,
			Mana:      boss.Mana,
			Armor:     boss.Armor,
			Damage:    boss.Damage,
		}
		newActiveSpells := map[int]int{}
		newActiveSpells[spellIndex] = spell.Duration
		spell.Cast(&newPlayer, &newBoss)
		newOption := &Solver22Option{
			player:       newPlayer,
			boss:         newBoss,
			activeSpells: newActiveSpells,
			manaSpent:    spell.Cost,
			index:        0,
		}
		heap.Push(&q, newOption)
	}
	for len(q) > 0 {
		option := heap.Pop(&q).(*Solver22Option)
		// boss turn
		if option.boss.HitPoints <= 0 {
			return option.manaSpent
		}
		for activeSpellIndex := range option.activeSpells {
			spell := spells[activeSpellIndex]
			spell.Effect(&option.player, &option.boss)
			option.activeSpells[activeSpellIndex]--
			if option.activeSpells[activeSpellIndex] < 1 {
				spell.End(&option.player, &option.boss)
				delete(option.activeSpells, activeSpellIndex)
			}
		}
		if option.boss.HitPoints <= 0 {
			return option.manaSpent
		}
		option.player.HitPoints -= max(1, option.boss.Damage-option.player.Armor)
		if option.player.HitPoints <= 0 {
			continue
		}
		// player turn
		for activeSpellIndex := range option.activeSpells {
			spell := spells[activeSpellIndex]
			spell.Effect(&option.player, &option.boss)
			option.activeSpells[activeSpellIndex]--
			if option.activeSpells[activeSpellIndex] < 1 {
				spell.End(&option.player, &option.boss)
				delete(option.activeSpells, activeSpellIndex)
			}
		}
		for spellIndex, spell := range spells {
			if _, ok := option.activeSpells[spellIndex]; ok || spell.Cost > option.player.Mana {
				continue
			}
			newPlayer := Player{
				HitPoints: option.player.HitPoints - 1,
				Mana:      option.player.Mana - spell.Cost,
				Armor:     option.player.Armor,
				Damage:    option.player.Damage,
			}
			if newPlayer.HitPoints <= 0 {
				continue
			}
			newBoss := Player{
				HitPoints: option.boss.HitPoints,
				Mana:      option.boss.Mana,
				Armor:     option.boss.Armor,
				Damage:    option.boss.Damage,
			}
			newActiveSpells := map[int]int{}
			for k, v := range option.activeSpells {
				newActiveSpells[k] = v
			}
			newActiveSpells[spellIndex] = spell.Duration
			spell.Cast(&newPlayer, &newBoss)
			newOption := &Solver22Option{
				player:       newPlayer,
				boss:         newBoss,
				activeSpells: newActiveSpells,
				manaSpent:    option.manaSpent + spell.Cost,
				index:        0,
			}
			heap.Push(&q, newOption)
		}
	}
	return -1
}
