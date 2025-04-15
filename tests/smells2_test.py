import pytest

from smells2 import HumanNose, RobotNose, create_nose

ROSE = "rose"
DAISY = "daisy"
TULIP = "tulip"


def test_human_nose_can_smell():
    n = HumanNose()
    n.smell(ROSE)
    assert ROSE in n.get_smelled_smells()


def test_robot_nose_can_smell():
    n = RobotNose()
    n.smell(ROSE)
    assert ROSE in n.get_smelled_smells()


def test_human_nose_has_allergies():
    n = HumanNose([ROSE])
    # Test that we can smell a non-allergy odor
    n.smell(TULIP)
    assert TULIP in n.get_smelled_smells()

    # Test that we cannot smell an allergy odor
    n.smell(ROSE)
    assert ROSE not in n.get_smelled_smells()

    # When the nose is having an immune response, we can't smell
    with pytest.raises(RuntimeError):
        n.smell(DAISY)

    # Reset the immune response
    n.rest()

    # Now the nose can smell another non-allergy smell
    n.smell(DAISY)
    assert set([DAISY, TULIP]) == n.get_smelled_smells()


def test_robot_nose_has_air_capacity():
    n = RobotNose([], 2)

    # Test that we can smell 2 odors with a capacity of 2
    n.smell(ROSE)
    n.smell(DAISY)

    # If we try to smell with a full air tank, an error is raised
    with pytest.raises(RuntimeError):
        n.smell(TULIP)

    # Rest to reset the air capacity
    n.rest()

    # Now we can smell another smell
    n.smell(TULIP)
    assert set([ROSE, DAISY, TULIP]) == n.get_smelled_smells()


def test_factory_function_creates_correct_nose():
    human_nose = create_nose(allergies=[ROSE])
    robot_nose = create_nose(is_robot=True, air_tank_capacity_liters=5)
    
    assert isinstance(human_nose, HumanNose)
    assert isinstance(robot_nose, RobotNose)
    assert robot_nose.air_tank_capacity_liters == 5
    assert ROSE in human_nose.allergies