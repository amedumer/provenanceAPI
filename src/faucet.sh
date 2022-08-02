#!/bin/bash
cd ../provenance
provenanced tx bank send \
    $(provenanced keys show -a node0 --home build/node0 --keyring-backend test --testnet) \
    $1 \
    100000nhash \
    --from node0 \
    --keyring-backend test \
    --home build/node0 \
    --chain-id chain-local \
    --gas auto --gas-prices 1905nhash --gas-adjustment 2 \
    --broadcast-mode block \
    --yes \
    --testnet -o json  | jq
exit 0