# Copyright(C) 2013 by Abe developers.

# genesis_tx.py: known transactions unavailable through RPC for
# historical reasons: https://bitcointalk.org/index.php?topic=119530.0

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public
# License along with this program.  If not, see
# <http://www.gnu.org/licenses/agpl.html>.

def get(tx_hash_hex):
    """
    Given the hexadecimal hash of the genesis transaction (as shown
    by, e.g., "bitcoind getblock 0") return the hexadecimal raw
    transaction.  This works around a Bitcoind limitation described at
    https://bitcointalk.org/index.php?topic=119530.0
    """

    # Main Securecoin chain:
    if tx_hash_hex == "b1814844a286d66d0b6e00966209606002adeb72b8cb8f3db72aa4c96f5da2e9":
        return "700000000000000000000000000000000000000000000000000000000000000000000000e9a25d6fc9a42ab73d8fcbb872ebad026060096296006e0b6dd686a2444881b177201d52ffff0f1e571002000101000000010000000000000000000000000000000000000000000000000000000000000000ffffffff4d04ffff001d0104454175677573742032372c2032303133202d20552e4e2e2070726f62657320616c6c65676564206761732061747461636b3b20552e532e207761726e732044616d6173637573ffffffff01a086010000000000434104e565ca385918acee9899b048250de59e6638f1e0dcd484b033a318901c30f4e85dc324f7e9b0344145b29ca8f2906c397c0d33078d653df70a92e3b16fb2c447ac00000000"

    # Extract your chain's genesis transaction data from the first
    # block file and add it here, or better yet, patch your coin's
    # getrawtransaction to return it on request:
    #if tx_hash_hex == "<HASH>"
    #    return "<DATA>"

    return None
