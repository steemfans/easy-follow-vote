#!/usr/bin/python3 -u
#encoding:UTF-8
import json, os, sys, time
from contextlib import suppress
from concurrent import futures
from steem.blockchain import Blockchain
from steem.steemd import Steemd
from steem.commit import Commit
from steem.account import Account
from steem.post import Post
from steem import Steem
import traceback

env_dist = os.environ

# init block config
print('-------- env params --------')
steemd_url = env_dist.get('STEEMD')
if steemd_url == None or steemd_url == "":
    steemd_url = 'https://api.steemit.com'
print('STEEMD: %s' % steemd_url)

worker_num = env_dist.get('WORKER_NUM')
if worker_num == None or worker_num == "":
    worker_num = 5
print('WORKER_NUM: %s' % (worker_num))
worker_num = int(worker_num)

to_follow_str = env_dist.get('TO_FOLLOW')
if to_follow_str == None or to_follow_str == "":
    print('need setting TO_FOLLOW')
    sys.exit()
to_follow = to_follow_str.split(',')
print('TO_FOLLOW: %s' % (to_follow_str))

voter = env_dist.get('VOTER')
if voter == None or voter == "":
    print('need setting VOTER')
    sys.exit()
print('VOTER: %s' % (voter))

voter_priv_key = env_dist.get('VOTER_PRIV_KEY')
if voter_priv_key == None or voter_priv_key == "":
    print('need setting VOTER_PRIV_KEY')
    sys.exit()

weight = env_dist.get('WEIGHT')
if weight == None or weight == "":
    weight = 50
weight = int(weight)
print('WEIGHT: %s' % (weight))

vp_threshold = env_dist.get('VP_THRESHOLD')
if vp_threshold == None or vp_threshold == "":
    vp_threshold = 30
vp_threshold = int(vp_threshold)
print('VP_THRESHOLD: %s' % (vp_threshold))

print('-------- env params --------')

# init blockchain
steemd_nodes = [
    steemd_url,
]
S = Steem(nodes=steemd_nodes, keys=[voter_priv_key])
s = S.steemd
c = S.commit
b = Blockchain(s)

def worker(start, end):
    try:
        print('start from {start} to {end}'.format(start=start, end=end))
        
        # get block
        block_infos = s.get_blocks(range(start, end+1))
        # print(block_infos)
        for block_info in block_infos:
            transactions = block_info['transactions']
            for trans in transactions:
                # print(trans)
                operations = trans['operations']
                for op in operations:
                    if op[0] in ['vote']:
                        if op[1]['voter'] in to_follow:
                            if current_voting_power(voter) > vp_threshold:
                                post_str = op[1]['author'] + '/' + op[1]['permlink']
                                post_instance = Post(post_str, s)
                                voter_instance = Account(voter, s)
                                if voter_instance.has_voted(post_instance):
                                    print('[log] has voted %s' % (post_str))
                                else:
                                    c.vote(post_str, weight, voter)
                                    print('[log] follow %s to vote %s by %s' % (op[1]['voter'], post_str, weight))
                            else:
                                print('[log] voting power is not enough.')
    except:
        print('[error] from %s to %s' % (start, end), sys.exc_info())

def current_voting_power(username):
    """
    This helper method also takes into account the regenerated
    voting power.
    """
    account_info = s.get_account(username)
    last_vote_time = parse_time(account_info["last_vote_time"])
    diff_in_seconds = (datetime.datetime.utcnow() -
                       last_vote_time).total_seconds()
    regenerated_vp = diff_in_seconds * 10000 / 86400 / 5
    total_vp = (account_info["voting_power"] + regenerated_vp) / 100
    if total_vp > 100:
        total_vp = 100
    return total_vp

def run():
    start_block_num = int(b.info()['head_block_number'])

    while True:
        end_block_num = int(b.info()['head_block_number'])
        if start_block_num >= end_block_num:
            continue
        if end_block_num - start_block_num >= 50:
            while start_block_num < end_block_num:
                tmp_end_block_num = start_block_num + 50
                if tmp_end_block_num > end_block_num:
                    tmp_end_block_num = end_block_num
                with futures.ThreadPoolExecutor(max_workers=worker_num) as executor:
                    executor.submit(worker, start_block_num, tmp_end_block_num)
                start_block_num = tmp_end_block_num + 1
        else:
            with futures.ThreadPoolExecutor(max_workers=worker_num) as executor:
                executor.submit(worker, start_block_num, end_block_num)
            start_block_num = end_block_num + 1
        print('--- get in sleep ---')
        time.sleep(3)
        print('--- sleep end ---')

if __name__ == '__main__':
    with suppress(KeyboardInterrupt):
        run()
