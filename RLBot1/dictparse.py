import json

FALSE = False

NULL = None

def getjson():
    dict = {
      "data": {
        "platformInfo": {
          "platformSlug": "epic",
          "platformUserId": "65b9945a-13d9-4e53-b08a-48b82d268c84",
          "platformUserHandle": "oFrikk",
          "platformUserIdentifier": "oFrikk",
          "avatarUrl": NULL,
          "additionalParameters": NULL
        },
        "userInfo": {
          "userId": NULL,
          "isPremium": FALSE,
          "isVerified": FALSE,
          "isInfluencer": FALSE,
          "isPartner": FALSE,
          "countryCode": NULL,
          "customAvatarUrl": NULL,
          "customHeroUrl": NULL,
          "customAvatarFrame": NULL,
          "customAvatarFrameInfo": NULL,
          "premiumDuration": NULL,
          "socialAccounts": [],
          "pageviews": 487,
          "xpTier": NULL,
          "isSuspicious": NULL
        },
        "metadata": {
          "lastUpdated": {
            "value": "2023-12-24T22:48:09.8481235+00:00",
            "displayValue": "2023-12-24T22:48:09.8481235+00:00"
          },
          "playerId": 16891578,
          "currentSeason": 27
        },
        "segments": [
          {
            "type": "overview",
            "attributes": {},
            "metadata": {
              "name": "Lifetime"
            },
            "expiryDate": "0001-01-01T00:00:00+00:00",
            "stats": {
              "wins": {
                "rank": 140574,
                "percentile": 96.3,
                "displayName": "Wins",
                "displayCategory": "Performance",
                "category": "performance",
                "description": NULL,
                "metadata": {},
                "value": 7097,
                "displayValue": "7,097",
                "displayType": "Number"
              },
              "goals": {
                "rank": 148284,
                "percentile": 96.2,
                "displayName": "Goals",
                "displayCategory": "Performance",
                "category": "performance",
                "description": NULL,
                "metadata": {},
                "value": 17863,
                "displayValue": "17,863",
                "displayType": "Number"
              },
              "mVPs": {
                "rank": 167249,
                "percentile": 95.7,
                "displayName": "MVPs",
                "displayCategory": "Performance",
                "category": "performance",
                "description": NULL,
                "metadata": {},
                "value": 2988,
                "displayValue": "2,988",
                "displayType": "Number"
              },
              "saves": {
                "rank": 70179,
                "percentile": 98.2,
                "displayName": "Saves",
                "displayCategory": "Performance",
                "category": "performance",
                "description": NULL,
                "metadata": {},
                "value": 18269,
                "displayValue": "18,269",
                "displayType": "Number"
              },
              "assists": {
                "rank": 105958,
                "percentile": 97.2,
                "displayName": "Assists",
                "displayCategory": "Performance",
                "category": "performance",
                "description": NULL,
                "metadata": {},
                "value": 7660,
                "displayValue": "7,660",
                "displayType": "Number"
              },
              "shots": {
                "rank": 81123,
                "percentile": 97.9,
                "displayName": "Shots",
                "displayCategory": "Performance",
                "category": "performance",
                "description": NULL,
                "metadata": {},
                "value": 46299,
                "displayValue": "46,299",
                "displayType": "Number"
              },
              "goalShotRatio": {
                "rank": 8681184,
                "percentile": 0,
                "displayName": "Goal Shot Ratio",
                "displayCategory": "Performance",
                "category": "performance",
                "description": NULL,
                "metadata": {},
                "value": 38.58182682131363,
                "displayValue": "38.6",
                "displayType": "NumberPrecision1"
              },
              "score": {
                "rank": 50351,
                "percentile": 99.3,
                "displayName": "TRN Score",
                "displayCategory": "General",
                "category": "general",
                "description": "Tracker Network Score is a custom formula made to determine skill by considering several factors such as ranked play and goals, mvps, etc.",
                "metadata": {},
                "value": 4472798.732702702,
                "displayValue": "4,472,798.7",
                "displayType": "NumberPrecision1"
              },
              "seasonRewardLevel": {
                "rank": NULL,
                "percentile": 99.1,
                "displayName": "Season Reward Level",
                "displayCategory": "General",
                "category": "general",
                "description": NULL,
                "metadata": {
                  "iconUrl": "https://trackercdn.com/cdn/tracker.gg/rocket-league/ranks/s4-19.png",
                  "rankName": "Grand Champion"
                },
                "value": 7,
                "displayValue": "7",
                "displayType": "Number"
              },
              "seasonRewardWins": {
                "rank": NULL,
                "percentile": NULL,
                "displayName": "Season Reward Wins",
                "displayCategory": "General",
                "category": "general",
                "description": NULL,
                "metadata": {},
                "value": 0,
                "displayValue": "0",
                "displayType": "Number"
              },
              "tRNRating": {
                "rank": NULL,
                "percentile": 85,
                "displayName": "TRN Rating",
                "displayCategory": "General",
                "category": "general",
                "description": "Tracker Network Score is a custom formula made to determine skill by considering several factors such as ranked play and goals, mvps, etc.",
                "metadata": {},
                "value": 2815.742017897484,
                "displayValue": "2,815.7",
                "displayType": "NumberPrecision1"
              }
            }
          },
          {
            "type": "playlist",
            "attributes": {
              "playlistId": 0,
              "season": 27
            },
            "metadata": {
              "name": "Un-Ranked"
            },
            "expiryDate": "0001-01-01T00:00:00+00:00",
            "stats": {
              "tier": {
                "rank": NULL,
                "percentile": NULL,
                "displayName": "Matches",
                "displayCategory": "General",
                "category": "general",
                "description": NULL,
                "metadata": {
                  "iconUrl": "https://trackercdn.com/cdn/tracker.gg/rocket-league/ranks/s4-0.png",
                  "name": "Unranked"
                },
                "value": 0,
                "displayValue": "0",
                "displayType": "Number"
              },
              "division": {
                "rank": NULL,
                "percentile": NULL,
                "displayName": "Matches",
                "displayCategory": "General",
                "category": "general",
                "description": NULL,
                "metadata": {
                  "name": "Division I"
                },
                "value": 0,
                "displayValue": "0",
                "displayType": "Number"
              },
              "matchesPlayed": {
                "rank": NULL,
                "percentile": NULL,
                "displayName": "Matches",
                "displayCategory": "Performance",
                "category": "performance",
                "description": NULL,
                "metadata": {},
                "value": 0,
                "displayValue": "0",
                "displayType": "Number"
              },
              "winStreak": {
                "rank": NULL,
                "percentile": NULL,
                "displayName": "WinStreak",
                "displayCategory": "Performance",
                "category": "performance",
                "description": NULL,
                "metadata": {
                  "type": "win"
                },
                "value": 0,
                "displayValue": "0",
                "displayType": "Number"
              },
              "rating": {
                "rank": 5548,
                "percentile": 99.7,
                "displayName": "Rating",
                "displayCategory": "Skill",
                "category": "skill",
                "description": NULL,
                "metadata": {
                  "iconUrl": "https://trackercdn.com/cdn/tracker.gg/rocket-league/ranks/s4-0.png",
                  "tierName": "Unranked"
                },
                "value": 1752,
                "displayValue": "1,752",
                "displayType": "Number"
              },
              "peakRating": {
                "rank": NULL,
                "percentile": NULL,
                "displayName": "Peak Rating",
                "displayCategory": "Skill",
                "category": "skill",
                "description": NULL,
                "metadata": {},
                "value": NULL,
                "displayValue": NULL,
                "displayType": "Number"
              }
            }
          },
          {
            "type": "playlist",
            "attributes": {
              "playlistId": 10,
              "season": 27
            },
            "metadata": {
              "name": "Ranked Duel 1v1"
            },
            "expiryDate": "0001-01-01T00:00:00+00:00",
            "stats": {
              "tier": {
                "rank": NULL,
                "percentile": 99.4,
                "displayName": "Matches",
                "displayCategory": "General",
                "category": "general",
                "description": NULL,
                "metadata": {
                  "iconUrl": "https://trackercdn.com/cdn/tracker.gg/rocket-league/ranks/s15rank19.png",
                  "name": "Grand Champion I"
                },
                "value": 19,
                "displayValue": "19",
                "displayType": "Number"
              },
              "division": {
                "rank": NULL,
                "percentile": 47,
                "displayName": "Matches",
                "displayCategory": "General",
                "category": "general",
                "description": NULL,
                "metadata": {
                  "deltaDown": 5,
                  "deltaUp": 14,
                  "name": "Division III"
                },
                "value": 2,
                "displayValue": "2",
                "displayType": "Number"
              },
              "matchesPlayed": {
                "rank": NULL,
                "percentile": 98.8,
                "displayName": "Matches",
                "displayCategory": "Performance",
                "category": "performance",
                "description": NULL,
                "metadata": {},
                "value": 39,
                "displayValue": "39",
                "displayType": "Number"
              },
              "winStreak": {
                "rank": NULL,
                "percentile": NULL,
                "displayName": "WinStreak",
                "displayCategory": "Performance",
                "category": "performance",
                "description": NULL,
                "metadata": {
                  "type": "loss"
                },
                "value": 2,
                "displayValue": "-2",
                "displayType": "Number"
              },
              "rating": {
                "rank": 6404,
                "percentile": 99.6,
                "displayName": "Rating",
                "displayCategory": "Skill",
                "category": "skill",
                "description": NULL,
                "metadata": {
                  "iconUrl": "https://trackercdn.com/cdn/tracker.gg/rocket-league/ranks/s15rank19.png",
                  "tierName": "Grand Champion I"
                },
                "value": 1203,
                "displayValue": "1,203",
                "displayType": "Number"
              },
              "peakRating": {
                "rank": NULL,
                "percentile": NULL,
                "displayName": "Peak Rating",
                "displayCategory": "Skill",
                "category": "skill",
                "description": NULL,
                "metadata": {
                  "iconUrl": "https://trackercdn.com/cdn/tracker.gg/rocket-league/ranks/s15rank19.png",
                  "tierName": "Grand Champion I"
                },
                "value": 1212,
                "displayValue": "1,212",
                "displayType": "Number"
              }
            }
          },
          {
            "type": "playlist",
            "attributes": {
              "playlistId": 11,
              "season": 27
            },
            "metadata": {
              "name": "Ranked Doubles 2v2"
            },
            "expiryDate": "0001-01-01T00:00:00+00:00",
            "stats": {
              "tier": {
                "rank": NULL,
                "percentile": 99.5,
                "displayName": "Matches",
                "displayCategory": "General",
                "category": "general",
                "description": NULL,
                "metadata": {
                  "iconUrl": "https://trackercdn.com/cdn/tracker.gg/rocket-league/ranks/s15rank20.png",
                  "name": "Grand Champion II"
                },
                "value": 20,
                "displayValue": "20",
                "displayType": "Number"
              },
              "division": {
                "rank": NULL,
                "percentile": 50,
                "displayName": "Matches",
                "displayCategory": "General",
                "category": "general",
                "description": NULL,
                "metadata": {
                  "deltaDown": 27,
                  "deltaUp": 12,
                  "name": "Division III"
                },
                "value": 2,
                "displayValue": "2",
                "displayType": "Number"
              },
              "matchesPlayed": {
                "rank": NULL,
                "percentile": 98.5,
                "displayName": "Matches",
                "displayCategory": "Performance",
                "category": "performance",
                "description": NULL,
                "metadata": {},
                "value": 140,
                "displayValue": "140",
                "displayType": "Number"
              },
              "winStreak": {
                "rank": NULL,
                "percentile": NULL,
                "displayName": "WinStreak",
                "displayCategory": "Performance",
                "category": "performance",
                "description": NULL,
                "metadata": {
                  "type": "win"
                },
                "value": 1,
                "displayValue": "1",
                "displayType": "Number"
              },
              "rating": {
                "rank": 3214,
                "percentile": 99.8,
                "displayName": "Rating",
                "displayCategory": "Skill",
                "category": "skill",
                "description": NULL,
                "metadata": {
                  "iconUrl": "https://trackercdn.com/cdn/tracker.gg/rocket-league/ranks/s15rank20.png",
                  "tierName": "Grand Champion II"
                },
                "value": 1665,
                "displayValue": "1,665",
                "displayType": "Number"
              },
              "peakRating": {
                "rank": NULL,
                "percentile": NULL,
                "displayName": "Peak Rating",
                "displayCategory": "Skill",
                "category": "skill",
                "description": NULL,
                "metadata": {
                  "iconUrl": "https://trackercdn.com/cdn/tracker.gg/rocket-league/ranks/s15rank20.png",
                  "tierName": "Grand Champion II"
                },
                "value": 1665,
                "displayValue": "1,665",
                "displayType": "Number"
              }
            }
          },
          {
            "type": "playlist",
            "attributes": {
              "playlistId": 13,
              "season": 27
            },
            "metadata": {
              "name": "Ranked Standard 3v3"
            },
            "expiryDate": "0001-01-01T00:00:00+00:00",
            "stats": {
              "tier": {
                "rank": NULL,
                "percentile": 99.5,
                "displayName": "Matches",
                "displayCategory": "General",
                "category": "general",
                "description": NULL,
                "metadata": {
                  "iconUrl": "https://trackercdn.com/cdn/tracker.gg/rocket-league/ranks/s15rank20.png",
                  "name": "Grand Champion II"
                },
                "value": 20,
                "displayValue": "20",
                "displayType": "Number"
              },
              "division": {
                "rank": NULL,
                "percentile": 47,
                "displayName": "Matches",
                "displayCategory": "General",
                "category": "general",
                "description": NULL,
                "metadata": {
                  "deltaDown": 25,
                  "name": "Division III"
                },
                "value": 2,
                "displayValue": "2",
                "displayType": "Number"
              },
              "matchesPlayed": {
                "rank": NULL,
                "percentile": 99.6,
                "displayName": "Matches",
                "displayCategory": "Performance",
                "category": "performance",
                "description": NULL,
                "metadata": {},
                "value": 142,
                "displayValue": "142",
                "displayType": "Number"
              },
              "winStreak": {
                "rank": NULL,
                "percentile": NULL,
                "displayName": "WinStreak",
                "displayCategory": "Performance",
                "category": "performance",
                "description": NULL,
                "metadata": {
                  "type": "loss"
                },
                "value": 1,
                "displayValue": "-1",
                "displayType": "Number"
              },
              "rating": {
                "rank": 6807,
                "percentile": 99.9,
                "displayName": "Rating",
                "displayCategory": "Skill",
                "category": "skill",
                "description": NULL,
                "metadata": {
                  "iconUrl": "https://trackercdn.com/cdn/tracker.gg/rocket-league/ranks/s15rank20.png",
                  "tierName": "Grand Champion II"
                },
                "value": 1671,
                "displayValue": "1,671",
                "displayType": "Number"
              },
              "peakRating": {
                "rank": NULL,
                "percentile": NULL,
                "displayName": "Peak Rating",
                "displayCategory": "Skill",
                "category": "skill",
                "description": NULL,
                "metadata": {
                  "iconUrl": "https://trackercdn.com/cdn/tracker.gg/rocket-league/ranks/s15rank20.png",
                  "tierName": "Grand Champion II"
                },
                "value": 1671,
                "displayValue": "1,671",
                "displayType": "Number"
              }
            }
          },
          {
            "type": "playlist",
            "attributes": {
              "playlistId": 27,
              "season": 27
            },
            "metadata": {
              "name": "Hoops"
            },
            "expiryDate": "0001-01-01T00:00:00+00:00",
            "stats": {
              "tier": {
                "rank": NULL,
                "percentile": 97.5,
                "displayName": "Matches",
                "displayCategory": "General",
                "category": "general",
                "description": NULL,
                "metadata": {
                  "iconUrl": "https://trackercdn.com/cdn/tracker.gg/rocket-league/ranks/s4-16.png",
                  "name": "Champion I"
                },
                "value": 16,
                "displayValue": "16",
                "displayType": "Number"
              },
              "division": {
                "rank": NULL,
                "percentile": 28,
                "displayName": "Matches",
                "displayCategory": "General",
                "category": "general",
                "description": NULL,
                "metadata": {
                  "deltaDown": 3,
                  "deltaUp": 10,
                  "name": "Division II"
                },
                "value": 1,
                "displayValue": "1",
                "displayType": "Number"
              },
              "matchesPlayed": {
                "rank": NULL,
                "percentile": 88,
                "displayName": "Matches",
                "displayCategory": "Performance",
                "category": "performance",
                "description": NULL,
                "metadata": {},
                "value": 1,
                "displayValue": "1",
                "displayType": "Number"
              },
              "winStreak": {
                "rank": NULL,
                "percentile": NULL,
                "displayName": "WinStreak",
                "displayCategory": "Performance",
                "category": "performance",
                "description": NULL,
                "metadata": {
                  "type": "loss"
                },
                "value": 1,
                "displayValue": "-1",
                "displayType": "Number"
              },
              "rating": {
                "rank": 42451,
                "percentile": 97.6,
                "displayName": "Rating",
                "displayCategory": "Skill",
                "category": "skill",
                "description": NULL,
                "metadata": {
                  "iconUrl": "https://trackercdn.com/cdn/tracker.gg/rocket-league/ranks/s4-16.png",
                  "tierName": "Champion I"
                },
                "value": 938,
                "displayValue": "938",
                "displayType": "Number"
              },
              "peakRating": {
                "rank": NULL,
                "percentile": NULL,
                "displayName": "Peak Rating",
                "displayCategory": "Skill",
                "category": "skill",
                "description": NULL,
                "metadata": {
                  "iconUrl": "https://trackercdn.com/cdn/tracker.gg/rocket-league/ranks/s4-16.png",
                  "tierName": "Champion I"
                },
                "value": 938,
                "displayValue": "938",
                "displayType": "Number"
              }
            }
          },
          {
            "type": "playlist",
            "attributes": {
              "playlistId": 28,
              "season": 27
            },
            "metadata": {
              "name": "Rumble"
            },
            "expiryDate": "0001-01-01T00:00:00+00:00",
            "stats": {
              "tier": {
                "rank": NULL,
                "percentile": 97.8,
                "displayName": "Matches",
                "displayCategory": "General",
                "category": "general",
                "description": NULL,
                "metadata": {
                  "iconUrl": "https://trackercdn.com/cdn/tracker.gg/rocket-league/ranks/s4-17.png",
                  "name": "Champion II"
                },
                "value": 17,
                "displayValue": "17",
                "displayType": "Number"
              },
              "division": {
                "rank": NULL,
                "percentile": 76,
                "displayName": "Matches",
                "displayCategory": "General",
                "category": "general",
                "description": NULL,
                "metadata": {
                  "deltaDown": 7,
                  "deltaUp": 10,
                  "name": "Division IV"
                },
                "value": 3,
                "displayValue": "3",
                "displayType": "Number"
              },
              "matchesPlayed": {
                "rank": NULL,
                "percentile": 95.8,
                "displayName": "Matches",
                "displayCategory": "Performance",
                "category": "performance",
                "description": NULL,
                "metadata": {},
                "value": 7,
                "displayValue": "7",
                "displayType": "Number"
              },
              "winStreak": {
                "rank": NULL,
                "percentile": NULL,
                "displayName": "WinStreak",
                "displayCategory": "Performance",
                "category": "performance",
                "description": NULL,
                "metadata": {
                  "type": "loss"
                },
                "value": 1,
                "displayValue": "-1",
                "displayType": "Number"
              },
              "rating": {
                "rank": 23808,
                "percentile": 98.6,
                "displayName": "Rating",
                "displayCategory": "Skill",
                "category": "skill",
                "description": NULL,
                "metadata": {
                  "iconUrl": "https://trackercdn.com/cdn/tracker.gg/rocket-league/ranks/s4-17.png",
                  "tierName": "Champion II"
                },
                "value": 1104,
                "displayValue": "1,104",
                "displayType": "Number"
              },
              "peakRating": {
                "rank": NULL,
                "percentile": NULL,
                "displayName": "Peak Rating",
                "displayCategory": "Skill",
                "category": "skill",
                "description": NULL,
                "metadata": {
                  "iconUrl": "https://trackercdn.com/cdn/tracker.gg/rocket-league/ranks/s4-17.png",
                  "tierName": "Champion II"
                },
                "value": 1104,
                "displayValue": "1,104",
                "displayType": "Number"
              }
            }
          },
          {
            "type": "playlist",
            "attributes": {
              "playlistId": 29,
              "season": 27
            },
            "metadata": {
              "name": "Dropshot"
            },
            "expiryDate": "0001-01-01T00:00:00+00:00",
            "stats": {
              "tier": {
                "rank": NULL,
                "percentile": 98.8,
                "displayName": "Matches",
                "displayCategory": "General",
                "category": "general",
                "description": NULL,
                "metadata": {
                  "iconUrl": "https://trackercdn.com/cdn/tracker.gg/rocket-league/ranks/s4-18.png",
                  "name": "Champion III"
                },
                "value": 18,
                "displayValue": "18",
                "displayType": "Number"
              },
              "division": {
                "rank": NULL,
                "percentile": 77,
                "displayName": "Matches",
                "displayCategory": "General",
                "category": "general",
                "description": NULL,
                "metadata": {
                  "deltaDown": 11,
                  "deltaUp": 6,
                  "name": "Division IV"
                },
                "value": 3,
                "displayValue": "3",
                "displayType": "Number"
              },
              "matchesPlayed": {
                "rank": NULL,
                "percentile": NULL,
                "displayName": "Matches",
                "displayCategory": "Performance",
                "category": "performance",
                "description": NULL,
                "metadata": {},
                "value": 0,
                "displayValue": "0",
                "displayType": "Number"
              },
              "winStreak": {
                "rank": NULL,
                "percentile": NULL,
                "displayName": "WinStreak",
                "displayCategory": "Performance",
                "category": "performance",
                "description": NULL,
                "metadata": {
                  "type": "loss"
                },
                "value": 1,
                "displayValue": "-1",
                "displayType": "Number"
              },
              "rating": {
                "rank": 10253,
                "percentile": 99.3,
                "displayName": "Rating",
                "displayCategory": "Skill",
                "category": "skill",
                "description": NULL,
                "metadata": {
                  "iconUrl": "https://trackercdn.com/cdn/tracker.gg/rocket-league/ranks/s4-18.png",
                  "tierName": "Champion III"
                },
                "value": 1048,
                "displayValue": "1,048",
                "displayType": "Number"
              },
              "peakRating": {
                "rank": NULL,
                "percentile": NULL,
                "displayName": "Peak Rating",
                "displayCategory": "Skill",
                "category": "skill",
                "description": NULL,
                "metadata": {},
                "value": NULL,
                "displayValue": NULL,
                "displayType": "Number"
              }
            }
          },
          {
            "type": "playlist",
            "attributes": {
              "playlistId": 30,
              "season": 27
            },
            "metadata": {
              "name": "Snowday"
            },
            "expiryDate": "0001-01-01T00:00:00+00:00",
            "stats": {
              "tier": {
                "rank": NULL,
                "percentile": 77,
                "displayName": "Matches",
                "displayCategory": "General",
                "category": "general",
                "description": NULL,
                "metadata": {
                  "iconUrl": "https://trackercdn.com/cdn/tracker.gg/rocket-league/ranks/s4-11.png",
                  "name": "Platinum II"
                },
                "value": 11,
                "displayValue": "11",
                "displayType": "Number"
              },
              "division": {
                "rank": NULL,
                "percentile": 43,
                "displayName": "Matches",
                "displayCategory": "General",
                "category": "general",
                "description": NULL,
                "metadata": {
                  "deltaDown": 7,
                  "deltaUp": 12,
                  "name": "Division II"
                },
                "value": 1,
                "displayValue": "1",
                "displayType": "Number"
              },
              "matchesPlayed": {
                "rank": NULL,
                "percentile": NULL,
                "displayName": "Matches",
                "displayCategory": "Performance",
                "category": "performance",
                "description": NULL,
                "metadata": {},
                "value": 0,
                "displayValue": "0",
                "displayType": "Number"
              },
              "winStreak": {
                "rank": NULL,
                "percentile": NULL,
                "displayName": "WinStreak",
                "displayCategory": "Performance",
                "category": "performance",
                "description": NULL,
                "metadata": {
                  "type": "loss"
                },
                "value": 8,
                "displayValue": "-8",
                "displayType": "Number"
              },
              "rating": {
                "rank": 547193,
                "percentile": 69,
                "displayName": "Rating",
                "displayCategory": "Skill",
                "category": "skill",
                "description": NULL,
                "metadata": {
                  "iconUrl": "https://trackercdn.com/cdn/tracker.gg/rocket-league/ranks/s4-11.png",
                  "tierName": "Platinum II"
                },
                "value": 686,
                "displayValue": "686",
                "displayType": "Number"
              },
              "peakRating": {
                "rank": NULL,
                "percentile": NULL,
                "displayName": "Peak Rating",
                "displayCategory": "Skill",
                "category": "skill",
                "description": NULL,
                "metadata": {},
                "value": NULL,
                "displayValue": NULL,
                "displayType": "Number"
              }
            }
          },
          {
            "type": "playlist",
            "attributes": {
              "playlistId": 34,
              "season": 27
            },
            "metadata": {
              "name": "Tournament Matches"
            },
            "expiryDate": "0001-01-01T00:00:00+00:00",
            "stats": {
              "tier": {
                "rank": NULL,
                "percentile": 99.3,
                "displayName": "Matches",
                "displayCategory": "General",
                "category": "general",
                "description": NULL,
                "metadata": {
                  "iconUrl": "https://trackercdn.com/cdn/tracker.gg/rocket-league/ranks/s15rank20.png",
                  "name": "Grand Champion II"
                },
                "value": 20,
                "displayValue": "20",
                "displayType": "Number"
              },
              "division": {
                "rank": NULL,
                "percentile": 27,
                "displayName": "Matches",
                "displayCategory": "General",
                "category": "general",
                "description": NULL,
                "metadata": {
                  "deltaDown": 14,
                  "deltaUp": 23,
                  "name": "Division II"
                },
                "value": 1,
                "displayValue": "1",
                "displayType": "Number"
              },
              "matchesPlayed": {
                "rank": NULL,
                "percentile": 61,
                "displayName": "Matches",
                "displayCategory": "Performance",
                "category": "performance",
                "description": NULL,
                "metadata": {},
                "value": 5,
                "displayValue": "5",
                "displayType": "Number"
              },
              "winStreak": {
                "rank": NULL,
                "percentile": NULL,
                "displayName": "WinStreak",
                "displayCategory": "Performance",
                "category": "performance",
                "description": NULL,
                "metadata": {
                  "type": "loss"
                },
                "value": 1,
                "displayValue": "-1",
                "displayType": "Number"
              },
              "rating": {
                "rank": 2851,
                "percentile": 99.6,
                "displayName": "Rating",
                "displayCategory": "Skill",
                "category": "skill",
                "description": NULL,
                "metadata": {
                  "iconUrl": "https://trackercdn.com/cdn/tracker.gg/rocket-league/ranks/s15rank20.png",
                  "tierName": "Grand Champion II"
                },
                "value": 1615,
                "displayValue": "1,615",
                "displayType": "Number"
              },
              "peakRating": {
                "rank": NULL,
                "percentile": NULL,
                "displayName": "Peak Rating",
                "displayCategory": "Skill",
                "category": "skill",
                "description": NULL,
                "metadata": {
                  "iconUrl": "https://trackercdn.com/cdn/tracker.gg/rocket-league/ranks/s15rank20.png",
                  "tierName": "Grand Champion II"
                },
                "value": 1627,
                "displayValue": "1,627",
                "displayType": "Number"
              }
            }
          }
        ],
        "availableSegments": [
          {
            "type": "playlist",
            "attributes": {
              "season": 1
            },
            "metadata": {
              "name": "1"
            }
          },
          {
            "type": "playlist",
            "attributes": {
              "season": 2
            },
            "metadata": {
              "name": "2"
            }
          },
          {
            "type": "playlist",
            "attributes": {
              "season": 3
            },
            "metadata": {
              "name": "3"
            }
          },
          {
            "type": "playlist",
            "attributes": {
              "season": 4
            },
            "metadata": {
              "name": "4"
            }
          },
          {
            "type": "playlist",
            "attributes": {
              "season": 5
            },
            "metadata": {
              "name": "5"
            }
          },
          {
            "type": "playlist",
            "attributes": {
              "season": 6
            },
            "metadata": {
              "name": "6"
            }
          },
          {
            "type": "playlist",
            "attributes": {
              "season": 7
            },
            "metadata": {
              "name": "7"
            }
          },
          {
            "type": "playlist",
            "attributes": {
              "season": 8
            },
            "metadata": {
              "name": "8"
            }
          },
          {
            "type": "playlist",
            "attributes": {
              "season": 9
            },
            "metadata": {
              "name": "9"
            }
          },
          {
            "type": "playlist",
            "attributes": {
              "season": 10
            },
            "metadata": {
              "name": "10"
            }
          },
          {
            "type": "playlist",
            "attributes": {
              "season": 11
            },
            "metadata": {
              "name": "11"
            }
          },
          {
            "type": "playlist",
            "attributes": {
              "season": 12
            },
            "metadata": {
              "name": "12"
            }
          },
          {
            "type": "playlist",
            "attributes": {
              "season": 13
            },
            "metadata": {
              "name": "13"
            }
          },
          {
            "type": "playlist",
            "attributes": {
              "season": 14
            },
            "metadata": {
              "name": "14"
            }
          },
          {
            "type": "playlist",
            "attributes": {
              "season": 15
            },
            "metadata": {
              "name": "Season 1 (15)"
            }
          },
          {
            "type": "playlist",
            "attributes": {
              "season": 16
            },
            "metadata": {
              "name": "Season 2 (16)"
            }
          },
          {
            "type": "playlist",
            "attributes": {
              "season": 17
            },
            "metadata": {
              "name": "Season 3 (17)"
            }
          },
          {
            "type": "playlist",
            "attributes": {
              "season": 18
            },
            "metadata": {
              "name": "Season 4 (18)"
            }
          },
          {
            "type": "playlist",
            "attributes": {
              "season": 19
            },
            "metadata": {
              "name": "Season 5 (19)"
            }
          },
          {
            "type": "playlist",
            "attributes": {
              "season": 20
            },
            "metadata": {
              "name": "Season 6 (20)"
            }
          },
          {
            "type": "playlist",
            "attributes": {
              "season": 21
            },
            "metadata": {
              "name": "Season 7 (21)"
            }
          },
          {
            "type": "playlist",
            "attributes": {
              "season": 22
            },
            "metadata": {
              "name": "Season 8 (22)"
            }
          },
          {
            "type": "playlist",
            "attributes": {
              "season": 23
            },
            "metadata": {
              "name": "Season 9 (23)"
            }
          },
          {
            "type": "playlist",
            "attributes": {
              "season": 24
            },
            "metadata": {
              "name": "Season 10 (24)"
            }
          },
          {
            "type": "playlist",
            "attributes": {
              "season": 25
            },
            "metadata": {
              "name": "Season 11 (25)"
            }
          },
          {
            "type": "playlist",
            "attributes": {
              "season": 26
            },
            "metadata": {
              "name": "Season 12 (26)"
            }
          },
          {
            "type": "playlist",
            "attributes": {
              "season": 27
            },
            "metadata": {
              "name": "Season 13 (27)"
            }
          }
        ],
        "expiryDate": "2023-12-24T22:52:09.913135+00:00"
      }
    }
    return dict

# playlistCount gets iterated by 1 then condition is >= 1 so it ignores lifetime
# condition for 1 is for unranked
# anything else is ranked playlists
playlistCount = 0
dict = getjson()
for data in dict["data"]["segments"]:
  print(json.dumps(data))

  if playlistCount == 1:
    playlistName = data["metadata"]["name"]  # Gives playlist name -> Unranked
    unrankedMMR = data["stats"]["rating"]["value"]
    print(playlistName)
    print(unrankedMMR)

  elif playlistCount > 1:
    playlistName = data["metadata"]["name"]  # Gives playlist name -> All other playlists
    rankName = data["stats"]["tier"]["metadata"]["name"]  # Gives rank name
    divisionName = data["stats"]["division"]["metadata"]["name"]
    MMR = data["stats"]["rating"]["value"]
    print(playlistName)
    print(rankName)
    print(divisionName)
    print(MMR)

  playlistCount += 1

