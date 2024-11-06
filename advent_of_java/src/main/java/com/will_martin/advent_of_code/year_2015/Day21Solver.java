package com.will_martin.advent_of_code.year_2015;

import com.will_martin.advent_of_code.Solver;
import lombok.Value;
import lombok.val;

import java.util.*;

public class Day21Solver implements Solver {

    private static final List<Item> shopItems = List.of(
            new Item(8, 4, 0, ItemType.WEAPON),
            new Item(10, 5, 0, ItemType.WEAPON),
            new Item(25, 6, 0, ItemType.WEAPON),
            new Item(40, 7, 0, ItemType.WEAPON),
            new Item(74, 8, 0, ItemType.WEAPON),
            new Item(13, 0, 1, ItemType.ARMOR),
            new Item(31, 0, 2, ItemType.ARMOR),
            new Item(53, 0, 3, ItemType.ARMOR),
            new Item(75, 0, 4, ItemType.ARMOR),
            new Item(102, 0, 5, ItemType.ARMOR),
            new Item(25, 1, 0, ItemType.RING),
            new Item(50, 2, 0, ItemType.RING),
            new Item(100, 3, 0, ItemType.RING),
            new Item(20, 0, 1, ItemType.RING),
            new Item(40, 0, 2, ItemType.RING),
            new Item(80, 0, 3, ItemType.RING)
    );

    public boolean playerWins(int playerHp, final int playerDamage, final int playerArmor, int bossHp, final int bossDamage, final int bossArmor) {
        while (playerHp > 0 && bossHp > 0) {
            // player turn
            bossHp -= Math.max(1, playerDamage - bossArmor);
            if (bossHp <= 0) {
                break;
            }
            // boss turn
            playerHp -= Math.max(1, bossDamage - playerArmor);
        }
        return bossHp <= 0;
    }

    @Value
    private static class Item {
        int cost;
        int damage;
        int armor;
        ItemType type;
    }

    private enum ItemType {
        WEAPON,
        ARMOR,
        RING
    }

    @Value
    private static class Gear implements Comparable<Gear> {
        Set<Item> items;
        int goldSpent;

        @Override
        public int compareTo(Gear other) {
            return Integer.compare(goldSpent, other.getGoldSpent());
        }
    }

    @Override
    public String solvePart1(String data) {
        PlayerStats bossStats = getResult(data);

        var q = new PriorityQueue<Gear>();
        for (val item : shopItems) {
            if (item.type == ItemType.WEAPON) {
                q.add(new Gear(Set.of(item), item.cost));
            }
        }
        while (!q.isEmpty()) {
            val gear = q.poll();
            if (playerWins(100, gear.items.stream().mapToInt(item -> item.damage).sum(), gear.items.stream().mapToInt(item -> item.armor).sum(), bossStats.bossHp(), bossStats.bossDamage(), bossStats.bossArmor())) {
                return String.valueOf(gear.goldSpent);
            }
            for (val item : shopItems) {
                if (gear.items.contains(item)) {
                    continue;
                }
                if (item.type == ItemType.WEAPON) {
                    continue;
                }
                if (item.type == ItemType.ARMOR && gear.items.stream().anyMatch(i -> i.type == ItemType.ARMOR)) {
                    continue;
                }
                if (item.type == ItemType.RING && gear.items.stream().filter(i -> i.type == ItemType.RING).count() == 2) {
                    continue;
                }
                var newItems = new HashSet<>(gear.items);
                newItems.add(item);
                val newGear = new Gear(newItems, gear.goldSpent + item.cost);
                q.add(newGear);
            }
        }
        return String.valueOf(Integer.MAX_VALUE);
    }

    private static PlayerStats getResult(String data) {
        int bossHp = 0, bossDamage = 0, bossArmor = 0;
        for (final String line : data.trim().split("\n")) {
            val parts = line.split(" ");
            if (parts.length > 0) {
                val v = Integer.parseInt(parts[parts.length - 1]);
                if (0 == bossHp) {
                    bossHp = v;
                } else if (0 == bossDamage) {
                    bossDamage = v;
                } else {
                    bossArmor = v;
                }
            }
        }
        PlayerStats playerStats = new PlayerStats(bossHp, bossDamage, bossArmor);
        return playerStats;
    }

    private record PlayerStats(Integer bossHp, Integer bossDamage, Integer bossArmor) {
    }

    @Override
    public String solvePart2(String data) {
        PlayerStats bossStats = getResult(data);

        var q = new ArrayList<Gear>();
        for (val item : shopItems) {
            if (item.type == ItemType.WEAPON) {
                q.add(new Gear(Set.of(item), item.cost));
            }
        }
        int maxSpent = Integer.MIN_VALUE;
        while (!q.isEmpty()) {
            val gear = q.removeLast();
            if (!playerWins(100, gear.items.stream().mapToInt(item -> item.damage).sum(), gear.items.stream().mapToInt(item -> item.armor).sum(), bossStats.bossHp(), bossStats.bossDamage(), bossStats.bossArmor()) && (gear.goldSpent > maxSpent)) {
                maxSpent = gear.goldSpent;
            }
            for (val item : shopItems) {
                if (gear.items.contains(item)) {
                    continue;
                }
                if (item.type == ItemType.WEAPON) {
                    continue;
                }
                if (item.type == ItemType.ARMOR && gear.items.stream().anyMatch(i -> i.type == ItemType.ARMOR)) {
                    continue;
                }
                if (item.type == ItemType.RING && gear.items.stream().filter(i -> i.type == ItemType.RING).count() == 2) {
                    continue;
                }
                var newItems = new HashSet<>(gear.items);
                newItems.add(item);
                val newGear = new Gear(newItems, gear.goldSpent + item.cost);
                q.add(newGear);
            }
        }
        return String.valueOf(maxSpent);
    }
}
