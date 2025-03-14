"""
Game tasks for training reasoning capabilities:
- Board games
- Puzzle games
- Strategy games
- Simulation games
"""

from .countdown import CountdownConfig, CountdownDataset
from .emoji_mystery import EmojiMysteryConfig, EmojiMysteryCurriculum, EmojiMysteryDataset
from .futoshiki import FutoshikiConfig, FutoshikiDataset
from .knight_swap import KnightSwapConfig, KnightSwapDataset
from .mahjong import MahjongPuzzleConfig, MahjongPuzzleCurriculum, MahjongPuzzleDataset
from .maze import MazeConfig, MazeDataset
from .mini_sudoku import MiniSudokuConfig, MiniSudokuCurriculum, MiniSudokuDataset
from .n_queens import NQueensConfig, NQueensCurriculum, NQueensDataset
from .puzzle24 import Puzzle24Config, Puzzle24Dataset
from .rush_hour import RushHourConfig, RushHourDataset
from .sokoban import SokobanConfig, SokobanCurriculum, SokobanDataset
from .sudoku import SudokuConfig, SudokuDataset
from .tower_of_hanoi import HanoiConfig, HanoiDataset
from .tsumego import TsumegoConfig, TsumegoCurriculum, TsumegoDataset

__all__ = [
    "CountdownConfig",
    "CountdownDataset",
    "EmojiMysteryConfig",
    "EmojiMysteryCurriculum",
    "EmojiMysteryDataset",
    "FutoshikiConfig",
    "FutoshikiCurriculum",
    "FutoshikiDataset",
    "MiniSudokuConfig",
    "MiniSudokuDataset",
    "MiniSudokuCurriculum",
    "Puzzle24Config",
    "Puzzle24Dataset",
    "SudokuConfig",
    "SudokuDataset",
    "SokobanConfig",
    "SokobanCurriculum",
    "SokobanDataset",
    "RushHourConfig",
    "RushHourDataset",
    "MazeConfig",
    "MazeDataset",
    "HanoiConfig",
    "HanoiDataset",
    "NQueensDataset",
    "NQueensConfig",
    "NQueensCurriculum",
    "TsumegoConfig",
    "TsumegoCurriculum",
    "TsumegoDataset",
    "KnightSwapConfig",
    "KnightSwapDataset",
    "MahjongPuzzleConfig",
    "MahjongPuzzleDataset",
    "MahjongPuzzleCurriculum",
]
