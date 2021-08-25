#    Copyright (C) 2021 Pranav Taysheti 
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>. 

"""
====================
Credentials
====================
This module contains a class to save authentication objects from tweepy, praw,
and other modules.

The way tweepy and praw authentication works:
--------------------------------------------------

"""
  
import praw
import tweepy

class Credentials():
    """Credentials class
    ========================
    Stores the successfully authenticated tweepy and praw objects for use
    throughout the program.

    Members:
    --------------------------
    :twitter_auth: Authenticates the tweepy library and stores the `tweepy.api`
    object in `tweepy_api`.
    :reddit_auth: Authenticates praw library and stores `praw.reddit` oject in
    `reddit_api`.
    :reddit_api:
    :twitter_api:
    """

    def __init__(self):
        self.twitter_api = None
        self.reddit_api = None

    def auth_twitter(self):
        pass

    def auth_reddit(self):
        pass