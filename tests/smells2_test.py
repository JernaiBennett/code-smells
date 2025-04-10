import pytest

from smells2 import Nose

ROSE = "rose"
DAISY = "daisy"
TULIP = "tulip"


def test_human_nose_can_smell():
    n = Nose()
    n.smell(ROSE)
    assert ROSE in n.get_smelled_smells()


def test_robot_nose_can_smell():
    n = Nose([], True)
    n.smell(ROSE)
    assert ROSE in n.get_smelled_smells()


def test_human_nose_has_allergies():
    n = Nose([ROSE])
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
    n = Nose([], True, 2)

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
