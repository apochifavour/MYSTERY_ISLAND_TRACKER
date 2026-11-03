import unittest
from game import new_game, move, collect_item, light_lighthouse

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
        self.assertIn("You have run out of energy!", message)
    def test_cannot_cross_bridge_without_rope(self):
        p = new_game("Ada")
        p["location"] = "Cave"

        ok, _ = move(p, "bridge")

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

        ok, _ = move(p, "north")

        self.assertFalse(ok)
        self.assertEqual(p["energy"], 5)

    def test_successful_move_costs_energy(self):
        p = new_game("Ada")

        ok, _ = move(p, "jungle")

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
      
    def test_collect_lantern_in_cave(self):
        p = new_game("Ada")
        p["location"] = "Cave"

        ok, message = collect_item(p)

        self.assertTrue(ok)
        self.assertIn("lantern", p["inventory"])


    def test_cannot_light_lighthouse_without_lantern(self):
        p = new_game("Ada")
        p["location"] = "Lighthouse"

        ok, message = light_lighthouse(p)

        self.assertFalse(ok)
        self.assertFalse(p["won"])


    def test_can_win_with_lantern(self):
        p = new_game("Ada")
        p["location"] = "Lighthouse"
        p["inventory"].append("lantern")

        ok, message = light_lighthouse(p)

        self.assertTrue(ok)
        self.assertTrue(p["won"])
        self.assertTrue(p["game_over"])        
    def test_cannot_move_after_game_over(self):
        p = new_game("Ada")
        p["game_over"] = True

        ok, message = move(p, "jungle")

        self.assertFalse(ok)
        self.assertEqual(message, "The game is over.")

    def test_cannot_collect_item_after_game_over(self):
        p = new_game("Ada")
        p["location"] = "Jungle"
        p["game_over"] = True

        ok, message = collect_item(p)

        self.assertFalse(ok)
        self.assertEqual(message, "The game is over.")
        self.assertNotIn("rope", p["inventory"])

if __name__ == "__main__":
    unittest.main()
