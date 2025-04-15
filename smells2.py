class Nose:
    """
    Base class for noses which can smell.
    """
    def __init__(self, allergies=None):
        self.smelled_smells = set()
        self.allergies = allergies or []

    def smell(self, odor):
        """Smell an odor."""
        self.smelled_smells.add(odor)

    def rest(self):
        """Rest the nose. Does not reset the allergies list or set of past smells."""
        pass

    def get_smelled_smells(self):
        """Return a copy of the set of previously encountered odors."""
        return self.smelled_smells.copy()


class HumanNose(Nose):
    """Represents a human nose with allergy responses."""
    
    def __init__(self, allergies=None):
        super().__init__(allergies)
        self.immune_response = False

    def smell(self, odor):
        """
        Smell an odor.
        Humans must not have an active immune response to smell.
        """
        if not self.immune_response:
            if odor in self.allergies:
                self.immune_response = True
            else:
                super().smell(odor)
        else:
            raise RuntimeError("Nose cannot smell when immune response is active.")

    def rest(self):
        """Reset the immune response."""
        self.immune_response = False


class RobotNose(Nose):
    """Represents a robot nose with air tank capacity."""
    
    def __init__(self, allergies=None, air_tank_capacity_liters=20):
        super().__init__(allergies)
        self.air_tank_capacity_liters = air_tank_capacity_liters
        self.current_air_tank_level = 0

    def smell(self, odor):
        """
        Smell an odor.
        Robots must have capacity in their air tank to smell.
        """
        if self.current_air_tank_level < self.air_tank_capacity_liters:
            super().smell(odor)
            self.current_air_tank_level += 1
        else:
            raise RuntimeError("Robot nose cannot smell when air tank is full.")

    def rest(self):
        """Reset the air tank level."""
        self.current_air_tank_level = 0


def create_nose(allergies=None, is_robot=False, air_tank_capacity_liters=20):
    """Factory function to create the appropriate nose type."""
    if is_robot:
        return RobotNose(allergies, air_tank_capacity_liters)
    else:
        return HumanNose(allergies)


if __name__ == "__main__":
    print("Run `pytest tests/smells2_test.py` instead.")