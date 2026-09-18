
from .. import options, BurnoutParadiseRemasteredWorld
from .bases import BurnoutParadiseRemasteredTestBase


class TestBasic(BurnoutParadiseRemasteredTestBase):
    options = {}
    world: BurnoutParadiseRemasteredWorld

    def test_can_beat_game(self):
        self.collect_all_but([])
        self.assertBeatable(True)

