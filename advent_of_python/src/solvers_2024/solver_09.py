from dataclasses import dataclass

from functional import seq

from solver import Solver


@dataclass
class Block:
    id: int
    location: int
    size: int

class SolverImpl(Solver):
    @staticmethod
    def _sum_block(block: Block) -> int:
        return sum(block.id * i for i in range(block.location, block.location + block.size))

    def solve_part_1(self, data: str) -> int:
        dense_block_list = seq(list(data.strip())).map(int).to_list()
        length = sum(dense_block_list)
        blocks = [None] * length
        blckid = 0
        index = 0
        for i in range(0, len(dense_block_list), 2):
            for j in range(index, index + dense_block_list[i]):
                blocks[j] = blckid
            index += sum(dense_block_list[i:i + 2])
            blckid += 1
        first_none_index = dense_block_list[0]
        for i in range(length - 1, dense_block_list[0] - 1, -1):
            if blocks[i] is not None:
                first_none_index = self._find_first_none_index(blocks, first_none_index)
                if first_none_index >= i:
                    break
                blocks[first_none_index] = blocks[i]
                blocks[i] = None
                first_none_index += 1
        first_none_index = self._find_first_none_index(blocks, dense_block_list[0])
        blocks = blocks[:first_none_index]
        result = seq(enumerate(blocks)).map(lambda iv: iv[0] * iv[1]).sum()
        return result

    def solve_part_2(self, data: str) -> int:
        dense_block_list = seq(list(data.strip())).map(int).to_list()
        length = sum(dense_block_list)
        s = 0
        blocks = {}
        spaces = {}
        for i in range(0, len(dense_block_list), 2):
            block_size = dense_block_list[i]
            blckid = i // 2
            blocks[blckid] = Block(size=block_size, location=s, id=blckid)
            s += block_size

            if i < len(dense_block_list) - 1:
                space_size = dense_block_list[i + 1]
                spaces[s] = space_size
                s += space_size
        # move end blocks
        for k in sorted(blocks.keys(), reverse=True):
            block = blocks[k]
            space_index = None
            space_size = None
            for space_key in sorted(spaces.keys()):
                if space_key > block.location:
                    break
                space_size_inner = spaces[space_key]
                if space_size_inner >= block.size:
                    space_index = space_key
                    space_size = space_size_inner
                    break
            if space_index is not None:
                block.location = space_index
                del spaces[space_index]
                new_space_size = space_size - block.size
                if new_space_size > 0:
                    new_space_index = space_index + block.size
                    spaces[new_space_index] = new_space_size

        return seq(blocks.values()).map(self._sum_block).sum()

    def _find_first_none_index(self, blocks, first_none_index):
        try:
            while blocks[first_none_index] is not None:
                first_none_index += 1
        except IndexError:
            ...
        return first_none_index

    def _find_first_free_block(self, blocks, free_block_index):
        try:
            while blocks[free_block_index] is not None:
                free_block_index += 1
        except IndexError:
            ...
        free_block_size = 1
        try:
            while blocks[free_block_index + free_block_size] is None:
                free_block_size += 1
        except IndexError:
            ...
        return free_block_index, free_block_size
