__author__ = 'lukeberr'
from transit_api import Stop, Transit
from nose.tools import assert_equal

class test_transit_api:
    def setup(self):
        self.stop_id = "1_23390"
        self.transit = Transit()

    def teardown(self):
        pass

    def test_get_stop(self):
        mystop = self.transit.get_stop(self.stop_id)
        assert_equal(mystop.id, self.stop_id, "ID mismatch when getting stop")
        assert_equal(mystop.heading, "S", "got unexpected stop heading")
