# -*- coding: utf-8 -*-

from django.urls import re_path as url

from player.mahjong_soul.views import (
    ms_accounts,
    get_current_ms_games,
    get_current_ms_games_async
)

urlpatterns = [
    url(r"^accounts/$", ms_accounts, name="ms_accounts"),
    url(r"^games/$", get_current_ms_games, name="get_current_ms_games"),
    url(r"^games/async/$", get_current_ms_games_async, name="get_current_ms_games_async"),
    url(r"^accounts/(?P<stat_type>[\w\-]+)/$", ms_accounts, name="ms_accounts"),
]
