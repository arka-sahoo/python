import pytest
from television import *

class Test:
    def setup_method(self):
        self.t1 = Television()
        self.t2 = Television()
        self.t3 = Television()
        self.t4 = Television()
        self.t5 = Television()
        self.t6 = Television()
        self.t7 = Television()

    def test_init(self):
        assert self.t1.__str__() == f'Power = False, Channel = 0, Volume = 0'

    def test_power(self):
        assert "Power = False" in self.t2.__str__()
        self.t2.power()
        assert "Power = True" in self.t2.__str__()
        self.t2.power()

    def test_mute(self):
        self.t3.power()
        self.t3.volume_up()
        assert self.t3.__str__() == f'Power = True, Channel = 0, Volume = 1'
        self.t3.mute()
        assert self.t3.__str__() == f'Power = True, Channel = 0, Volume = 0'
        self.t3.power()
        assert self.t3.__str__() == f'Power = False, Channel = 0, Volume = 0'
        self.t3.mute()
        assert self.t3.__str__() == f'Power = False, Channel = 0, Volume = 0'

    def test_channel_up(self):
        self.t4.channel_up()
        assert self.t4.__str__() == f'Power = False, Channel = 0, Volume = 0'
        self.t4.power()
        self.t4.channel_up()
        assert self.t4.__str__() == f'Power = True, Channel = 1, Volume = 0'
        self.t4.channel_up()
        self.t4.channel_up()
        self.t4.channel_up()
        assert self.t4.__str__() == f'Power = True, Channel = 0, Volume = 0'

    def test_channel_down(self):
        self.t5.channel_down()
        assert self.t4.__str__() == f'Power = False, Channel = 0, Volume = 0'
        self.t4.power()
        self.t4.channel_down()
        assert self.t4.__str__() == f'Power = True, Channel = 3, Volume = 0'

    def test_volume_up(self):
        self.t6.volume_up()
        assert self.t6.__str__() == f'Power = False, Channel = 0, Volume = 0'
        self.t6.power()
        self.t6.volume_up()
        assert self.t6.__str__() == f'Power = True, Channel = 0, Volume = 1'
        self.t6.mute()
        assert self.t6.__str__() == f'Power = True, Channel = 0, Volume = 0'
        self.t6.mute()
        self.t6.volume_up()
        self.t6.volume_up()
        assert self.t6.__str__() == f'Power = True, Channel = 0, Volume = 2'

    def test_volume_down(self):
        self.t7.volume_down()
        assert self.t7.__str__() == f'Power = False, Channel = 0, Volume = 0'
        self.t7.power()
        self.t7.volume_up()
        self.t7.volume_up()
        self.t7.volume_down()
        assert self.t7.__str__() == f'Power = True, Channel = 0, Volume = 1'
        self.t7.mute()
        self.t7.volume_down()
        assert self.t7.__str__() == f'Power = True, Channel = 0, Volume = 0'
        self.t7.volume_down()
        self.t7.volume_down()
        assert self.t7.__str__() == f'Power = True, Channel = 0, Volume = 0'