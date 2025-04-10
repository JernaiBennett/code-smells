class Nose:
    """
    Creates a Nose which can smell. Might represent a Robot or Human nose.
    """

    def __init__(self, allergies=None, is_robot=False, air_tank_capacity_liters=20):
        self.smelled_smells = set()
        self.immune_response = False
        self.is_robot = is_robot
        self.allergies = allergies or []
        self.air_tank_capacity_liters = air_tank_capacity_liters
        self.current_air_tank_level = 0
        self.is_running = False

    def smell(self, odor):
        """
        Smell an odor.

        Robots must have capacity in their air tank to smell.
        Humans must not have an active immune response to smell.
        Cyborgs must have both capacity and no immune response to smell.
        """
        if self.is_robot:
            if self.current_air_tank_level < self.air_tank_capacity_liters:
                self.smelled_smells.add(odor)
                self.current_air_tank_level += 1
            else:
                raise RuntimeError("Robot nose cannot smell when air tank is full.")
        else:
            if not self.immune_response:
                if odor in self.allergies:
                    self.immune_response = True
                else:
                    self.smelled_smells.add(odor)
            else:
                raise RuntimeError("Nose cannot smell when immune response is active.")

    def rest(self):
        """
        Rest the nose.

        This resets the immune response for humans and air tank for robots, and both for cyborgs.

        Does not reset the allergies list or set of past smells.
        """
        self.immune_response = False
        self.current_air_tank_level = 0
        self.is_running = False

    def get_smelled_smells(self):
        """
        Return a copy of the set of previously encountered odors.
        """
        return self.smelled_smells.copy()


if __name__ == "__main__":
    print("Run `pytest tests/smells2_test.py` instead.")
