import pytest
from television import Television

def test_init():
    tv = Television()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_power_toggle():
    tv = Television()
    tv.power()
    assert "Power = True" in str(tv)
    tv.power()
    assert "Power = False" in str(tv)

def test_mute_behavior():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.mute()
    assert "Volume = 1" in str(tv)
    tv.volume_up()
    assert "Volume = 2" in str(tv)

def test_channel_up_wrap():
    tv = Television()
    tv.power()
    for _ in range(5):
        tv.channel_up()
    assert "Channel = 1" in str(tv)

def test_channel_down_wrap():
    tv = Television()
    tv.power()
    tv.channel_down()
    assert "Channel = 3" in str(tv)

def test_volume_up_max_and_unmute():
    tv = Television()
    tv.power()
    tv.mute()
    tv.volume_up()
    tv.volume_up()
    tv.volume_up()
    assert "Volume = 2" in str(tv)

def test_volume_down_min_and_unmute():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.mute()
    tv.volume_down()
    tv.volume_down()
    tv.volume_down()
    assert "Volume = 0" in str(tv)