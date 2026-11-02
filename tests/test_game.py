import unittest
from game import new_game, move

class TestGame(unittest.TestCase):
    def test_new_game_defaults(self):
        p = new_game("Ada")
        self.assertEqual(p["location"], "Beach")
        self.assertEqual(p["energy"], 5)
        self.assertEqual(p["inventory"], [])

    def test_wrong_direction_costs_nothing(self):
        p = new_game("Ada")
        ok, _ = move(p, "north")
        self.assertFalse(ok)
        self.assertEqual(p["energy"], 5)

    def test_successful_move_costs_energy(self):
    p = new_game("Ada")

    ok, _ = move(p, "east")

    self.assertTrue(ok)

    self.assertEqual(p["energy"], 4)        

if __name__ == "__main__":
    unittest.main()