#!/usr/bin/env python3
"""
Author : unho.chang <unho.chang@dataotaku.com>
Date   : 2024-07-11
Purpose: Python Coding Club
"""

import argparse
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Heap abuse", formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        "-a",
        "--adjectives",
        help="Number of adjectives",
        metavar="adjectives",
        type=int,
        default=2,
    )

    parser.add_argument(
        "-n",
        "--number",
        help="Number of insults",
        metavar="insults",
        type=int,
        default=3,
    )

    parser.add_argument(
        "-s",
        "--seed",
        help="Random seed",
        metavar="seed",
        type=int,
        default=None,
    )

    args = parser.parse_args()

    if args.adjectives < 1:
        parser.error(f'--adjectives "{args.adjectives}" must be > 0')

    if args.number < 1:
        parser.error(f'--number "{args.number}" must be > 0')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    adj_arg = args.adjectives
    num_arg = args.number
    seed_arg = args.seed

    adj_list = "bankrupt, baseborn, beef-witted, beetle-headed, beslubbering, boil-brained, clapper-clawed, clay-brained, common-kissing, crook-pated, dismal-dreaming, dizzy-eyed, doghearted, dread-bolted, earth-vexing, elf-skinned, fat-kidneyed, fen-sucked, flap-mouthed, fly-bitten, folly-fallen, fool-born, full-gorged, guts-griping, half-faced, hasty-witted, hedge-born, hell-hated, idle-headed, ill-breeding, ill-nurtured, knotty-pated, milk-livered, motley-minded, onion-eyed, plume-plucked, pottle-deep, pox-marked, reeky, rough-hewn, rude-growing, rump-fed, shard-borne, sheep-biting, spur-galled, swag-bellied, tardy-gaited, tickle-brained, toad-spotted, unchin-snouted, weather-bitten".split(
        ", "
    )

    nown_list = "apple-john, baggage, barnacle, bladder, boar-pig, bugbear, bum-bailey, canker-blossom, clack-dish, clotpole, coxcomb, codpiece, death-token, dewberry, flap-dragon, flax-wench, flirt-gill, foot-lick, fustilarian, giglet, gudgeon, haggard, harpy, hedge-pig, horn-beast, hugger-mugger, jack-a-nape, jolthead, lewdster, lout, maggot-pie, malt-worm, mammet, measle, minnow, miscreant, moldwarp, mumble-news, nut-hook, pigeon-egg, pignut, puttock, pumpion, ratsbane, scut, skainsmate, strumpet, varlot, vassal, whey-face, wagtail, You".split(
        ", "
    )

    adjectives = """
    bankrupt base caterwauling corrupt cullionly detestable dishonest false
    filthsome filthy foolish foul gross heedless indistinguishable infected
    insatiate irksome lascivious lecherous loathsome lubbery old peevish
    rascaly rotten ruinous scurilous scurvy slanderous sodden-witted
    thin-faced toad-spotted unmannered vile wall-eyed
    """.strip().split()

    nouns = """
    Judas Satan ape ass barbermonger beggar block boy braggart butt
    carbuncle coward coxcomb cur dandy degenerate fiend fishmonger fool
    gull harpy jack jolthead knave liar lunatic maw milksop minion
    ratcatcher recreant rogue scold slave swine traitor varlet villain worm
    """.strip().split()

    random.seed(seed_arg)

    statements_out = ""
    for _ in range(num_arg):
        adj_choosed = random.sample(adjectives, adj_arg)
        adj_statement = ", ".join(adj_choosed)
        noun_choosed = random.choice(nouns)
        abuse_statements = f"You {adj_statement} {noun_choosed}!"
        statements_out += abuse_statements + "\n"

    print(statements_out, end="")


# --------------------------------------------------
if __name__ == "__main__":
    main()
