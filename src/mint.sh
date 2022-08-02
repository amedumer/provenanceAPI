#!/bin/bash
cd ../provenance
provenanced tx wasm execute \
    tp14hj2tavq8fpesdwxxcu44rty3hh90vhujrvcmstl4zr3txmfvw9s96lrg8 \
    "{\"mint\":{\"amount\":\"1000\",\"address\":\"$1\"}}" \
    --from bank1 \
    --keyring-backend test \
    --home build/node0 \
    --chain-id chain-local \
    --gas auto --gas-prices 1905nhash --gas-adjustment 2 \
    --broadcast-mode block \
    --yes \
    --testnet -o json | jq
exit 0