# -*- coding: utf-8 -*

from  allumette_game import *
import pytest
from random import randint



def test_init_packet_of_cigarettes():
    assert [
        ["|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|"],
        ["|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|"],
        ["|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|"]
        ] == init_packet_of_cigarettes()


def test_distrait_level() :
    assert distrait_level(3) in (1, 2, 3)
    assert distrait_level(9) in (1, 2, 3)
    assert distrait_level(13) in (1, 2, 3)


def test_naif_level() :
    assert naif_level(5) in (1, 2, 3)
    assert naif_level(3) in(1, 2, 3)
    assert naif_level(2) in (1, 2)
    assert 1 == naif_level(1)
    

def test_rapide_level() :
    assert 3 == rapide_level(3)
    assert 3 == rapide_level(5)
    assert 2 == rapide_level(2)
    assert 1 == rapide_level(1)

def test_expert_level() :
    assert 1 == expert_level(2)
    assert 2 == expert_level(3)
    assert 3 == expert_level(4)
    assert 1  == expert_level(5)
