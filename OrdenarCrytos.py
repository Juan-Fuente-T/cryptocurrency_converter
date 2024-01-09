import csv
import json

# Lista de criptomonedas
criptomonedas = ['bitcoin', 'ethereum', 'tether', 'binancecoin', 'solana', 'ripple', 'usd-coin', 'staked-ether', 'cardano', 'avalanche-2', 'dogecoin', 'polkadot', 'tron', 'chainlink', 'the-open-network', 'matic-network', 'wrapped-bitcoin', 'internet-computer', 'shiba-inu', 'dai', 'litecoin', 'bitcoin-cash', 'uniswap', 'leo-token', 'cosmos', 'injective-protocol', 'stellar', 'near', 'okb', 'optimism', 'ethereum-classic', 'blockstack', 'monero', 'filecoin', 'hedera-hashgraph', 'aptos', 'lido-dao', 'immutable-x', 'crypto-com-chain', 'kaspa', 'vechain', 'arbitrum', 'true-usd', 'celestia', 'mantle', 'first-digital-usd', 'quant-network', 'maker', 'algorand', 'sei-network', 
'the-graph', 'bitcoin-cash-sv', 'ordinals', 'render-token', 'thorchain', 'elrond-erd-2', 'aave', 'bittensor', 'rocket-pool-eth', 'sats-ordinals', 'mina-protocol', 'flow', 'osmosis', 'havven', 'fantom', 'theta-token', 'the-sandbox', 'axie-infinity', 'tokenize-xchange', 'bittorrent', 'kucoin-shares', 'sui', 'wemix-token', 'bitget-token', 'beam-2', 'whitebit', 'cheelee', 'eos', 'neo', 
'decentraland', 'kava', 'tezos', 'oasis-network', 'gala', 'binance-usd', 'iota', 'helium', 'astar', 'usdd', 'woo-network', 'pancakeswap-token', 'terra-luna', 'xdce-crowd-sale', 'fetch-ai', 'frax-ether', 'gatechain-token', 'dydx', 'chiliz', 'akash-network', 'frax', 'conflux-token', 'bonk', 'msol', 'ecash', 'corgiai', 'klay-token', 'frax-share', 'stepn', 'axelar', 'casper-network', 'curve-dao-token', 'rocket-pool', 'arweave', 'blur', 'flare-networks', 'siacoin', 'kujira', 'nexo', 'illuvium', 'compound-wrapped-btc', 'tether-gold', 'apecoin', 'staked-frax-ether', 'ronin', 'pepe', 'compound-ether', 'gnosis', 'coinbase-wrapped-staked-eth', 'gmx', '1inch', 'trust-wallet-token', 'coredaoorg', 'fasttoken', 'metis-token', 'lido-staked-sol', 'deso', 'pax-gold', 'terra-luna-2', 'radix', 'huobi-btc', 'apenft', 'ethereum-name-service', 'skale', 'iotex', 'huobi-token', 'rollbit-coin', 'celo', 'pyth-network', 'zilliqa', 'paxos-standard', 'aelf', 'kusama', 'holotoken', 'aleph-zero', 'basic-attention-token', 'gas', 'chia', 'compound-governance-token', 'singularitynet', 'bitcoin-gold', 'sweth', 'ribbon-finance', 'dash', 'moonbeam', 'lukso-token-2', 'qtum', 'oec-token', 'tellor', 'centrifuge', 'zcash', 'loopring', 'mask-network', 'nem', 'worldcoin-wld', 'stride', 'ethereum-pow-iou', 'pocket-network', 'enjincoin', 'autonolas', 'safepal', 'raydium', 'floki', 'tectum', 'theta-fuel', 'mx-token', 'paypal-usd', 'kadena', 'echelon-prime', '0x', 'beldex', 'benqi-liquid-staked-avax', 'jasmycoin', 'just', 'origintrail', 'decred', 'orca', 'ocean-protocol', 'yearn-finance', 'convex-finance', 'magic']

# Ordenar alfabéticamente
criptomonedas_ordenadas = sorted(criptomonedas)

# Guardar en CSV
csv_filename = 'criptomonedas.csv'
with open(csv_filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Criptomoneda'])
    writer.writerows(map(lambda x: [x], criptomonedas_ordenadas))

# Guardar en JSON
json_filename = 'criptomonedas.json'
with open(json_filename, 'w') as jsonfile:
    json.dump(criptomonedas_ordenadas, jsonfile)

# Mostrar mensaje
print(f"Lista de criptomonedas ordenada alfabéticamente guardada en {csv_filename} (CSV) y {json_filename} (JSON).")
