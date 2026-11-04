import unittest
from game import new_game, move, collect_item, light_lighthouse
from copy import deepcopy

class TestGame(unittest.TestCase):

    def test_new_game_defaults(self):
        p = new_game("Ada")

        self.assertEqual(p["location"], "Beach")
        self.assertEqual(p["energy"], 5)
        self.assertEqual(p["inventory"], [])

    def test_game_ends_when_energy_reaches_zero(self):
        p = new_game("Ada")
        p["energy"] = 1

        ok, message = move(p, "jungle")

        self.assertTrue(ok)
        self.assertEqual(p["energy"], 0)
        self.assertTrue(p["game_over"])

    def test_cannot_cross_bridge_without_rope(self):
        p = new_game("Ada")
        p["location"] = "Cave"

        ok, message = move(p, "bridge")

        self.assertFalse(ok)
        self.assertEqual(p["location"], "Cave")

    def test_can_cross_bridge_with_rope(self):
        p = new_game("Ada")
        p["location"] = "Cave"
        p["inventory"].append("rope")

        ok, message = move(p, "bridge")

        self.assertTrue(ok)
        self.assertEqual(p["location"], "Old Bridge")
        self.assertEqual(p["energy"], 4)

    def test_wrong_direction_costs_nothing(self):
        p = new_game("Ada")

        ok, message = move(p, "north")

        self.assertFalse(ok)
        self.assertEqual(p["energy"], 5)

    def test_successful_move_costs_energy(self):
        p = new_game("Ada")

        ok, message = move(p, "jungle")

        self.assertTrue(ok)
        self.assertEqual(p["energy"], 4)

    def test_collect_rope_in_jungle(self):
        p = new_game("Ada")
        p["location"] = "Jungle"

        ok, message = collect_item(p)

        self.assertTrue(ok)
        self.assertIn("rope", p["inventory"])

    def test_cannot_collect_item_twice(self):
        p = new_game("Ada")
        p["location"] = "Jungle"

        collect_item(p)

        ok, message = collect_item(p)

        self.assertFalse(ok)
        self.assertEqual(p["inventory"].count("rope"), 1)

    def test_cannot_collect_item_after_game_over(self):
        p = new_game("Ada")
        p["location"] = "Jungle"
        p["game_over"] = True

        ok, message = collect_item(p)

        self.assertFalse(ok)
        self.assertEqual(message, "The game is over.")
        self.assertNotIn("rope", p["inventory"])        
    
    def test_invalid_command_does_not_change_player_state(self):
        p = new_game("Ada")
        original_state = deepcopy(p)

        ok, message = move(p, "fly")

        self.assertFalse(ok)
        self.assertEqual(p, original_state)
    def test_cannot_light_lighthouse_without_lantern(self):
        p = new_game("Ada")
        p["location"] = "Lighthouse"

        ok, message = light_lighthouse(p)

        self.assertFalse(ok)
        self.assertFalse(p["won"])
        self.assertFalse(p["game_over"])

    def test_player_wins_with_lantern_at_lighthouse(self):
        p = new_game("Ada")
        p["location"] = "Lighthouse"
        p["inventory"].append("lantern")

        ok, message = light_lighthouse(p)

        self.assertTrue(ok)
        self.assertTrue(p["won"])
        self.assertTrue(p["game_over"])

    def test_replay_resets_player_state(self):
        p = new_game("Ada")

        p["location"] = "Cave"
        p["energy"] = 1
        p["inventory"].append("rope")

        new_player = new_game("Ada")

        self.assertEqual(new_player["location"], "Beach")
        self.assertEqual(new_player["energy"], 5)
        self.assertEqual(new_player["inventory"], [])
        self.assertFalse(new_player["game_over"])
        self.assertFalse(new_player["won"])


if __name__ == "__main__":
    unittest.main()